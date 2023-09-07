# views.py
import json
from django.http import StreamingHttpResponse
from django.shortcuts import render
import requests
from .models import SSEDATAPOINT

def save_data_to_database(request):
    url = 'http://127.0.0.1:8000/sse/'  # Replace with your actual URL

    def data_generator():
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    data = json.loads(line)
                    
                    # Extract data from the JSON response
                    time = data['time']
                    humidity = data['humidity']
                    temperature = data['temperature']

                    # Create a new SensorData instance and save it to the database
                    sensor_data = SSEDATAPOINT(
                        time=time,
                        humidity=humidity,
                        temperature=temperature
                    )
                    sensor_data.save()

                    yield f'Data saved: {sensor_data}\n'
                else:
                    yield 'Empty line received\n'
        else:
            yield f'Failed to fetch data from URL. Status code: {response.status_code}\n'

    return StreamingHttpResponse(data_generator(), content_type='text/plain')


def show_data(request):
    sensor_data = SSEDATAPOINT.objects.all().order_by('-time')
    return render(request, 'data_list2.html', {'sensor_data': sensor_data})


def chart_view(request):
    data_points = SSEDATAPOINT.objects.all()
    data = [{'time': point.time.strftime('%Y-%m-%d %H:%M:%S'), 'humidity': point.humidity, 'temperature': point.temperature} for point in data_points]
    data_json = json.dumps(data)
    return render(request, 'graph.html', {'data_json': data_json})

