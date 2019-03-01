from django.shortcuts import render
import requests

def home(request):
	args = {}
	r = requests.get('https://newsapi.org/v2/everything?q=agriculture%20india&apiKey=35a9468e4b31475da1cf8c3bd0fb4a6b')
	args['contents'] = r.json()
	return render(request,'home/news.html', args)