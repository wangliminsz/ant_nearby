# import os
# import time

import random

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

def flex_Input():

    kWordFlex = {

    "type": "bubble",
    "size": "kilo",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "Input #keyword",
                "color": "#ffffff",
                "size": "xl",
                "flex": 4,
                "weight": "bold"
            },
            ]
        }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#0367D3",
        "spacing": "md",
        "height": "75px",
        "paddingTop": "22px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "✓",
                "size": "sm",
                "gravity": "center", "flex": 1,
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "cornerRadius": "30px",
                    "height": "12px",
                    "width": "12px",
                    "borderColor": "#EF454D",
                    "borderWidth": "2px"
                },
                {
                    "type": "filler"
                }
                ],
                "flex": 1
            },
            {
                "type": "text",
                "text": "Input #keyword",
                "gravity": "center", "flex": 1,
                "flex": 12,
                "size": "sm"
            }
            ],
            "spacing": "lg",
            "cornerRadius": "30px",
            "margin": "xl"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 1
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "filler"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "width": "2px",
                        "backgroundColor": "#B7B7B7"
                    },
                    {
                        "type": "filler"
                    }
                    ],
                    "flex": 1
                }
                ],
                "width": "12px"
            },
            {
                "type": "text",
                "text": "Add # before keyword",
                "gravity": "center",
                "flex": 12,
                "size": "xs",
                "color": "#8c8c8c"
            }
            ],
            "spacing": "lg",
            "height": "64px"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "✓",
                    "gravity": "center", "flex": 1,
                    "size": "sm"
                }
                ],
                "flex": 1
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "cornerRadius": "30px",
                    "width": "12px",
                    "height": "12px",
                    "borderWidth": "2px",
                    "borderColor": "#6486E3"
                },
                {
                    "type": "filler"
                }
                ],
                "flex": 1
            },
            {
                "type": "text",
                "text": "Processing...",
                "gravity": "center", "flex": 1,
                "flex": 12,
                "size": "sm"
            }
            ],
            "spacing": "lg",
            "cornerRadius": "30px"
        }
        ]
    }
    }

    ####

    fmessage = FlexSendMessage(
            alt_text='Please input your #keyword', contents=kWordFlex)
    return fmessage


