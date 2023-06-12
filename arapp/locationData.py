import requests
import random

from arapp.models import mbkkaround

def locationData_Ant(locUser, latP, lngP, dbKeyword, dbRadius):

    userInfo = mbkkaround.objects.filter(mbuserid=locUser).last()
    lat = float(latP)
    lng = float(lngP)

#     2022-02-20 ---------------------
#     kWordList = ["airport" , "aquarium" , "bowling_alley" , "casino" , "cemetery" , "courthouse" , "funeral_home" , "light_rail_station" , "painter" , "synagogue" , "taxi_stand" , "zoo"]
#     2022-02-20 ---------------------

    GOOGLE_API_KEY = "AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg"
    print('inside loc function 3000------------>', dbRadius)
    finalRadius = userInfo.mbradius

    resultList = []

    if userInfo.mbradius == 0:

        if userInfo.mbmethod == 1:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
                # print('url keyword-----------------')
                # print(gmap_Example)

        if userInfo.mbmethod == 2:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
                print('url keyword type-----------------')
                print(gmap_Example)

        if userInfo.mbmethod == 3:
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)

    else:
        # kWord = userInfo.mbkword
        gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + dbKeyword + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
        # print('radius keyword-----------------')
        # print(gmap_Example)

        # if userInfo.mbmethod == 3:
        # gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
        # print('radius keyword-----------------')
        # print(gmap_Example)

    destSearch = gmap_Example

    destReq = requests.get(destSearch)
    nearby_Facility_dict = destReq.json()
    nearby_Facility_20 = nearby_Facility_dict ["results"]
    result_Num = len(nearby_Facility_20)


    for i in range(result_Num):

        # resultDict = {"locId": 0, "locName": "", "locLat": 0, "locLng": 0, "locRating": None, "locAddress": None,  "locPhotoUrl": None}
        resultDict = {}

        if nearby_Facility_20[i]:

            resultDict["locId"] = i
            resultDict["locName"] = nearby_Facility_20[i]["name"]
            resultDict["locLat"] = nearby_Facility_20[i]["geometry"]["location"]["lat"]
            resultDict["locLng"] = nearby_Facility_20[i]["geometry"]["location"]["lng"]

            # Cal Distance -------------------------------------------------------------------------

            latL = nearby_Facility_20[i]["geometry"]["location"]["lat"]
            lngL = nearby_Facility_20[i]["geometry"]["location"]["lng"]

            latDiff = abs(latL - lat)
            lngDiff = abs(lngL - lng)
            totalDiff = pow(latDiff, 2) + pow(lngDiff, 2)

            myDistance = pow(totalDiff, 0.5)
            resultDict["locDistance"] = myDistance

            myDistanceStr = str(round(139.276 * myDistance, 2)) + " km"
            resultDict["locDistanceStr"] = myDistanceStr

            # Cal Distance -------------------------------------------------------------------------

            resultDict["locRating"] = 0 if nearby_Facility_20[i].get("rating") is None else nearby_Facility_20[i]["rating"]
    #             resultDict["locAddress"] = None if nearby_Facility_20[i].get("vicinity") is None else nearby_Facility_20[i]["vicinity"]

            if nearby_Facility_20[i].get("photos") is None:
                    resultDict["locPhotoUrl"] = None
            else:
                resultDict["locPhoto_reference"] = nearby_Facility_20[i]["photos"][0]["photo_reference"]
                resultDict["locPhoto_width"] = nearby_Facility_20[i]["photos"][0]["width"]
                resultDict["locPhotoUrl"] = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,resultDict["locPhoto_reference"], resultDict["locPhoto_width"])

                ###

            resultList.append(resultDict)
            # print(resultList)
            # print("resultList -------------------------------------------")


    #resultRateList = sorted(resultList, key=lambda x: x['locRating'], reverse=True)
    #locDistance

    #resultRateList = resultList
    resultRateList = sorted(resultList, key=lambda x: x['locDistance'], reverse=False)

    return (resultRateList, result_Num)




# def locationData(locUser, latP, lngP):

#     userInfo = mbkkaround.objects.filter(mbuserid=locUser).last()
#     lat = float(latP)
#     lng = float(lngP)

# #     2022-02-20 ---------------------
# #     kWordList = ["airport" , "aquarium" , "bowling_alley" , "casino" , "cemetery" , "courthouse" , "funeral_home" , "light_rail_station" , "painter" , "synagogue" , "taxi_stand" , "zoo"]
# #     2022-02-20 ---------------------

#     GOOGLE_API_KEY = "AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg"
#     finalRadius = userInfo.mbradius

#     resultList = []

#     if userInfo.mbradius == 0:

#         if userInfo.mbmethod == 1:
#                 # kWord = userInfo.mbkword
#                 gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
#                 # print('url keyword-----------------')
#                 # print(gmap_Example)

#         if userInfo.mbmethod == 2:
#                 # kWord = userInfo.mbkword
#                 gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
#                 print('url keyword type-----------------')
#                 print(gmap_Example)

#         if userInfo.mbmethod == 3:
#                 gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)

#     else:
#         # kWord = userInfo.mbkword
#         gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
#         print('radius keyword-----------------')
#         print(gmap_Example)

#         # if userInfo.mbmethod == 3:
#         # gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
#         # print('radius keyword-----------------')
#         # print(gmap_Example)

#     destSearch = gmap_Example

#     destReq = requests.get(destSearch)
#     nearby_Facility_dict = destReq.json()
#     nearby_Facility_20 = nearby_Facility_dict ["results"]
#     result_Num = len(nearby_Facility_20)


#     for i in range(result_Num):

#         # resultDict = {"locId": 0, "locName": "", "locLat": 0, "locLng": 0, "locRating": None, "locAddress": None,  "locPhotoUrl": None}
#         resultDict = {}

#         if nearby_Facility_20[i]:

#             resultDict["locId"] = i
#             resultDict["locName"] = nearby_Facility_20[i]["name"]
#             resultDict["locLat"] = nearby_Facility_20[i]["geometry"]["location"]["lat"]
#             resultDict["locLng"] = nearby_Facility_20[i]["geometry"]["location"]["lng"]

#             # Cal Distance -------------------------------------------------------------------------

#             latL = nearby_Facility_20[i]["geometry"]["location"]["lat"]
#             lngL = nearby_Facility_20[i]["geometry"]["location"]["lng"]

#             latDiff = abs(latL - lat)
#             lngDiff = abs(lngL - lng)
#             totalDiff = pow(latDiff, 2) + pow(lngDiff, 2)

#             myDistance = pow(totalDiff, 0.5)
#             resultDict["locDistance"] = myDistance

#             myDistanceStr = str(round(139.276 * myDistance, 2)) + " km"
#             resultDict["locDistanceStr"] = myDistanceStr

#             # Cal Distance -------------------------------------------------------------------------

#             resultDict["locRating"] = 0 if nearby_Facility_20[i].get("rating") is None else nearby_Facility_20[i]["rating"]
#     #             resultDict["locAddress"] = None if nearby_Facility_20[i].get("vicinity") is None else nearby_Facility_20[i]["vicinity"]

#             if nearby_Facility_20[i].get("photos") is None:
#                     resultDict["locPhotoUrl"] = None
#             else:
#                 resultDict["locPhoto_reference"] = nearby_Facility_20[i]["photos"][0]["photo_reference"]
#                 resultDict["locPhoto_width"] = nearby_Facility_20[i]["photos"][0]["width"]
#                 resultDict["locPhotoUrl"] = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,resultDict["locPhoto_reference"], resultDict["locPhoto_width"])

#                 ###

#             resultList.append(resultDict)
#             # print(resultList)
#             # print("resultList -------------------------------------------")


#     #resultRateList = sorted(resultList, key=lambda x: x['locRating'], reverse=True)
#     #locDistance

#     #resultRateList = resultList
#     resultRateList = sorted(resultList, key=lambda x: x['locDistance'], reverse=False)

#     return (resultRateList, result_Num)

###














# results["name"]
# results["geometry"]["location"]["lat"]
# results["geometry"]["location"]["lng"]

# results["photos"]["height"]
# results["photos"]["width"]
# results["photos"]["photo_reference"]

# results["vicinity"]
# results["rating"]

# locName = results["name"]
# locLat = results["geometry"]["location"]["lat"]
# locLng = results["geometry"]["location"]["lng"]
# locRating = results["rating"]
# locAddress = results["vicinity"]
# locPhoto_reference = results["photos"]["photo_reference"]
# locPhoto_width = results["photos"]["width"]
# locPhotoUrl = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,locPhoto_reference,locPhoto_width)

# thumbnail_image_url="https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,photo_reference,photo_width)
# map_url="https://www.google.com/maps/search/?api=1&query={lat}, {long}&query_place_id={place_id}".format(lat=location["geometry"]["location"]["lat"], long=location["geometry"]["location"]["lng"],place_id=location["place_id"])

# Elements Srinakarin
# 13.69642131796132,
# 100.64538084064222

# the Privacy Rama9
# 13.74455317945146,
# 100.60296055413663


# ?key={}&location={},{}&...&...&...".format(GOOGLE_API_KEY,lat,lng)
# &keyword=chinese
# &rankby=distance
# &location=13.69642131796132%2C100.64538084064222
# &type=restaurant
# &key=
# &language=zh-TW
# &radius=6000

# # ------------------------------------------------------
