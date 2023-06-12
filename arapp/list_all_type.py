import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

from arapp.list_all_type_data import *

def theFlexList():

    # mybkklist = mdata
    # mybkklist = sorted(mdata, key=lambda x: x['mbname'], reverse=False)

    # -----------------------------------------------

    mybubble_sample = {
        "type": "bubble",
        "size": "micro",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello",
                        "displayText": "wanglimin"
                    }
                }
            ]
        },
        "styles": {
            "footer": {
                "separator": False
            }
        }
    }

    # ---------------------------------------------

    # for mybkk in mybkklist:

    contents = dict()
    contents['type'] = 'carousel'

    mybubbles = []

    for externalIdx in range(8):

        mybubble = dict()

        mybubble['type'] = 'bubble'
        mybubble['size'] = 'kilo'

        # ------------------

        mybubble_styles_footer = dict()
        mybubble_styles_footer['separator'] = False
        mybubble_styles = dict()
        mybubble_styles['footer'] = mybubble_styles_footer

        # ------------------

        mybubble_body = dict()
        mybubble_body['type'] = 'box'
        mybubble_body['layout'] = 'vertical'

        # ------------------

        mybubble_body_contents = []

        range_Num  = 12

        for internalIdx in range(range_Num):

            exitMark = (externalIdx * range_Num + internalIdx)
            if exitMark >= 94:
                break

            typeName = typelist[(externalIdx * range_Num + internalIdx)]['en'] + " " + typelist[(externalIdx * range_Num + internalIdx)]['cn']

            myKernal = dict()
            myKernal['type'] = 'button'
            myKernal_action = {
                "type": "postback",
                "label": typeName,
                "data": "TYPETYPE&" + typelist[(externalIdx * range_Num + internalIdx)]['en'],
                #  "label":  "my Label",
                #  "data": "my Data",
                "displayText": typeName
            }
            myKernal['action'] = myKernal_action
            myKernal['height'] = 'sm'
            mybubble_body_contents.append(myKernal)

        mybubble_body['contents'] = mybubble_body_contents
        mybubble['body'] = mybubble_body
        mybubble['styles'] = mybubble_styles

        mybubbles.append(mybubble)

    contents['contents'] = mybubbles

    lmessage = FlexSendMessage(alt_text='List All Types', contents=contents)
    return lmessage

# ---------------------------------------------
