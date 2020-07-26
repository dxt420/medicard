from django.db import models
import uuid


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


from django.utils import timezone
import datetime

 

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False,blank=True)
    is_super_admin = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.username
  

class Agent(models.Model):
    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    contact = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    membership_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,blank=True)
    contact = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50,blank=True)
    dob = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    # fpbiotemplate1 = models.CharField(max_length=10000,blank=True)
	# fpbiotemplate2 = models.CharField(max_length=10000,blank=True)
	# fno1 = models.CharField(max_length=2,blank=True)
	# fno2 = models.CharField(max_length=2,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MemberFunds(models.Model):
    membership_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    balance = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.membership_id.name


class Log(models.Model):
    log_message = models.CharField(max_length=500,blank=True)
    log_secondary_message = models.CharField(max_length=500,blank=True)
    log_user_id = models.CharField(max_length=50,blank=True)
    log_secondary_user_id = models.CharField(max_length=50,blank=True)
    log_type = models.CharField(max_length=50,blank=True) #use this to specify more forexample logs for funds or check ins e.t.c
    created_at = models.DateTimeField(auto_now_add=True)




####log model here ininit



# class users(models.Model):
# 	fname = models.CharField(max_length=50)
# 	sname = models.CharField(max_length=50)
# 	empno = models.CharField(max_length=50)

