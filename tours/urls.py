from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('hotels', views.accommodation, name="hotel"),
    path('index', views.loginuser, name='index'),
    path('hotelsearch', views.hotelsearch, name="hotelsearch"),
    path('hotels_name_search', views.hotel_name_search, name="hotelnamesearch"),
    path('guide', views.guide, name="guide"),
    path('message', views.message, name='messages'),
    path('logout', views.logout_user, name='logout'),
    path('readmessage', views.readmessage, name='readmessage')
]