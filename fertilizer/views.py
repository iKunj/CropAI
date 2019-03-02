from django.shortcuts import render
from fertilizer_shop.models import fertilizer_data

def home(request):
	fertilizer = fertilizer_data.objects.all()
	return render(request,'home/fertilizer.html', {'fertilizer': fertilizer})