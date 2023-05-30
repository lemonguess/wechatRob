import json
import os

import requests
import flask
import logging
from flask import Flask, jsonify, has_request_context, copy_current_request_context, request
from functools import wraps
from concurrent.futures import Future, ThreadPoolExecutor
from get_spider_file import get_file_path
from getmsg import getmsg
import asyncio


def run_async(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        call_result = Future()

        def _run():
            loop = asyncio.new_event_loop()
            try:
                result = loop.run_until_complete(func(*args, **kwargs))
            except Exception as error:
                call_result.set_exception(error)
            else:
                call_result.set_result(result)
            finally:
                loop.close()

        loop_executor = ThreadPoolExecutor(max_workers=1)
        if has_request_context():
            _run = copy_current_request_context(_run)
        loop_future = loop_executor.submit(_run)
        loop_future.result()
        return call_result.result()

    return _wrapper


app = flask.Flask(__name__)


@app.route('/weixin', methods=['POST'])
@run_async
async def main():
    msg, from_name, final_from_name, time_str, from_wxid, final_from_wxid, msg_type, robot_wxid = getmsg()
    # 这一块后面可以写插件主要内容
    # new_msg = '123'
    new_msg = ''
    message = {
        "success": True,
        "message": "successful!",
        "event": "SendTextMsg",
        "robot_wxid": robot_wxid,
        "to_wxid": from_wxid,
        "member_wxid": "",
        "member_name": "",
        "group_wxid": "",
        "msg": new_msg
    }
    if from_wxid in ['23584516242@chatroom', '48377160542@chatroom', 'wxid_rs2fy4y9i5rz22']:
        # sendTextMsg(from_wxid="23584516242@chatroom", new_msg=new_msg, robot_wxid=robot_wxid)
        path = get_file_path(msg)
        # sendFile(from_wxid=from_wxid, path=path, robot_wxid=robot_wxid)
        if path:
            sendFile(from_wxid='48377160542@chatroom', path=path, robot_wxid=robot_wxid)
        else:
            pass
    return jsonify(message)


def sendTextMsg(from_wxid, new_msg, robot_wxid):

    data = dict()
    data["event"] = "SendTextMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = from_wxid
    data["msg"] = str(new_msg)
    res = requests.post(url="http://192.168.3.22:8090", data=json.dumps(data, ensure_ascii=False))
    print(res.json())

def sendFile(from_wxid, path, robot_wxid):
    # path = r"D:\workspace\wechatRob\output\2023-05-27\行路千万里.txt"
    name = path.split(os.sep)[-1]
    data = dict()
    msg = dict()
    data["event"] = "SendFileMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = from_wxid
    msg['name'] = name
    msg["path"] = path
    data['msg'] = msg
    res = requests.post(url="http://127.0.0.1:8090",json=data)
    print(res.json())
def testsend():
    from_wxid = "23584516242@chatroom"
    new_msg = "开呢"
    robot_wxid = "wxid_rs2fy4y9i5rz22"
    sendTextMsg(from_wxid, new_msg, robot_wxid)
def runserver():
    app.config['JSON_AS_ASCII'] = False
    log = logging.getLogger('log')
    log.disabled = True
    app.run(host='0.0.0.0', port=8074, debug=True)
if __name__ == '__main__':
    runserver()
    # from_wxid = "23584516242@chatroom"
    # new_msg = "开呢"
    # robot_wxid = "wxid_rs2fy4y9i5rz22"
    # sendTextMsg(from_wxid, new_msg, robot_wxid)
