from django.shortcuts import render,redirect
from .models import publichat,chat,update,hotel,tourguide
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages as errors
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    news=update.objects.all().order_by('date_uploaded')
    return render(request, 'tours/home.html',{'news':news})

def accommodation(request):
    city = hotel.objects.values_list('town', flat=True).distinct()
    hotelnames = hotel.objects.values_list('hotel_name', flat=True).distinct()
    resorts=hotel.objects.all().order_by('-price')
    return render(request,'tours/hotels.html', {'resorts':resorts, 'city':city, 'hotelnames':hotelnames})

@csrf_exempt
def hotelsearch(request):
    if request.method =='POST':
        city=request.POST['city']
        hotels=hotel.objects.filter(town=city)
        return render(request, 'tours/citysearch.html', {'hotels': hotels,'city':city})
    else:
        city=hotel.objects.values_list('town',flat=True)
        return render(request, 'tours/citysearch.html', {'city':city})

@csrf_exempt
def hotel_name_search(request):
    if request.method =='POST':
        searched_hotel=request.POST['hotel']
        available_hotels=hotel.objects.filter(hotel_name=searched_hotel)
        return render(request, 'tours/hotelsearch.html', {'available_hotels': available_hotels, 'hotel_name':searched_hotel})
    else:
        return render(request, 'tours/hotelsearch.html')

def guide(request):
    guides=tourguide.objects.all()
    return render(request, 'tours/guides.html', {'guides':guides})

def message(request):
    all_messages=chat.objects.all().order_by('-date_sent')
    chats=publichat.objects.all().order_by('-time_sent')
    return render(request, 'tours/message.html', {'chats':chats, 'messages':all_messages})


def register(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        username = request.POST['username']
        country=request.POST['country']
        gender= request.POST['gender']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            errors.error(request, 'USERNAME IS TAKEN')
            return render(request, 'tours/register.html')
        else:
            user=User.objects.create_user(
                username=username,password=password
            )
            profile =user.profile
            profile.country=country
            profile.gender=gender
            profile.firstname = firstname
            profile.secondname=secondname
            profile.user_type='USER'
            profile.save()
            login(request,user)
            return redirect('home')

    else:
        return redirect('index')

def loginuser(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            errors.warning(request, 'INVALID CREDENTIALS!!!')
            return render(request, 'tours/index.html')

    else:
        return render(request, 'tours/index.html')


def logout_user(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def readmessage(request):
    if request.method =='POST':
        id=request.POST['id']
        current_chat=chat.objects.filter(id=id)
        return render(request, 'tours/readmessage.html', {'chat':current_chat})
    else:
        current_chat = chat.objects.filter(id=id)
        return render(request, 'tours/readmessage.html', {'chat': current_chat})