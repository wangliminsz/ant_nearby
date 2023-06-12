# import os
# import time

import random

from arapp.models import *

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

def flex_Locs(myLocList, myLocNum, lineUserId):

    # print(myLocList)
    # print('flex_Locs -----------------------------------')

    # print(lineUserId)
    # print('Line User Id -----------------------------------')

    if myLocNum >= 12:
        bubbleNum = 12
    else:
        bubbleNum = myLocNum

    # mbkkdetail.objects.all().delete()

    thisUser = mbkkdetail.objects.filter(dtuserid = lineUserId)

    if thisUser.exists():
        mbkkdetail.objects.filter(dtuserid=lineUserId).delete()

    dtIndex = 0

    for myLocitem in myLocList[:bubbleNum]:

        dtname = myLocitem['locName']
        dtlat = myLocitem['locLat']
        dtlng = myLocitem['locLng']

        if myLocitem['locRating']:
            dtrating = myLocitem['locRating']
            # print(theRating)
            # print('rating -- maybe error --------------')
        else:
            dtrating = 0

        if myLocitem["locDistanceStr"]:
            dtdistancestr = myLocitem["locDistanceStr"]

        # if myLocitem['locAddress']:
        #     dtaddress = myLocitem['locAddress']
        #     # print(theRating)
        #     # print('rating -- maybe error --------------')
        # else:
        #     dtaddress = ''

        # dtaddress = ''
        # array 里面确实没有，那暂时不用了

        if myLocitem['locPhotoUrl']:
            imgUrl = myLocitem['locPhotoUrl']
        else:
            randomNum = random.randint(0,100)
            if randomNum > 90:
                #imgUrl = "https://i.imgur.com/NHVE7qa.jpg"
                imgUrl = "https://i.imgur.com/3ABmSBt.jpg"
            elif randomNum > 80:
                #imgUrl = "https://i.imgur.com/V6TwRMv.jpg"
                imgUrl = "https://i.imgur.com/QoS95HW.jpg"
            elif randomNum > 70:
                imgUrl = "https://i.imgur.com/Cx32BBl.jpg"
            elif randomNum > 60:
                imgUrl = "https://i.imgur.com/T5Rs4UX.jpg"
            elif randomNum > 50:
                imgUrl = "https://i.imgur.com/ARTvTE8.jpg"
            elif randomNum > 40:
                imgUrl = "https://i.imgur.com/zM8qsLO.png"
            elif randomNum > 30:
                imgUrl = "https://i.imgur.com/ldBQuR1.jpg"
                # imgUrl = "https://i.imgur.com/nI56zhG.jpg"
            elif randomNum > 20:
                # imgUrl = "https://i.imgur.com/zWSmDnS.jpg"
                imgUrl = "https://i.imgur.com/wUlVkxZ.jpg"
            elif randomNum > 10:
                # imgUrl = "https://i.imgur.com/5sF6eSn.jpg"
                imgUrl = "https://i.imgur.com/FbzRG5X.jpg"
            else:
                # imgUrl = "https://i.imgur.com/WgJ8KsO.jpg"
                imgUrl = "https://i.imgur.com/ZeKhTDb.jpg"

        mbkkdetail.objects.create(dtuserid=lineUserId, dtlocid=dtIndex, dtlocname=dtname, dtloclat=dtlat, dtloclng=dtlng, dtlocrating=dtrating, dtlocphotourl=imgUrl, dtlocdistance=dtdistancestr)

        dtIndex = dtIndex + 1

        # dtuserid
        # dtlocid
        # dtlocname
        # dtloclat
        # dtloclng
        # dtlocrating
        ### dtlocaddress
        # dtlocphotourl

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    myIndex = 0

    for myLocitem in myLocList[:bubbleNum]:

        # myIdx = enumerate(myLocList)
        # print(myIdx)

        theName = myLocitem['locName']
        if myLocitem['locPhotoUrl']:
            imgUrl = myLocitem['locPhotoUrl']
        else:
            randomNum = random.randint(0,100)
            if randomNum > 90:
                #imgUrl = "https://i.imgur.com/NHVE7qa.jpg"
                imgUrl = "https://i.imgur.com/3ABmSBt.jpg"
            elif randomNum > 80:
                #imgUrl = "https://i.imgur.com/V6TwRMv.jpg"
                imgUrl = "https://i.imgur.com/QoS95HW.jpg"
            elif randomNum > 70:
                imgUrl = "https://i.imgur.com/Cx32BBl.jpg"
            elif randomNum > 60:
                imgUrl = "https://i.imgur.com/T5Rs4UX.jpg"
            elif randomNum > 50:
                imgUrl = "https://i.imgur.com/ARTvTE8.jpg"
            elif randomNum > 40:
                imgUrl = "https://i.imgur.com/zM8qsLO.png"
            elif randomNum > 30:
                imgUrl = "https://i.imgur.com/ldBQuR1.jpg"
                # imgUrl = "https://i.imgur.com/nI56zhG.jpg"
            elif randomNum > 20:
                # imgUrl = "https://i.imgur.com/zWSmDnS.jpg"
                imgUrl = "https://i.imgur.com/wUlVkxZ.jpg"
            elif randomNum > 10:
                # imgUrl = "https://i.imgur.com/5sF6eSn.jpg"
                imgUrl = "https://i.imgur.com/FbzRG5X.jpg"
            else:
                # imgUrl = "https://i.imgur.com/WgJ8KsO.jpg"
                imgUrl = "https://i.imgur.com/ZeKhTDb.jpg"


        if myLocitem['locRating']:
            theRating = "Rating: " + str(myLocitem['locRating'])
            # print(theRating)
            # print('rating -- maybe error --------------')
        else:
            theRating = "No rating data"

        # theStyle = myLocitem['mbstyle']
        # theIndex = myLocitem['mbid']
        # theDistance = myLocitem['mbdistance']
        # theDistanceStr = str(round(139.276 * theDistance, 2)) + " km"

        theDistanceStr = myLocitem["locDistanceStr"]
        # print(theDistanceStr)
        # print('flex distance ------------------------------')

        # locId
        # locName
        # locLat
        # locLng
        # locRating
        # locAddress
        # locPhotoUrl

        bubble = {
            "type": "bubble",
            "size": "micro",
            "hero": {
                    "type": "image",
                    # "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
                    # "url":  "https://i.imgur.com/NHVE7qa.jpg",
                    "url":  imgUrl,
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213",
                    "action":{
                                "type": "postback",
                                "label": "More...",
                                "data": "FLEXLOCA&" + str(myIndex)
                    }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                        {
                            "type": "text",
                            "text": theName,
                            "weight": "bold",
                            "size": "sm",
                            "wrap": True
                        },
                    {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": theRating,
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "xs",
                                            "flex": 5
                                        },
                                        {
                                            "type": "text",
                                            "text": theDistanceStr,
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "xs",
                                            "flex": 5
                                        }
                                    ]
                                }
                            ]
                    }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "postback",
                                "label": "More...",
                                "data": "FLEXLOCA&" + str(myIndex)
                            }
                        }
                ],
                "flex": 0
            }
        }

        bubbles.append(bubble)

        myIndex = myIndex + 1

        # dtuserid
        # dtlocid
        # dtlocname
        # dtloclat
        # dtloclng
        # dtlocrating
        # dtlocaddress
        # dtlocphotourl

        # thisUser = event.source.user_id
        # # thisType = event.postback.data[9:]
        # thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)

        # if thisUserId.exists():
        #     mbkkaround.objects.filter(mbuserid=thisUser).update(mbkword=kWord)
        # else:
        #     mbkkaround.objects.create(mbuserid=thisUser, mbkword=kWord)

        # locId
        # locName
        # locLat
        # locLng
        # locRating
        # locAddress
        # locPhotoUrl

    contents['contents'] = bubbles

    fmessage = FlexSendMessage(
        alt_text='Nearby Facilities', contents=contents)
    return fmessage
