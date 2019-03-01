from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def home(request):
	if request.user.is_authenticated:
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
			return render(request, 'home/index.html')