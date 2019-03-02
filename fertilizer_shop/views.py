from django.shortcuts import render,redirect
from .models import fertilizer_data

def add(request):
    return render(request, 'fertilizer_shop/add.html')

def add_confirm(request):
    if request.method == 'POST':  
        fname = request.POST['fname']
        fprice = request.POST['price']
        print(fname)
        print(fprice)
        temp = fertilizer_data(buyer = request.user.username ,name = fname, price = fprice)
        temp.save()
        return redirect('home-index')