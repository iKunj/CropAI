from django.shortcuts import render

def home(request):
 	return render(request,'home/policy.html')

def apply(request):
	s_name = request.POST['scheme']
	content = {
		'title' : s_name,
		'fname' : request.user.username,
	}
	return render(request, 'home/apply.html',content)