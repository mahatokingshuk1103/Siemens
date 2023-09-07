# weather_app/views.py
from django.shortcuts import render
import requests

def weather_view(request):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": "53.1,-0.13"}
    headers = {
        "X-RapidAPI-Key": "91477e6fddmshcbf946191cad483p11feccjsnfeeea016c013",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    weather_data = response.json()
    
    return render(request, 'weather_data.html', {'weather_data': weather_data})
