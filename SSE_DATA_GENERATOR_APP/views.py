from django.shortcuts import render
# sseapp/views.py
from django.http import StreamingHttpResponse
import json
import random
import time

def sse(request):
    def event_stream():
        while True:
            data = {
                'time': time.strftime("%Y-%m-%d %H:%M:%S"),
                'humidity': round(random.uniform(30, 70), 2),  # Simulate humidity data
                'temperature': round(random.uniform(18, 28), 2),  # Simulate temperature data
            }
            yield f"{json.dumps(data)}\n\n"
            time.sleep(10)  # Adjust the interval as needed

    response = StreamingHttpResponse(event_stream(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response

