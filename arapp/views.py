from ast import Pass
from arapp.flexContact import flex_Ad, flex_Contact
from arapp.flexDetail import theLocImage, theLocation
from arapp.models import *
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
# from linebot.models import MessageEvent, TextSendMessage,
from linebot.models import *

from arapp.list_all_project import *
from arapp.locationData import *
from arapp.flexLocation import *
from arapp.flexRadius import *
from arapp.flexProject import *

from arapp.flexInputKword import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # 先設定一個要回傳的message空集合
        message = []
        my_str = ''
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        # body = request.body.decode('utf-8')
        # body = request.body.decode('latin-1')

        sysText = ["Let's explore...", "About Nearby","About Ant Nearby", "Thanks", "Find facilities nearby", "Keyword confirmed", "Keyword cancelled", "15km or Above", "Radius 10km", "Radius 5km", "Radius 2km", "Radius 1km", "Radius not specified", "Please choose a type:"]

        #在這裡將body寫入機器人回傳的訊息中，可以更容易看出你收到的webhook長怎樣#
        # message.append(TextSendMessage(text=str(body)))

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            # 如果事件為訊息
            if isinstance(event, MessageEvent):

               if event.message.type == 'text':
                    mtext = event.message.text
                    mSource = event.source.user_id

                    if ("Let's explore..." in mtext) or ('Start to find facilities nearby' in mtext):
                        # alt_text='Buttons template',
                        # message = TemplateSendMessage(
                        #     alt_text='Find Nearby',
                        #     template=ButtonsTemplate(
                        #         title='Menu',
                        #         text='Find facilities nearby',
                        #         actions=[
                        #             PostbackTemplateAction(
                        #                 label='by Keyword',
                        #                 text='Keyword example:\r\n\n#chinese\r\n#pizza\r\n#hotpot\r\n\nNote:\r\n\n1.Add # before keyword\r\n\n2.Maxium 3 keywords',
                        #                 data='KKKKWWWW&' + mSource
                        #             ),
                        #             PostbackTemplateAction(
                        #                 label='by Keyword and Type',
                        #                 text='Keyword example:\r\n\n#chinese\r\n#pizza\r\n#hotpot\r\n\nNote:\r\n\n1.Add # before keyword\r\n\n2.Maxium 3 keywords',
                        #                 data='KWKWTYPE&' + mSource
                        #             ),
                        #             PostbackTemplateAction(
                        #                 label='List All Types',
                        #                 text='List all types ...',
                        #                 data='LISTTYPE&' + mSource
                        #             )
                        #         ]
                        #     )
                        # )

                        message = theFlexList()
                        line_bot_api.reply_message(event.reply_token, message)
                    elif 'deldb' in mtext:
                        # deletedb1290!@()
                        # alt_text='Buttons template',
                        mbkkaround.objects.all().delete()
                        print("delete DB")
               ### ---------------------------------------------

               elif event.message.type == 'location':

                    theUser = event.source.user_id

                    (myLocs, myLocs_Num) = locationData(theUser, event.message.latitude, event.message.longitude)
                    # locationData(theUser, event.message.latitude, event.message.longitude)

                    #print('locations --------------------------------')
                    #print(myLocs)
                    #print(myLocs_Num)
                    #print('locations --------------------------------')
                    ltext = "Nearby Facilities"
                    message1 = TextSendMessage(text=ltext)

                    if (myLocs_Num > 0):
                        message2 = flex_Locs(myLocs, myLocs_Num, theUser)
                    else:
                        print(myLocs_Num)
                        print('why no found --------------------------')
                        message2 = TextSendMessage(text="Not Found")

                    message3 = flex_Contact()

                    # message.append(message1)
                    # message.append(message2)

                    # line_bot_api.reply_message(
                    #     event.reply_token, [message1])

                    line_bot_api.reply_message(
                        event.reply_token, [message1, message2, message3])

               ### ---------------------------------------------

            elif isinstance(event, PostbackEvent):

                # mbmethod = models.IntegerField(default=0) # 1- keyword 2- keyword&type 3- listtype

                if "FLEXLOCA&"  in event.postback.data:

                    theUserId = event.source.user_id
                    theDetailIndex = int(event.postback.data[9:])
                    print(theDetailIndex)
                    print("detail ------------------")

                    theDetail = mbkkdetail.objects.filter(dtuserid=theUserId).filter(dtlocid=theDetailIndex).last()

                    print(theDetail.dtlocname)
                    print(theDetail.dtloclat)
                    print(theDetail.dtloclng)
                    print(theDetail.dtlocrating)
                    print(theDetail.dtlocphotourl)
                    print("detail ------------------")

                    # message1 = TextSendMessage(text='More info...')
                    # message2 = theLocation(event.postback.data)
                    # message3 = theFlex(event.postback.data)
                    # message4 = flex_Ad()

                    # line_bot_api.reply_message(
                    #     event.reply_token, [message1, message2, message3,message4])

                    if theDetail:

                        # theFlex()
                        contact_message = flex_Ad(theDetail.dtlocname)

                        # dtlocAddress = "Address"
                        dtlocAddress = theDetail.dtlocdistance

                        if len(theDetail.dtlocname) > 90:
                            theLocName = theDetail.dtlocname[:90]
                        else:
                            theLocName = theDetail.dtlocname

                        location_message = theLocation(theLocName, dtlocAddress, theDetail.dtloclat, theDetail.dtloclng)

                        # detail_message = flex_Detail()

                        ## Flex Image Message
                        if "imgur" not in theDetail.dtlocphotourl:
                            img_message = theLocImage(theDetail.dtlocphotourl)
                            line_bot_api.reply_message(event.reply_token, [location_message, img_message, contact_message])
                        else:
                            line_bot_api.reply_message(event.reply_token, [location_message, contact_message])

                        # ## Image MessageMessage
                        # if "imgur" not in theDetail.dtlocphotourl:
                        #     img_message = ImageSendMessage(original_content_url=theDetail.dtlocphotourl,preview_image_url=theDetail.dtlocphotourl)
                        #     line_bot_api.reply_message(event.reply_token, [location_message, img_message, contact_message])
                        # else:
                        #     line_bot_api.reply_message(event.reply_token, [location_message, contact_message])

                    # dtuserid
                    # dtlocid
                    # dtlocname
                    # dtloclat
                    # dtloclng
                    # dtlocrating
                    ### dtlocaddress
                    # dtlocphotourl
                    # if thisUserId.exists():
                    #     mbkkaround.objects.filter(mbuserid=thisUser).update(mbmethod=1)
                    # else:
                    #     mbkkaround.objects.create(mbuserid=thisUser, mbmethod=1)

                if "mcontact&" in event.postback.data:

                    # theFlex()
                    contact_message_flex = flex_Contact()

                    # ltext = "About Nearby"
                    # input_message_text = TextSendMessage(text=ltext)

                    line_bot_api.reply_message(event.reply_token, contact_message_flex)

                if "KKKKWWWW&" in event.postback.data:
                    print("hello keyword")

                    mSource = event.source.user_id
                    thisUser = mSource

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        mbkkaround.objects.filter(mbuserid=thisUser).update(mbmethod=1)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbmethod=1)

                    # theFlex()
                    input_message_flex = flex_Input()

                    ltext = "Please input your #keyword:"
                    input_message_text = TextSendMessage(text=ltext)

                    # line_bot_api.unlink_rich_menu_from_user(thisUser)
                    # line_bot_api.link_rich_menu_to_user(thisUser, "richmenu-e05687aa18f766f3fb551a29cafecbf4")

                    line_bot_api.reply_message(event.reply_token, [input_message_flex,input_message_text])

                elif "KWKWTYPE&" in event.postback.data:
                    print("hello keyword & type")

                    mSource = event.source.user_id
                    thisUser = mSource

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        mbkkaround.objects.filter(mbuserid=thisUser).update(mbmethod=2)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbmethod=2)


                    # list_message = theFlexList()
                    # theFlex()
                    input_message_flex = flex_Input()

                    ltext = "Please input your #keyword:"
                    input_message_text = TextSendMessage(text=ltext)

                    line_bot_api.reply_message(event.reply_token, [input_message_flex,input_message_text])

                elif "LISTTYPE&" in event.postback.data:

                    print("hello list type")

                    mSource = event.source.user_id
                    thisUser = mSource

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        mbkkaround.objects.filter(mbuserid=thisUser).update(mbmethod=3)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbmethod=3)

                    # theFlexList()
                    list_message = theFlexList()
                    line_bot_api.reply_message(event.reply_token, list_message)

                elif "RRRRDDDD&" in event.postback.data:
                    print('radius Confirmed')

                    #-----------------

                    # distance 1km 2km 5km 10km 50km

                    thisData = event.postback.data.split("&")
                    thisRadius = thisData[2]

                    if thisRadius == 'distance':
                        dbRadius = 0
                    elif thisRadius == '1km':
                        dbRadius = 1500
                    elif thisRadius == '2km':
                        dbRadius = 2500
                    elif thisRadius == '5km':
                        dbRadius = 6500
                    elif thisRadius == '10km':
                        dbRadius = 12500
                    elif thisRadius == '50km':
                        dbRadius = 50000

                    #-----------------

                    mSource = event.source.user_id
                    thisUser = mSource

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        mbkkaround.objects.filter(mbuserid=thisUser).update(mbradius=dbRadius)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbradius=dbRadius)

                    #-----------------

                    userInfo = thisUserId.last()
                    print(userInfo.mbmethod)
                    print('userInfo method -------------------')

                    if userInfo.mbmethod == 1 or userInfo.mbmethod == 3 :

                        message = TemplateSendMessage(
                            alt_text='Send your location?',
                            template=ConfirmTemplate(
                                text="Send your location?",
                                actions=[
                                    URITemplateAction(
                                        type='uri',
                                        label='Yes',
                                        uri='https://line.me/R/nv/location'
                                    ),
                                    PostbackTemplateAction(
                                        label="No",
                                        text="Thanks",
                                        data="No Location"
                                    )
                                ]
                            )
                        )

                        line_bot_api.reply_message(
                            event.reply_token, message)

                    elif userInfo.mbmethod == 2:

                        ltext = "Please choose a type:"
                        text_message = TextSendMessage(text=ltext)

                        # theFlexList()
                        list_message = theFlexList()
                        line_bot_api.reply_message(event.reply_token, [text_message, list_message])

                    #-----------------

                elif "KCONFIRM&" in event.postback.data:
                    print('keyword Confirmed')
                    # print(event.postback.data)

                    thisData = event.postback.data.split("&")
                    # thisUser = thisData[1]
                    thisKeyword = thisData[1]

                    print(thisKeyword)

                    print('keyword DB------------------------------------------')

                    # mSource = event.source.user_id
                    # thisUser = mSource
                    # thisType = event.postback.data[9:]

                    # thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    # if thisUserId.exists():
                    #     mbkkaround.objects.filter(mbuserid=thisUser).update(mbtype=thisType)
                    # else:
                    #     mbkkaround.objects.create(mbuserid=thisUser, mbtype=thisType)

                    mSource = event.source.user_id
                    thisUser = mSource

                    # userInfo = mbkkaround.objects.filter(mbuserid=thisUser).last()

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        if thisUserId.last().mbmethod != 2:
                            mbkkaround.objects.filter(mbuserid=thisUser).update(mbkword=thisKeyword, mbmethod=1)
                        else:
                            mbkkaround.objects.filter(mbuserid=thisUser).update(mbkword=thisKeyword)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbmethod=1,mbkword=thisKeyword)

                    # -----------------

                    message = flex_Radius(thisUser)

                    line_bot_api.reply_message(
                        event.reply_token, message)

                    # -----------------

                elif "TYPETYPE&" in event.postback.data:

                    mSource = event.source.user_id

                    thisUser = mSource
                    thisType = event.postback.data[9:]

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        if thisUserId.last().mbmethod == 1:
                            mbkkaround.objects.filter(mbuserid=thisUser).update(mbtype=thisType, mbmethod=3)
                        else:
                            mbkkaround.objects.filter(mbuserid=thisUser).update(mbtype=thisType)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbtype=thisType)

                    # -----------------

                    userInfo = mbkkaround.objects.filter(mbuserid = thisUser).last()

                    # -----------------

                    if userInfo.mbmethod == 3:
                        message = flex_Radius(thisUser)

                        line_bot_api.reply_message(
                            event.reply_token, message)

                    elif userInfo.mbmethod == 2:
                        print("haha Deadlock -----------------------------")

                        message = TemplateSendMessage(
                            alt_text='Send your location?',
                            template=ConfirmTemplate(
                                text="Send your location?",
                                actions=[
                                    URITemplateAction(
                                        type='uri',
                                        label='Yes',
                                        uri='https://line.me/R/nv/location'
                                    ),
                                    PostbackTemplateAction(
                                        label="No",
                                        text="Thanks",
                                        data="No Location"
                                    )
                                ]
                            )
                        )

                        line_bot_api.reply_message(
                            event.reply_token, message)

                elif "PROJPROJ&" in event.postback.data:

                    mSource = event.source.user_id
                    thisUser = mSource

                    print('Event Project Data &------>', event.postback.data)
                    thisType = event.postback.data[9:]
                    my_list = thisType.split("$")

                    # mbradius=dbRadius
                    dbRadius = 3000
                    dbKeyword = "helloAnt"
                    dbKeyword1 = "Shopping Mall | Mall | Shopping | Cinema"
                    dbKeyword2 = "Restaurant | Buffet | Steak | Hotpot | Michelin"
                    dbKeyword3 = "School | University | College | Student"
                    dbKeyword4 = "Park | Leisure | Resort | Club | Massage"
                    dbKeyword5 = "BTS | MRT | Subway | Hospital | Clinic"

                    thisUserId = mbkkaround.objects.filter(mbuserid = thisUser)
                    if thisUserId.exists():
                        mbkkaround.objects.filter(mbuserid=thisUser).update(mbtype=my_list[0], mb_plat=my_list[1], mb_plng=my_list[2], mbradius=dbRadius, mbkword=dbKeyword)
                    else:
                        mbkkaround.objects.create(mbuserid=thisUser, mbtype=my_list[0], mb_plat=my_list[1], mb_plng=my_list[2], mbradius=dbRadius, mbkword=dbKeyword)

                    # -----------------

                    # userInfo = mbkkaround.objects.filter(mbuserid = thisUser).last()

                    if thisUserId.exists():
                        mbkkdetail.objects.filter(dtuserid=thisUserId).delete()

                    # -----------------

                    (myLocs1, myLocs_Num1) = locationData_Ant(thisUser, my_list[1], my_list[2], dbKeyword1, dbRadius)
                    # locationData(theUser, event.message.latitude, event.message.longitude)

                    # ltext = "Nearby Facilities"
                    # message1 = TextSendMessage(text=ltext)

                    if (myLocs_Num1 > 0):
                        dtIdx = 1
                        message1= flex_Locs(myLocs1, myLocs_Num1, thisUser, dtIdx)
                    else:
                        print(myLocs_Num1)
                        print('why no found --------------------------')
                        message1 = TextSendMessage(text="Shopping Mall Not Found")

                    # message3 = flex_Contact()

                    ##################################################

                    (myLocs2, myLocs_Num2) = locationData_Ant(thisUser, my_list[1], my_list[2], dbKeyword2, dbRadius)

                    if (myLocs_Num2 > 0):
                        dtIdx = 2
                        message2= flex_Locs(myLocs2, myLocs_Num2, thisUser, dtIdx)
                    else:
                        print(myLocs_Num2)
                        print('why no found --------------------------')
                        message2 = TextSendMessage(text="Restaurant Not Found")

                    ##################################################

                    (myLocs3, myLocs_Num3) = locationData_Ant(thisUser, my_list[1], my_list[2], dbKeyword3, dbRadius)

                    if (myLocs_Num3 > 0):
                        dtIdx = 3
                        message3= flex_Locs(myLocs3, myLocs_Num3, thisUser, dtIdx)
                    else:
                        print(myLocs_Num3)
                        print('why no found --------------------------')
                        message3 = TextSendMessage(text="School Not Found")

                    ##################################################

                    (myLocs4, myLocs_Num4) = locationData_Ant(thisUser, my_list[1], my_list[2], dbKeyword4, dbRadius)

                    if (myLocs_Num4 > 0):
                        dtIdx = 4
                        message4= flex_Locs(myLocs4, myLocs_Num4, thisUser, dtIdx)
                    else:
                        print(myLocs_Num4)
                        print('why no found --------------------------')
                        message4 = TextSendMessage(text="Club Not Found")

                    ##################################################

                    (myLocs5, myLocs_Num5) = locationData_Ant(thisUser, my_list[1], my_list[2], dbKeyword5, dbRadius)

                    if (myLocs_Num5 > 0):
                        dtIdx = 5
                        message5= flex_Locs(myLocs5, myLocs_Num5, thisUser, dtIdx)
                    else:
                        print(myLocs_Num5)
                        print('why no found --------------------------')
                        message5 = TextSendMessage(text="Comm or Hospital Not Found")

                    ##################################################

                    ##################################################

                    line_bot_api.reply_message(
                        event.reply_token, [message1, message2, message3, message4, message5])

                    # -----------------

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
