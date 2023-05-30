# python-CuteCat

可爱猫 iHttp 插件的 python 接口封装 （参考aiocqhttp完成）

~~同时将发送的路径链接转换为url链接，为实现此功能，需要将 WeChat 安装到可爱猫的根目录下~~(新版本无需此设置)

接收事件类型

```
    on_group_msg = on('EventGroupMsg')
    on_friend_msg = on('EventFriendMsg')
    on_received_transfer = on('EventReceivedTransfer')
    on_friend_vertify = on('EventFriendVerify')
    on_sendout_msg = on('EventSendOutMsg')
    on_sys_msg = on('EventSysMsg')
    on_login = on('EventLogin')
```

发送事件类型

```
    def SendTextMsg(self, to_wxid : str, msg : str):...
    def SendImageMsg(self, to_wxid : str, msg : str):...
    def SendVideoMsg(self, to_wxid : str, msg : str):...
    def SendFileMsg(self, to_wxid : str, msg : str):...
    def GetRobotName(self) -> str:...
    def GetFriendList(self) -> List[Dict[str, Any]]:...
    def GetGroupList(self) -> List[Dict[str, Any]]:...
    def GetGroupMemberList(self, group_wxid : str) -> List[Dict[str, Any]]:...
    def GetGroupMemberInfo(self, group_wxid : str, member_wxid : str) -> Dict[str, Any]:...
    def AcceptTransfer(self, to_wxid : str, msg : str):...
    def AgreeGroupInvite(self, msg : str):...
    def AgreeeFriendVerify(self, msg : str):...
    def GetAppDir(self) -> str:...
```

```
1. 安装

pip3 install git+https://github.com/0honus0/python-CuteCat-iHttp.git

2. 使用

demo.py

from CuteCat import CuteCat

bot = CuteCat( api_url = '' , robot_wxid = '' , access_token = '')

@bot.on('EventFriendMsg')
def eventfrinendmsg(msg):
    print(msg)
    bot.SendTextMsg( to_wxid= msg.from_wxid, msg ='hello')

bot.run()
```

设置access_token则需要在插件中开启鉴权
