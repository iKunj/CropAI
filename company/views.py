from django.shortcuts import render,redirect
from sell.models import buyer_demand,farmer_crops

# Create your views here.
def home(request):
    crops_d = farmer_crops.objects.all()
    buyer_d = buyer_demand.objects.all()
    buyer_d = buyer_d.filter(buyer_name__contains= request.user.username)
    content = {
        'crops': crops_d,
        'buy': buyer_d,
    }
    return render(request,'company/company.html', content)

def add(request):
    return render(request, 'company/add.html')

def add_confirm(request):
    if request.method == 'POST':  
        fname = request.POST['fname']
        fprice = request.POST['price']
        fquantity = request.POST['quan']
        print(fname)
        print(fprice)
        temp = buyer_demand(buyer_name = request.user.username ,crop_name = fname, amount = fprice, quantity = fquantity)
        temp.save()
        return redirect('company-home')

def add_confirm_attach(request):
    print('Hello')
    id_temp = request.POST['id']
    print(id_temp)
    temp = farmer_crops.objects.get(id = id_temp)
    temp.bought = request.user.username
    temp.flag = 1
    temp.save()
    return redirect('company-home')
    