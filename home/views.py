from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from fertilizer_shop.models import fertilizer_data

def home(request):
	if request.user.is_authenticated:
		print('auth')
		if 'buyer' in str(request.user):
			print('buyer')
			fertilizer = fertilizer_data.objects.all()
			fertilizer = fertilizer.filter(buyer__contains= request.user.username)
			return render(request, 'fertilizer_shop/index.html', {'fertilizer': fertilizer})
		else:
			print('farmer')
			return render(request,'home/index.html')
	else:
		return render(request,'home/login.html')


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
			else:
				return redirect('home-index')
		else:
			return render(request, 'home/login.html')