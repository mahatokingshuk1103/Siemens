from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IoTData
from .serializers import IoTDataSerializer

class IoTDataView(APIView):
    def post(self, request):
        serializer = IoTDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def data_list_view(request):
    data = IoTData.objects.all().order_by('-timestamp')
    return render(request, 'data_list.html', {'data': data})
