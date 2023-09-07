# views.py
import requests
from django.shortcuts import render
from SSE_App.models import SSEDataPoint

def save_data_from_url(request):
    url = 'http://127.0.0.1:8000/sse/'  # Replace with your actual URL

    try:
        response = requests.get(url)
        data = response.json()  # Assuming the data is in JSON format

        for item in data:
            your_model_instance = SSEDataPoint(
                time=item['time'],
                humidity=item['humidity'],
                temperature=item['temperature']
                
            )
            your_model_instance.save()
            
        return render(request, 'success.html', {'message': 'Data imported successfully.'})

    except Exception as e:
        return render(request, 'error.html', {'message': str(e)})
