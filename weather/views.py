from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = "96354df7ef3c68331244e10536eca9bf"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
  

    
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        try:
            res_n = requests.get(url.format(city.name))
            res = res_n.json()
            city_info = {
                'city': city.name,
                'temp':res["main"]["temp"],
                'icon':res['weather'][0]['icon']
                }
            all_cities.append(city_info)
        except:
            redirect ('/home')
        

    context = {
        'all_info': all_cities,
        'form':form
    }

    return render(request,'main/index.html', context)

def about(request):
    return render(request,'main/about.html')