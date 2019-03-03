from django.shortcuts import render
import requests

data_temp =[
  {
    "Year": 2019,
    "Month": "Jan",
    "Temp": 28.90514
  },
  {
    "Year": 2019,
    "Month": "Feb",
    "Temp": 31.98333
  },
  {
    "Year": 2019,
    "Month": "Mar",
    "Temp": 34.68884
  },
  {
    "Year": 2019,
    "Month": "Apr",
    "Temp": 36.03836
  },
  {
    "Year": 2019,
    "Month": "May",
    "Temp": 34.69424
  },
  {
    "Year": 2019,
    "Month": "Jun",
    "Temp": 33.07179
  },
  {
    "Year": 2019,
    "Month": "Jul",
    "Temp": 32.78937
  },
  {
    "Year": 2019,
    "Month": "Aug",
    "Temp": 32.7831
  },
  {
    "Year": 2019,
    "Month": "Sep",
    "Temp": 32.53871
  },
  {
    "Year": 2019,
    "Month": "Oct",
    "Temp": 30.09967
  },
  {
    "Year": 2019,
    "Month": "Nov",
    "Temp": 27.5521
  },
  {
    "Year": 2019,
    "Month": "Dec",
    "Temp": 26.71533
  }
]

def home(request):
	args = {}
	ll = []
	url = "https://openweathermap.org/data/2.5/weather?q=bangalore&appid=b6907d289e10d714a6e88b30761fae22"
	r = requests.get(url.format()).json()
	args['contents'] = r
	for i in range(len(data_temp)):
		ll.append(data_temp[i]['Temp'])
	return render(request,'home/temperature.html', {"data": ll, "args":args})