from django.db import models

# Create your models here.

class User_Data(models.Model):
    mainkey    = models.CharField(max_length=100,default=None,unique=True,null=False)
    user_id         = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    management      = models.CharField(max_length=1000,default=None,null=False)
    organization    = models.CharField(max_length=100,unique=True,default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)

    def __str__(self):
        return self.username