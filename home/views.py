from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from fertilizer_shop.models import fertilizer_data
from sell.models import buyer_demand,farmer_crops

def home(request):
	if request.user.is_authenticated:
		print('auth')
		if 'buyer' in str(request.user):
			print('buyer')
			fertilizer = fertilizer_data.objects.all()
			fertilizer = fertilizer.filter(buyer__contains= request.user.username)
			return render(request, 'fertilizer_shop/index.html', {'fertilizer': fertilizer})
		elif 'company' in str(request.user):
				crops_d = farmer_crops.objects.all()
				buyer_d = buyer_demand.objects.all()
				buyer_d = buyer_d.filter(buyer_name__contains= request.user.username)
				content = {
					'crops': crops_d,
					'buy': buyer_d,
				}
				return render(request,'company/company.html', content)
		else:
			print('farmer')
			return render(request,'home/index.html')
	else:
		return render(request,'home/login.html')

def ysearch(request):
	return render(request, 'home/youtube.html')

def login_view(request):
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			print('sucess')
			if 'buyer' in username:
				fertilizer = fertilizer_data.objects.all()
				fertilizer = fertilizer.filter(buyer__contains= request.user.username)
				return render(request, 'fertilizer_shop/index.html',{'fertilizer': fertilizer})
			elif 'company' in username:
				crops_d = farmer_crops.objects.all()
				buyer_d = buyer_demand.objects.all()
				buyer_d = buyer_d.filter(buyer_name__contains= request.user.username)
				content = {
					'crops': crops_d,
					'buy': buyer_d,
				}
				return render(request,'company/company.html', content)
			else:
				return redirect('home-index')
		else:
			return render(request, 'home/login.html')

def help(request):
	return render(request, 'home/help.html')