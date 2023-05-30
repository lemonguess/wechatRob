## 一、微信机器人概述

### 1.企业微信机器人

刚开始想研究下微信机器人，了解到企业微信类似于钉钉，开放了api可以让开发者进行调用，以便于完成各种操作，但是企业微信有两个致命缺点，让我不得不放弃：

**缺点1**：无法监听消息

钉钉给出了接口，可以让开发者轮询请求，以获得消息，企业微信嘛... 只能发，不能收。

这玩意太伤了，等于说微信机器人纯属群发，根本不能对任何消息作出响应，也就是说，基本等于废物。

**缺点2**：仅限于企业微信群

这个群还不是那种普通账号都可以加入的那种，还是仅限于企业微信群聊中添加官方机器人，解释一下，就是只能下载企业微信APP，在企业微信APP里建立的群聊，才可以使用这个微信机器人。

鉴于以上两点来看，企业微信机器人的应用面极其窄，一般人用这个根本没什么球用，开发这个纯属浪费了我的宝贵时间。

**官方文档：**

[如何设置群机器人 -帮助中心-企业微信 (qq.com)](https://open.work.weixin.qq.com/help2/pc/14931)

[群机器人配置说明 - 接口文档 - 企业微信开发者中心 (qq.com)](https://developer.work.weixin.qq.com/document/path/91770)

python示例：

```python
"""
上传文件功能
"""
import json
import requests
import os

def send_message(media_id):
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7d1e7b25-fa81-4524-bf3a-5b9030bb9068"
    data = {
        "msgtype": "file",
        "file": {
            "media_id": media_id
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.text)
    print(response)
def get_media_id():
    file_path = "傅情.txt"
    filelength = os.path.getsize(file_path)
    headers = {
        # "Content-Type": "application/json",
        # "Content-Length": str(filelength),
        "Content-Disposition": f'form-data; name="media";filename="{file_path}"; filelength={filelength}',
        "Content-Type": "application/octet-stream"

    }
    f = open(file_path, 'rb')
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=7d1e7b25-fa81-4524-bf3a-5b9030bb9068&type=file"
    files = {"file": f}
    response = requests.post(url,
                             # headers=headers,
                             files=files)
    print(response.text)
    print(response)
    return response.json().get('media_id')
if __name__ == '__main__':
    media_id = get_media_id()
    send_message(media_id)
```

### 2.普通微信机器人

***普通微信是没有机器人功能的，官方没有给出任何接口\***

#### 实现原理：1、hook 微信的两种方式

又可以细化为两种。即有 hook PC 端 (Window 系统）的微信，也有 hook 手机端（ Android 系统）的微信。

1. **hook PC 端的代表作：wetool、可爱猫**。功能超级强大，虽不支持二次开发，但已有的功能足够个人使用，可惜官方作品已被腾讯告死，好在市面上还流落着不少破解版，有需要的自行搜索。另外还有一个需要进行二次开发，才能使用的非主流框架可爱猫，需要的自行研究；
2. **hook 移动端的代表作：太极**。功能也很强大，不支持二次开发。使用起来相对比较复杂，一般人玩不起来。 （也是我目前在用的微信机器人）

无论是 PC 端还是手机端，用 hook 方式实现的最大缺点就是要和某一个版本的微信客户端进行绑定，如果框架本身不对最新版本的微信适配，那使用的时候就无法升级到最新版本的微信。

#### 实现原理：2、模拟微信通信协议的两种方式

又可以细化为两种方式。

1. 通过模拟 web 协议的方式 ，代表作：ItChat。曾经红极一时，号称三十行即可自定义个人号机器人。可惜的是，微信官方已不准许新的微信号再使用 web 登录，这就直接从源头扼杀了 web 协议的微信机器人，虽说老的微信号还是能凑合着用，不过部分功能也受限。
2. 通过是非 web 协议，如 Pad 协议、Mac 协议，代表作：wechaty。当然它自身也支持 web 协议，而且 web 协议的机器人是免费的。这哥们打着开源的幌子，主要代码并没有开源，只是提供了一套 SDK 而已，除了 web 以外的通讯协议均付费（大概 200 一个月吧），才提供调用的 token。

以协议的方式来实现不需要和微信客户端绑定，但他们基本上都只提供 API，并不是可以直接拿来用的成品，需要进行二次开发才能使用。二次开发对普通用户来说是个巨大的门槛，但对懂编程的人来说是个巨大的优点，要实现什么功能由开发者来定。如最近很火的 ChatGPT 大都是通过 wechaty 二次开发接入。

#### 从功能上来说

理论上手机端微信机器人的功能是多余 PC 端的。因为手机端微信的功能本身就多余或者说领先 PC 端，例如红包相关的功能，PC 端的微信就无法处理吧。所以抢红包的功能就只能由手机端的微信机器人来做。

不过，PC 端的微信机器人在使用上比手机端方便，尤其是群管理相关的功能，在 PC 上一目了然，一眼看过去就知道如何使用。而手机端就很鸡肋，入口深，配置难！另外就是PC端的微信机器人大都支持二次开发，扩展性很强。

所以，还是要根据自己的业务需求选择适合自己的微信机器人。

### 3. 方案选择

本人实测，选择了可爱猫框架

搭建环境：

- Windows11
- 可爱猫5.2.7
- 微信3.1.0.41

链接：https://pan.baidu.com/s/1PDVo8VDr5mtRd4tu7z5tEw?pwd=ybch
提取码：ybch

![image-20230529200242365](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529200242365.png)

- 其他框架推荐：
  https://itchat.readthedocs.io/zh/latest/
  https://gitee.com/ikam/wx-hook-http

### 4.官方参考链接

[可爱猫iHttp-高性能服务端设计思路～-易语言-i可爱猫论坛-可爱猫小黑,致力于为易语言、PHP语言交流 (ikam.cn)](https://www.ikam.cn/thread-66.htm)

[易语言-i可爱猫论坛-可爱猫小黑,致力于为易语言、PHP语言交流 (ikam.cn)](https://www.ikam.cn/forum-1.htm)

## 二、可爱猫

### 1.功能概述

可爱猫的ihttp插件，逻辑是，通过可爱猫软件启动指定版本的微信，将微信的各种收发等操作通过sdk中转，接收到的消息会post给开发者指定的接口，开发者也可以按一定的格式，将操作信息post给可爱猫的SDK，以完成对微信的操作

![img](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/1_DZMRMHVSHT6GBMS.png)

### 2.使用流程

安装就不说了，但是注意，不同版本的可爱猫，要安装指定版本的微信哦

![image-20230529201103709](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529201103709.png)

![image-20230529201311535](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529201311535.png)

![image-20230529201424408](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529201424408.png)

![image-20230529201548143](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529201548143.png)

![image-20230529201851552](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230529201851552.png)

### 3.服务端开发简述

本人使用flask开发了服务，端口8074，并配置/weixin的post接口，这样所有的微信信息都会发到我这里来，我在分析信息后，再作出相应的回复，如回复消息、发送文件、艾特别人什么的，按可爱猫指定的格式，post给`http://192.168.3.22/8089`

#### api参考(不是我写的，有些不对的，多试试参数)

```python
# coding:utf-8
import json
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import Response

"""
消息事件                      事件说明

EventGroupMsg               群消息事件
EventFriendMsg              私聊消息事件
EventReceivedTransfer       收到转账事件
EventScanCashMoney          面对面收款
EventFriendVerify           好友请求事件
EventContactsChange         朋友变动事件
EventGroupMemberAdd         群成员增加事件
EventGroupMemberDecrease    群成员减少事件（群成员退出）
EventSysMsg                 系统消息事件
"""

"""
事件发送                      发送说明

SendTextMsg                 发送文本消息
SendImageMsg                发送图片消息
SendVideoMsg                发送视频消息
SendFileMsg                 发送文件消息
SendGroupMsgAndAt           发送群消息并艾特
SendEmojiMsg                发送动态表情
SendLinkMsg                 发送分享链接
SendMusicMsg                发送音乐分享
GetRobotName                取登录账号昵称
GetRobotHeadimgurl          取登录账号头像
GetLoggedAccountList        取登录账号列表
GetFriendList               取好友列表
GetGroupList                取群聊列表
GetGroupMemberList          取群成员列表
GetGroupMemberInfo          取群成员详细
AcceptTransfer              接收好友转账
AgreeGroupInvite            同意群聊邀请
AgreeFriendVerify           同意好友请求
EditFriendNote              修改好友备注
DeleteFriend                删除好友
GetappInfo                  取插件信息
GetAppDir                   取应用目录
AddAppLogs                  添加日志
ReloadApp                   重载插件
RemoveGroupMember           踢出群成员
EditGroupName               修改群名称
EditGroupNotice             修改群公告
BuildNewGroup               建立新群
QuitGroup                   退出群聊
InviteInGroup               邀请加入群聊
"""

class AcceptEvent(BaseModel):
    """
    消息接收模型
    """
    # 注：在私聊事件下，from_wxid和final_from_wxid一致
    # 消息事件
    event: Optional[str] = None
    # 机器人微信ID
    robot_wxid: Optional[str] = None
    # 机器人昵称
    robot_name: Optional[str] = None
    # 消息类型  1/文本消息 3/图片消息 34/语音消息  42/名片消息  43/视频 47/动态表情 48/地理位置  49/分享链接  2000/转账 2001/红包  2002/小程序  2003/群邀请
    type: Optional[int] = None
    # 微信群ID
    from_wxid: Optional[str] = None
    # 群名称
    from_name: Optional[str] = None
    # 发信人
    final_from_wxid: Optional[str] = None
    # 发信人昵称
    final_from_name: Optional[str] = None
    # 接收消息的群/人
    to_wxid: Optional[str] = None
    # 消息内容
    msg: Optional[str] = None
    # 金额
    money: Optional[float] = None

def SendTextMsg(robot_wxid, to_wxid, msg):
    """
    发送普通文本消息
    :param robot_wxid:机器人ID
    :param to_wxid:消息接收ID 人/群
    :param msg:文本消息
    :return:发送消息
    """
    data = dict()
    data["event"] = "SendTextMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    data["msg"] = str(msg)
    data = json.dumps(data)
    return Response(data)

def SendImageMsg(robot_wxid, to_wxid, path, name):
    """
    发送图片消息
    :param robot_wxid: 机器人ID
    :param to_wxid: 消息接收ID 人/群
    :param path: 图片URL路径
    :param name: 图片唯一名称
    :return: 发送图片消息
    """
    data = dict()
    msg = dict()
    data["event"] = "SendImageMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg["url"] = path
    msg['name'] = name
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)

def SendVideoMsg(robot_wxid, to_wxid, path, name):
    """
    发送视频消息
    :param robot_wxid: 机器人ID
    :param to_wxid: 消息接收ID 人/群
    :param path: 视频URL路径
    :param name: 视频唯一名称
    :return: 发送视频消息
    """
    data = dict()
    msg = dict()
    data["event"] = "SendVideoMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg["url"] = path
    msg['name'] = name
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)

def SendFileMsg(robot_wxid, to_wxid, path, name):
    """
    发送文件消息
    :param robot_wxid: 机器人ID
    :param to_wxid: 消息接收ID 人/群
    :param path: 文件URL路径
    :param name: 文件唯一名称
    :return: 发送文件频消息
    """
    data = dict()
    msg = dict()
    data["event"] = "SendFileMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg['name'] = name
    msg["url"] = path
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)

'robot_wxid, group_wxid, member_wxid, member_name, msg'

def SendGroupMsgAndAt(robot_wxid, to_wxid, at_id, at_name, msg):
    """
    发送@消息
    :param robot_wxid:机器人ID
    :param to_wxid:消息接收的群ID
    :param at_id:需要@的人ID
    :param at_name:需要@人的名称
    :param msg:文本消息
    :return:发送消息
    """
    data = dict()
    data["event"] = "SendGroupMsgAndAt"
    data["robot_wxid"] = robot_wxid
    data["group_wxid"] = to_wxid
    data['member_wxid'] = at_id
    data['member_name'] = at_name
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)

def SendEmojiMsg(robot_wxid, to_wxid, path, name):
    """
    发送动态表情
    :param robot_wxid: 机器人ID
    :param to_wxid: 接收消息ID 人/群
    :param path: URL路径
    :param name: 文件唯一名称
    :return: 发送消息
    """
    data = dict()
    msg = dict()
    data["event"] = "SendEmojiMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg['name'] = name
    msg["url"] = path
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)

def SendLinkMsg(robot_wxid, to_wxid, title, text, target_url, pic_url=' ', icon_url=' '):
    """
    发送链接卡片消息
    :param robot_wxid: 机器人ID
    :param to_wxid: 接收消息ID 人/群
    :param title: 链接卡片标题
    :param text: 链接卡片文本
    :param target_url: 链接卡片URL
    :param pic_url:
    :param icon_url: 链接卡片图标
    :return: 发送链接卡片消息
    """
    data = dict()
    msg = dict()
    data["event"] = "SendLinkMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg['title'] = title
    msg['text'] = text
    msg['target_url'] = target_url
    msg['pic_url'] = pic_url
    msg['icon_url'] = icon_url
    data['msg'] = msg
    data = json.dumps(data)
    return Response(data)
```

#### 我的

参考了这哥们的代码[可爱猫+python3+Flask+aiohttp简单搭建微信机器人_微信机器人框架_Tokeii的博客-CSDN博客](https://blog.csdn.net/u010418732/article/details/126942827?spm=1001.2014.3001.5501)

缺函数的话直接抄他的吧，有空再整理到github上，总的流程就是这样
