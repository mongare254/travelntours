from django.contrib import admin
from .models import update,hotel,tourguide,chat,publichat
# Register your models here.
admin.site.register(update)
admin.site.register(hotel)
admin.site.register(tourguide)
admin.site.register(chat)
admin.site.register(publichat)