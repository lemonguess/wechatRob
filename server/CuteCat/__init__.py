from flask import Flask, request, abort, jsonify, Response, send_file
from typing import List, Callable, Coroutine, Dict, Any
from .Event import Event
from .Message import Message
from .Bus import EventBus
from .Api import Api, HttpApi
import logging
import os, re
import magic


class CuteCat(Api):

    def __init__(self, api_url: str = None, self_url: str = 'http://192.168.3.22:8089', robot_wxid: str = None,
                 access_token: str = None):
        self._bus = EventBus()
        self._server_app = Flask(__name__)
        self._server_app.add_url_rule('/event', methods=['POST'], view_func=self._handle_event)
        self._server_app.add_url_rule('/tmp/<filename>', methods=['GET'], view_func=self._handle_request)
        self.logger = self._server_app.logger
        self.api_url = api_url
        self.host = "0.0.0.0"
        self.port = int((re.findall('http://.+?:(.+?)$', self_url))[0])
        if not access_token:
            self._api = HttpApi(api_url=api_url, robot_wxid=robot_wxid)
        else:
            self._api = HttpApi(api_url=api_url, access_token=access_token, robot_wxid=robot_wxid)

    def on(self, *event_type: str) -> Callable:
        def deco(func: Callable) -> Callable:
            for _type in event_type:
                self.subscribe(_type, func)
            return deco

        return deco

    def subscribe(self, event_name: str, func: Callable) -> None:
        self._bus.subscribe(event_name, func)

    def call_action(self, action: str, **params):
        return self._api.call_action(action, **params)

    def _handle_request(self, filename):
        # 增加win下判断，但是可用性未知，根据文档判断不可用
        if 'nt' in os.name:
            path = os.path.expanduser('~').replace('\\', '/') + '/AppData/Local/Temp/' + filename
        else:
            path = '/tmp/' + filename

        if not os.path.exists(path):
            return abort(404)
        else:
            mime = magic.from_file(path, mime=True)
            if isinstance(mime, bytes):
                mime = mime.decode()
            return send_file(path, as_attachment=True, mimetype=mime,
                             download_name=filename + '.' + mime.split('/')[-1])

    def _handle_event(self) -> Any:
        payload = request.json

        ev = Event.from_payload(payload)
        if not ev:
            return

        event_type = ev.type
        self.logger.info(f'received event: {event_type}')

        message = Message(ev)
        ev['type'] = message.type
        if message.type in ['image', 'voice', 'video', 'share', 'file']:
            ev['msg'] = self.url_preprocess(ev)
        results = self._bus.emit(event_type, ev)
        res = results[0] if results else None
        return jsonify(res)

    def url_preprocess(self, msg: str):
        path = msg['msg']
        if ('\\WeChat' in path) or ('\\Applet' in path):
            return f"{self.api_url}/get_file?path={path}"
        else:
            return path

    def run(self,
            *args,
            **kwargs) -> None:
        """运行 bot 对象，实际就是运行 Flask app，参数与 `Flask.run` 一致。"""
        if 'use_reloader' not in kwargs:
            kwargs['use_reloader'] = False
        self._server_app.run(host=self.host, port=self.port, *args, **kwargs)
