import requests
from config import *

# fetch data from homora API
def fetch_position(watch_list):
    positions = requests.get(HOMORA_AVAX_POSITIONS)
    apys = requests.get(HOMORA_APYS)
    apys = apys.json()
    positions = positions.json()
    positions = [position for position in positions if position["id"] in watch_list]
    for position in positions:
        position["apy"] = float(apys[position["pool"]["key"]]["tradingFeeAPY"])
    return positions


# send alert to discord web hook
def send_alert(data):
    data = {
        "content": "@everyone\n" + data,
        "embeds": None,
        "attachments": [],
    }
    requests.post(DISCORD_WEB_HOOK, data=data)
