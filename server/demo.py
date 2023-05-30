from CuteCat import CuteCat

bot = CuteCat(api_url='http://127.0.0.1:8090', robot_wxid='wxid_5hxa04j4z6pg22', access_token='')


@bot.on('EventFriendMsg')
def eventfrinendmsg(msg):
    print(msg)
    bot.SendTextMsg(to_wxid=msg.from_wxid, msg='hello')


bot.run()
