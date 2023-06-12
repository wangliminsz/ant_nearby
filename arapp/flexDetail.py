# import os
# import time

import random

from arapp.models import *

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

def theLocation(locName, locAddress, locLat, locLng):

    lmessage = LocationSendMessage(title= locName, address = locAddress, latitude = locLat, longitude = locLng)

    return lmessage

def theLocImage(imgUrl):

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []


    bubble = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": imgUrl,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": imgUrl
            }
        }
    }

    bubbles.append(bubble)

    contents['contents'] = bubbles

    cmessage = FlexSendMessage(
        alt_text='Nearby Detail', contents=contents)
    return cmessage
