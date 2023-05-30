原始api:http://www.uera.cn/api/robot/notice

https://www.uera.cn/api/robot/notice

我的api:http://127.0.0.1:8000/weixin

原始请求使用Charles抓包：没抓到

**官方解释**[可爱猫-httpSDK-完美免费版--ShowDoc (vwzx.com)](https://doc.vwzx.com/web/#/6?page_id=123)

我接收的

```json
{
    "event":"EventGroupMsg",//事件标示(当前值为群消息事件)
    "robot_wxid":"wxid_5hxa04j4z6pg22",//机器人wxid
    "robot_name":"",//机器人昵称，一般为空
    "type":1,//1/文本消息 3/图片消息 34/语音消息  42/名片消息  43/视频 47/动态表情 48/地理位置  49/分享链接  2000/转账 2001/红包  2002/小程序  2003/群邀请
    "from_wxid":"18900134932@chatroom",//群id，群消息事件才有
    "from_name":"微群测",//群名字
    "final_from_wxid":"sundreamer",//发该消息的用户微信id
    "final_from_name":"遗忘悠剑o",//微信昵称
    "to_wxid":"wxid_5hxa04j4z6pg22",//接收消息的人id，（一般是机器人收到了，也有可能是机器人发出的消息，别人收到了，那就是别人）
    "msg":"图片https://b3logfile.com/bing/20201024.jpg",//消息内容(string/array) 使用时候根据不同的事件标示来定义这个值，字符串类型或者数据类型
    "money":0.01 //金额，只有"EventReceivedTransfer"事件才有该参数
}

群：
{
    "event": "EventSendOutMsg",
    "robot_wxid": "wxid_rs2fy4y9i5rz22",
    "robot_name": "",
    "type": 1,
    "from_wxid": "wxid_rs2fy4y9i5rz22",
    "from_name": "",
    "final_from_wxid": "wxid_rs2fy4y9i5rz22",
    "final_from_name": "",
    "to_wxid": "48377160542@chatroom",
    "msgid": "1797651096",
    "msg": 1
}
```

我返回的：

```json
{
    "success":true,//true时，http-sdk才处理，false直接丢弃
    "message":"successful!",
    "event":"SendImageMsg",//告诉它干什么，SendImageMsg是发送图片事件
    "robot_wxid":"wxid_5hxa04j4z6pg22",//用哪个机器人发
    "to_wxid":"18900134932@chatroom",//发到哪里？群/好友
    "member_wxid":"",
    "member_name":"",
    "group_wxid":"",
    "msg":{//消息内容:发送 图片、视频、文件、动态表情都是这个结构
        "url":"https:\/\/b3logfile.com\/bing\/20201024.jpg",
        "name":"20201024.jpg"//带有扩展名的文件名，建议文件md5(尽量别重名，否则会给你发错哦！http-sdk会先检测文件在不在，如果不在才去url下载，再发送，否则直接发送)
    }
}
```





直接查看可爱猫的日志记录吧，条几条:

```json
2023-05-27 01:00:59.721 信息:收到main请求消息 | {"type":110,"param1":"wxid_rs2fy4y9i5rz22","param2":"1","param3":"0","param4":"filehelper","param5":"文件传输助手","param6":"5","param7":"1797651012","param8":"{\"content\":\"5\",\"final_from_name\":\"Lemon_guess\",\"final_from_wxid\":\"wxid_rs2fy4y9i5rz22\",\"from_name\":\"Lemon_guess\",\"from_wxid\":\"wxid_rs2fy4y9i5rz22\",\"msg_type\":1,\"msgid\":1797651012,\"original_content\":\"35\",\"send_out_type\":0,\"timestamp\":1685120459,\"to_name\":\"文件传输助手\",\"to_wxid\":\"filehelper\"}","param9":"","param10":"","param11":"","param12":""} 返回结果: 0


2023-05-27 00:38:51.700 信息:收到main请求消息 | {"type":100,"param1":"wxid_rs2fy4y9i5rz22","param2":"1","param3":"47519349567@chatroom","param4":"AST入门与实战交流①群","param5":"wxid_sh643f0j9j4u22","param6":"呵呵呵呵","param7":"wxid_rs2fy4y9i5rz22","param8":"Lemon_guess","param9":"四个行政许可都是八竿子打不着的许可","param10":"1797650980","param11":"{\"content\":\"四个行政许可都是八竿子打不着的许可\",\"final_from_name\":\"呵呵呵呵\",\"final_from_wxid\":\"wxid_sh643f0j9j4u22\",\"from_name\":\"AST入门与实战交流①群\",\"from_wxid\":\"47519349567@chatroom\",\"msg_type\":1,\"msgid\":1797650980,\"original_content\":\"E59B9BE4B8AAE8A18CE694BFE8AEB8E58FAFE983BDE698AFE585ABE7ABBFE5AD90E68993E4B88DE79D80E79A84E8AEB8E58FAF\",\"send_out_type\":-1,\"timestamp\":1685119129,\"to_name\":\"Lemon_guess\",\"to_wxid\":\"wxid_rs2fy4y9i5rz22\"}","param12":""} 返回结果: 0
```

接收时的body:

```json
{
    "event":"EventSendOutMsg",
    "robot_wxid":"wxid_rs2fy4y9i5rz22",
    "robot_name":"",
    "type":1,
    "from_wxid":"wxid_rs2fy4y9i5rz22",
    "from_name":"",
    "final_from_wxid":"wxid_rs2fy4y9i5rz22",
    "final_from_name":"",
    "to_wxid":"filehelper",
    "msgid":"1797651020",
    "msg":"测试数据"
}
```



发送时django也被停住了：

```
{'event': 'EventSendOutMsg', 'robot_wxid': 'wxid_rs2fy4y9i5rz22', 'robot_name': '', 'type': 1, 'from_wxid': 'wxid_rs2fy4y9i5rz22', 'from_name': '', 'final_from_wxid': 'wxid_rs2fy4y9i5rz22', 'final_from_name': '', 'to_wxid': 'filehelper', 'msgid': '121852897', 'msg': '我的'}
```

可爱猫的日志：

```
{"type":110,"param1":"wxid_rs2fy4y9i5rz22","param2":"1","param3":"1","param4":"filehelper","param5":"文件传输助手","param6":"我的","param7":"121852897","param8":"{\"content\":\"我的\",\"final_from_name\":\"Lemon_guess\",\"final_from_wxid\":\"wxid_rs2fy4y9i5rz22\",\"from_name\":\"Lemon_guess\",\"from_wxid\":\"wxid_rs2fy4y9i5rz22\",\"msg_type\":1,\"msgid\":121852897,\"original_content\":\"E68891E79A84\",\"send_out_type\":1,\"timestamp\":1685121852,\"to_name\":\"文件传输助手\",\"to_wxid\":\"filehelper\"}","param9":"","param10":"","param11":"","param12":""}
```

同理，我应该返回：

```json
{
    "success":true,//true时，http-sdk才处理，false直接丢弃
    "message":"successful!",
    "event":"SendImageMsg",//告诉它干什么，SendImageMsg是发送图片事件
    "robot_wxid":"wxid_rs2fy4y9i5rz22",//用哪个机器人发
    "to_wxid":"wxid_rs2fy4y9i5rz22",//发到哪里？群/好友
    "member_wxid":"",
    "member_name":"",
    "group_wxid":"",
    "msg":{//消息内容:发送 图片、视频、文件、动态表情都是这个结构
        "url":"https:\/\/b3logfile.com\/bing\/20201024.jpg",
        "name":"20201024.jpg"//带有扩展名的文件名，建议文件md5(尽量别重名，否则会给你发错哦！http-sdk会先检测文件在不在，如果不在才去url下载，再发送，否则直接发送)
    }
}

{
    "success":true,
    "message":"successful!",
    "event":"SendImageMsg",
    "robot_wxid":"wxid_rs2fy4y9i5rz22",
    "to_wxid":"wxid_rs2fy4y9i5rz22",
    "member_wxid":"",
    "member_name":"",
    "group_wxid":"",
    "msg":{
        "url":"https:\/\/b3logfile.com\/bing\/20201024.jpg",
        "name":"20201024.jpg"
    }
}
```

![image-20230527035510560](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230527035510560.png)

![image-20230527035528704](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230527035528704.png)
