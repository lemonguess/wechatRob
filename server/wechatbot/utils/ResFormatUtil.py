"""
构造一个字典
{
"code":
"msg":
"data"
}
jsonresponse
"""
from django.http import JsonResponse


class ResFormat:
    SUCCESS = 0, '成功'  # status
    PARAM_ERROR = 4001, '参数错误'
    ACCESS_RESTRICTION = 4002, '访问限制'
    ACCOUNT_REGISTRATION = 4003, '账户已注册'
    CODE_EXPIRED = 4004, '验证码过期'
    UPLOAD_EXCEPTION = 4005, '上传异常'
    UNKNOWN_ERROR = 4100, '未知错误'

    def __init__(self, status='SUCCESS', data=''):
        """
        初始化
        :param status: 响应状态，默认状态是成功
        :param data: 响应数据，默认是空
        """
        if hasattr(self, status):  # 检验状态是否存在
            status = getattr(self, status)  # 获取制定对象的指定属性
        else:
            status = self.UNKNOWN_ERROR

        self.code, self.msg = status
        self.data = data

    def res(self):
        """
        构造字典
        :return: 字典
        """
        dic = {'code': self.code}

        if self.msg:
            dic['msg'] = self.msg

        if self.data:
            dic['data'] = self.data

        return dic

    def json_response(self):
        """
        返回转以后的json响应对象
        :return: JsonResponse
        """
        return JsonResponse(self.res(), json_dumps_params={'ensure_ascii': False})
        # json.dumps()6个字符，json。loads()
