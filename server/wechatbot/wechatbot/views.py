from django.views import View
from utils.ResFormatUtil import ResFormat
import json

test_msg = {
    "success": True,
    "message": "successful!",
    "event": "SendImageMsg",
    "robot_wxid": "wxid_rs2fy4y9i5rz22",
    "to_wxid": "wxid_rs2fy4y9i5rz22",
    "member_wxid": "",
    "member_name": "",
    "group_wxid": "",
    "msg": {
        "url": "https://www.ikam.cn/view/img/avatar.png",
        "name": "20201024.jpg"
    }
}


class Weixin(View):
    def post(self, request):
        """
        用户注册
        :param request:
        :return:
        """
        body = json.loads(request.body.decode('utf-8'))
        msg = body.get("msg")
        # email = post.get('email')

        # return ResFormat().json_response()
        res = json.dumps(test_msg, ensure_ascii=False)
        return test_msg
