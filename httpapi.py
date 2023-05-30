import json
import time
import aiohttp

url = 'http://127.0.0.1:8073/send'
async def send_msg_private(msg, to_wxid):
    data = {
        "type": "100",
        "msg": msg,
        "to_wxid": to_wxid,
        "robot_wxid":"wxid_xxxxx"
    }
    data = json.dumps(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            print(await resp.text())

async def send_msg_group(msg, to_wxid):
    data = {
        "type": "100",
        "msg": msg,
        "to_wxid": to_wxid,
        "robot_wxid":"wxid_xxxxx"
    }
    data = json.dumps(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            print(await resp.text())

async def send_image_msg(picpath, to_wxid):
    data = {
        "type": "106",
        "msg": picpath,
        "to_wxid": to_wxid,
        "robot_wxid":"wxid_xxxxx"
    }
    data = json.dumps(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            print(await resp.text())
