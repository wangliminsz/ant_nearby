import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

def flex_Contact():
    # #print(mybkklist[0]['mbname'])
    # #print(mybkklist[0]['mbstyle'])
    # #print('inside flex ----------------------------------------')

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    # flexContact = {
    #     "type": "carousel",
    #     "contents": [
    bubble = {
    "type": "bubble",
    "size": "kilo",
            # "hero": {
            #     # "type": "image",
            #     # "size": "full",
            #     # "aspectRatio": "20:6",
            #     # "aspectMode": "cover",
            #     # "url": "https://i.imgur.com/UpbCLxZ.jpg"
            # },
    "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "lg",
                "contents": [
                    {
                        "type": "text",
                        "text": "Ant Global Property",
                        "wrap": True,
                        "weight": "bold",
                        "size": "lg",
                        "style": "normal"
                    },
                    # {
                    #     "type": "text",
                    #     "text": "Ant Global Property",
                    #     "size": "sm"
                    # },

                    {
                        "type": "text",
                        "text": "Thai Real Estate - Buy / Sale / Rent",
                        "wrap": True,
                        "size": "sm"
                    },

                    {
                        "type": "text",
                        "text": "Tel: 0909820001",
                        "size": "sm"
                    }
                ]
            },
    "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "uri",
                            "label": "Line ID",
                            "uri": "https://line.me/ti/p/kyOuQl8A2V"
                        },
                        "height": "sm"
                    }
                ]
            }
    }

    ###
    bubble = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/VvxVpDg.jpg",
                                "aspectMode": "cover",
                                "size": "full"
                            }
                        ],
                        "cornerRadius": "100px",
                        "width": "72px",
                        "height": "72px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "contents": [
                                    {
                                        "type": "span",
                                        "weight": "bold",
                                        "color": "#000000",
                                        "text": "เดซ Daisy"
                                    }
                                ],
                                "size": "md",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "Ant Global Property",
                                "size": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "Line ID",
                                    "uri": "https://line.me/ti/p/kyOuQl8A2V"
                                },
                                "style": "primary",
                                "height": "sm",
                                "margin": "10px"
                            }
                        ]
                    }
                ],
                "spacing": "xl",
                "paddingAll": "20px"
            }
        ],
        "paddingAll": "0px"
    }
}
    ###

    bubbles.append(bubble)

    contents['contents'] = bubbles

    cmessage = FlexSendMessage(
        alt_text='About Nearby', contents=contents)
    return cmessage

###


def flex_Ad(locName):
    # #print(mybkklist[0]['mbname'])
    # #print(mybkklist[0]['mbstyle'])
    # #print('inside flex ----------------------------------------')

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    # flexContact = {
    #     "type": "carousel",
    #     "contents": [
    bubble = {
    "type": "bubble",
    "size": "kilo",
            # "hero": {
            #     # "type": "image",
            #     # "size": "full",
            #     # "aspectRatio": "20:6",
            #     # "aspectMode": "cover",
            #     # "url": "https://i.imgur.com/UpbCLxZ.jpg"
            # },
    "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "lg",
                "contents": [
                    {
                        "type": "text",
                        "text": "Ant Global Property",
                        "wrap": True,
                        "weight": "bold",
                        "size": "lg",
                        "style": "normal"
                    },
                    # {
                    #     "type": "text",
                    #     "text": "Ant Global Property",
                    #     "size": "sm"
                    # },

                    {
                        "type": "text",
                        "text": "Thai Real Estate - Buy / Sale / Rent",
                        "wrap": True,
                        "size": "sm"
                    },

                    {
                        "type": "text",
                        "text": "Tel: 0909820001",
                        "size": "sm"
                    }
                ]
            },
    "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "uri",
                            "label": "Line ID",
                            "uri": "https://line.me/ti/p/kyOuQl8A2V"
                        },
                        "height": "sm"
                    }
                ]
            }
    }

    ###

    ###
    bubble = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/VvxVpDg.jpg",
                                "aspectMode": "cover",
                                "size": "full"
                            }
                        ],
                        "cornerRadius": "100px",
                        "width": "72px",
                        "height": "72px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "contents": [
                                    {
                                        "type": "span",
                                        "weight": "bold",
                                        "color": "#000000",
                                        "text": "เดซ Daisy"
                                    }
                                ],
                                "size": "md",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "Ant Global Property",
                                "size": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "Line ID",
                                    "uri": "https://line.me/ti/p/kyOuQl8A2V"
                                },
                                "style": "primary",
                                "height": "sm",
                                "margin": "10px"
                            }
                        ]
                    }
                ],
                "spacing": "xl",
                "paddingAll": "20px"
            }
        ],
        "paddingAll": "0px"
    }
}
    ###

    bubbles.append(bubble)

    contents['contents'] = bubbles

    cmessage = FlexSendMessage(
        alt_text=locName, contents=contents)
    return cmessage

###
###
