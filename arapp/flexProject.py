# import os
# import time

import random

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

# =======================

# def flex_Project(thisUser):

#     print("hello flex Project-----------------------")

#     # Define the place name, latitude, and longitude
#     place_name = "Central World"
#     latitude = 13.746711
#     longitude = 100.539074

#     # Create a BubbleContainer with a LocationComponent
#     bubble = BubbleContainer(
#         body=BoxComponent(
#             layout="vertical",
#             contents=[
#                 TextComponent(text=place_name, weight="bold", size="xl"),
#                 LocationComponent(
#                     title=place_name,
#                     address="",
#                     latitude=latitude,
#                     longitude=longitude,
#                     size="full",
#                     aspect_ratio="16:9",
#                     margin="md"
#                 )
#             ]
#         )
#     )

#     # Create a FlexSendMessage with the BubbleContainer
#     flex_message = FlexSendMessage(alt_text=place_name, contents=bubble)
#     return flex_message

####