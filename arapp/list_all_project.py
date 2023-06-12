import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

from arapp.list_all_project_data import *
from arapp.list_air_data import *

def theFlexList():

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

    # print('items ----------->', len(projectlist))
    projectlist = air_deliver_data()
    pages = len(projectlist) // 12 # integer division to get whole number of pages

    if len(projectlist) % 12 != 0:
        pages += 1  # add an extra page for any remaining items

    # print('pages ----------->', pages)

    for externalIdx in range(pages):

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
            if exitMark >= len(projectlist):
                break

            projectName = projectlist[(externalIdx * range_Num + internalIdx)]['en']
            projectLat = projectlist[(externalIdx * range_Num + internalIdx)]['p_lat']
            projectLng = projectlist[(externalIdx * range_Num + internalIdx)]['p_lng']
            # + " " + projectlist[(externalIdx * range_Num + internalIdx)]['cn']

            myKernal = dict()
            myKernal['type'] = 'button'
            myKernal_action = {
                "type": "postback",
                "label": projectName,
                "data": "PROJPROJ&" + projectName + "$" + projectLat + "$" + projectLng,
                # "data": "PROJPROJ&" + projectlist[(externalIdx * range_Num + internalIdx)]['en'],
                #  "label":  "my Label",
                #  "data": "my Data",
                "displayText": projectName
            }
            myKernal['action'] = myKernal_action
            myKernal['height'] = 'sm'
            mybubble_body_contents.append(myKernal)

        mybubble_body['contents'] = mybubble_body_contents
        mybubble['body'] = mybubble_body
        mybubble['styles'] = mybubble_styles

        mybubbles.append(mybubble)

    contents['contents'] = mybubbles

    lmessage = FlexSendMessage(alt_text='Project List', contents=contents)
    # print(lmessage)
    return lmessage

# theFlexList()

# ---------------------------------------------
