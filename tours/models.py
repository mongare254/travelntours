from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class update(models.Model):
    headline=models.CharField(max_length=50)
    text=models.TextField( default='Text')
    news_image=models.ImageField(upload_to='images/', blank=True)
    date_uploaded = models.DateField(default=date.today())

    def __str__(self):
        return self.headline

    @property
    def posted_today(self):
        return date.today() == self.date_uploaded

class hotel(models.Model):
    hotel_image = models.ImageField(upload_to='images/')
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    town = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(max_length=100)
    website = models.URLField(max_length=1000)
    contacts = models.CharField(max_length=1000)

    def __str__(self):
        return self.hotel_name + ' ' + self.location

class tourguide(models.Model):
    profile_image=models.ImageField(upload_to='images/')
    firstname=models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    facebook_handle=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname +' ' +self.secondname

class publichat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    time_sent=models.DateTimeField()

    def __str__(self):
        today=str(self.time_sent).split('.',2)
        date_today=today[0]
        return  str(self.user)

class chat(models.Model):
    sender=models.CharField(max_length=50, blank=True, null=True, default='Sender')
    receiver=models.CharField(max_length=100)
    subject=models.CharField(max_length=50, default='Subject')
    message=models.TextField(max_length=2000)
    message_read=models.BooleanField(default=False)
    date_sent=models.DateTimeField(max_length=20)

    def __str__(self):
        return  self.receiver

# class Profile(models.Model):
#     gender_choices = (
#         ('MALE', 'MALE'),
#         ('FEMALE', 'FEMALE'),
#     )
#     user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
#     user_type=models.CharField(max_length=500,blank=True)
#     country=models.CharField(max_length=100, blank=True)
#     gender=models.CharField(max_length=50,choices=gender_choices, blank=True)
#
#     def __str__(self):
#         return  self.user.username
#
# @receiver(post_save,sender=User)
# def create_user_profile(sender, instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender,instance,created,**kwargs):
#     instance.profile.save()