import flask,time,json
def getmsg():
    #取msg
    allmsg = flask.request.get_data()
    allmsg = json.loads(allmsg.decode('utf-8'))
    msg = allmsg.get('msg')
    from_name = allmsg.get('from_name')
    final_from_name = allmsg.get('final_from_name')
    time_str = allmsg.get('msgid')
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time_str)))
    from_wxid = allmsg.get('from_wxid')
    final_from_wxid = allmsg.get('final_from_wxid')
    msg_type = allmsg.get('type')
    robot_wxid = allmsg.get('robot_wxid')
    return msg,from_name,final_from_name,time_str,from_wxid,final_from_wxid,msg_type,robot_wxid
