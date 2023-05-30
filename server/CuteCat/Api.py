import abc
import functools
from typing import Callable, Any, Union, Awaitable , Optional , Dict
import requests
import json
import logging

class Api:
    """
    API 接口类。
    继承此类的具体实现类应实现异步的 `call_action` 方法。
    """

    @abc.abstractmethod
    def call_action(self, action: str, **params) -> Any:
        ...

    def __getattr__(self,
                    item: str) -> Callable[..., Union[Awaitable[Any], Any]]:
        """获取一个可调用对象，用于调用对应 API。"""
        return functools.partial(self.call_action, item)

class HttpApi(Api):
    """
    HTTP API 实现类。
    """

    def __init__(self, api_url: Optional[str] = None, access_token: Optional[str] = None, robot_wxid: Optional[str] = None):
        super().__init__()
        self._api_url = api_url
        self._access_token = access_token
        self.robot_wxid = robot_wxid

    def call_action(self, action: str, **params) -> Any:
        if not self._api_url:
            raise Exception('ApiNotAvailable')

        headers = {}
        if self._access_token:
            headers['Authorization'] = self._access_token

        param = {
            'msg'         : '',
            'to_wxid'     : '',
            'group_wxid'  : '',
            'member_wxid' : '',
            'success'     : True ,
            'event'       : action ,
            'robot_wxid'  : self.robot_wxid,
        }

        for k , v in params.items():
            param[k] = v

        retry = 3
        while retry > 0:
            try:
                ret = requests.post(self._api_url, headers = headers, json = param , timeout = 30)
                if json.loads(ret.text)['code'] == -1:
                    retry -= 1
                    continue
                return json.loads(ret.text)
            except Exception as e:
                logging.getLogger(__name__).warning(f"call_action {action} failed: {e}")
                retry -= 1
        return {}
        
