from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from .models import ExcelData
import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                ExcelData.objects.create(timestamp=row['timestamp'], 
                                         country_name=row['country_name'], 
                                         name=row['name'], 
                                         capacity_mw=row['capacity_mw'], 
                                         latitude=row['latitude'], 
                                         longitude=row['longitude'], 
                                         primary_fuel=row['primary_fuel'])
            return redirect('display_data')
    else:
        form = ExcelUploadForm()
    return render(request, 'upload_excel.html', {'form': form})

def display_data(request):
    data = ExcelData.objects.all()
    return render(request, 'display_data.html', {'data': data})


