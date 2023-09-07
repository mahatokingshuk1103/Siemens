# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_another_item.html')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


# views.py
import qrcode
from django.shortcuts import render
from .models import Item
import qrcode
from django.http import HttpResponse
from io import BytesIO
from PIL import Image


def generate_qr_code(request, item_id):
    item = Item.objects.get(pk=item_id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(item.location)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

# views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def modify_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    new_description = request.GET.get('new_description', '')

    if new_description:
        item.description = new_description
        item.save()
        return JsonResponse({'message': 'Item description updated successfully.'})
    else:
        return JsonResponse({'message': 'No data received for update.'})


