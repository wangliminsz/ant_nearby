# from winsound import MB_ICONEXCLAMATION
from django.db import models

# Create your models here.

# insert into arapp_mbkk ()

class mbkkaround(models.Model):
    # mbid = models.IntegerField()
    # mbname = models.CharField(max_length=256)
    # mbstyle = models.CharField(max_length=64)
    # mbtakeaway = models.CharField(max_length=64)
    # mblat = models.FloatField()
    # mblng = models.FloatField()
    # mburl = models.CharField(max_length=256)
    # mbimgurl=models.CharField(max_length=256)
    # mbaddress=models.CharField(max_length=256)
    # mbprice=models.CharField(max_length=64)
    # mbview = models.TextField()
    # mbcontact=models.CharField(max_length=32)
    # mbservice = models.TextField()
    # mbaward=models.CharField(max_length=256)

    mbuserid = models.CharField(max_length=64)

    mbtype = models.CharField(max_length=64,null=True,blank=True)
    mb_plat = models.CharField(max_length=64,null=True,blank=True)
    mb_plng = models.CharField(max_length=64,null=True,blank=True)

    mbmethod = models.IntegerField(default=0) # 1- keyword 2- keyword&type 3- listtype
    mbkword = models.CharField(max_length=256,null=True,blank=True)
    mbradius = models.IntegerField(default=0)

class mbkkdetail(models.Model):

    dtuserid = models.CharField(max_length=64)

    dtlocid =  models.IntegerField(default=99)
    dtlocname =  models.CharField(max_length=256,null=True,blank=True)
    dtloclat = models.FloatField()
    dtloclng = models.FloatField()
    dtlocrating = models.DecimalField(max_digits=3, decimal_places=1)
    dtlocdistance=models.CharField(max_length=32,null=True,blank=True)

    # dtlocaddress =  models.CharField(max_length=512,null=True,blank=True)
    dtlocphotourl =  models.CharField(max_length=512,null=True,blank=True)

    # locId
    # locName
    # locLat
    # locLng
    # locRating
    # locAddress
    # locPhotoUrl


    # mbuserid = models.CharField(max_length=64)
    # mbmethod = models.IntegerField(default=0) # 1- keyword 2- keyword&type 3- listtype
    # mbtype = models.CharField(max_length=64,null=True,blank=True)
    # mbkword = models.CharField(max_length=256,null=True,blank=True)
    # mbradius = models.IntegerField(default=0)



