from django.shortcuts import render
import pandas as pd

from django.db import connection
from django.core.mail import EmailMessage
from django.http import HttpResponse
import urllib.request, json
import urllib
import time

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
rain = 0
soil_Type = ''
soil_Type_Id = 0

name = ''

v = ''

data_market = [
  {
    "Crop_Id": 0,
    "Crop": "Rice",
    "market_trend": 79
  },
  {
    "Crop_Id": 1,
    "Crop": "Wheat",
    "market_trend": 55
  },
  {
    "Crop_Id": 2,
    "Crop": "Maize",
    "market_trend": 77
  },
  {
    "Crop_Id": 3,
    "Crop": "Millets",
    "market_trend": 32
  },
  {
    "Crop_Id": 4,
    "Crop": "Bajra",
    "market_trend": 37
  },
  {
    "Crop_Id": 5,
    "Crop": "Pulses",
    "market_trend": 53
  },
  {
    "Crop_Id": 6,
    "Crop": "Lentil",
    "market_trend": 42
  },
  {
    "Crop_Id": 7,
    "Crop": "Oilseeds",
    "market_trend": 70
  },
  {
    "Crop_Id": 8,
    "Crop": "Groundnut",
    "market_trend": 67
  },
  {
    "Crop_Id": 9,
    "Crop": "Sugarcane",
    "market_trend": 66
  },
  {
    "Crop_Id": 10,
    "Crop": "Sugar beet",
    "market_trend": 72
  },
  {
    "Crop_Id": 11,
    "Crop": "Cotton",
    "market_trend": 37
  },
  {
    "Crop_Id": 12,
    "Crop": "Tea",
    "market_trend": 87
  },
  {
    "Crop_Id": 13,
    "Crop": "Coffee",
    "market_trend": 58
  },
  {
    "Crop_Id": 14,
    "Crop": "Cocoa",
    "market_trend": 41
  },
  {
    "Crop_Id": 15,
    "Crop": "Rubber",
    "market_trend": 61
  },
  {
    "Crop_Id": 16,
    "Crop": "Jute",
    "market_trend": 67
  },
  {
    "Crop_Id": 17,
    "Crop": "Flax",
    "market_trend": 41
  },
  {
    "Crop_Id": 18,
    "Crop": "Coconut",
    "market_trend": 31
  },
  {
    "Crop_Id": 19,
    "Crop": "Oil-palm",
    "market_trend": 35
  },
  {
    "Crop_Id": 20,
    "Crop": "Clove",
    "market_trend": 80
  },
  {
    "Crop_Id": 21,
    "Crop": "Black Pepper",
    "market_trend": 77
  },
  {
    "Crop_Id": 22,
    "Crop": "Cardamon",
    "market_trend": 57
  },
  {
    "Crop_Id": 23,
    "Crop": "Turmeric",
    "market_trend": 46
  }
]

data_json =[
  {
    "Crop_Id": 0,
    "Crop": "Rice",
    "Rainfall": 125,
    "Temperature": 21,
    "Soil Type": "heavy-clayey",
    "Soil_Id": 0
  },
  {
    "Crop_Id": 1,
    "Crop": "Wheat",
    "Rainfall": 50,
    "Temperature": 19,
    "Soil Type": "well-drained-clay",
    "Soil_Id": 1
  },
  {
    "Crop_Id": 2,
    "Crop": "Maize",
    "Rainfall": 95,
    "Temperature": 21,
    "Soil Type": "deep-heavy clay",
    "Soil_Id": 2
  },
  {
    "Crop_Id": 3,
    "Crop": "Millets",
    "Rainfall": 50,
    "Temperature": 27,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 4,
    "Crop": "Bajra",
    "Rainfall": 43,
    "Temperature": 30,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 5,
    "Crop": "Pulses",
    "Rainfall": 43,
    "Temperature": 24,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 6,
    "Crop": "Lentil",
    "Rainfall": 38,
    "Temperature": 20,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 7,
    "Crop": "Oilseeds",
    "Rainfall": 40,
    "Temperature": 23,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 8,
    "Crop": "Groundnut",
    "Rainfall": 63,
    "Temperature": 20,
    "Soil Type": "well-drained-sandy loams",
    "Soil_Id": 5
  },
  {
    "Crop_Id": 9,
    "Crop": "Sugarcane",
    "Rainfall": 125,
    "Temperature": 63,
    "Soil Type": "Well-drained alluvium",
    "Soil_Id": 6
  },
  {
    "Crop_Id": 10,
    "Crop": "Sugar beet",
    "Rainfall": 37,
    "Temperature": 18,
    "Soil Type": "Well-drained-loamy soil",
    "Soil_Id": 7
  },
  {
    "Crop_Id": 11,
    "Crop": "Cotton",
    "Rainfall": 85,
    "Temperature": 23,
    "Soil Type": "Well-drained-loamy soil",
    "Soil_Id": 7
  },
  {
    "Crop_Id": 12,
    "Crop": "Tea",
    "Rainfall": 175,
    "Temperature": 25,
    "Soil Type": "Light loamy Soil",
    "Soil_Id": 8
  },
  {
    "Crop_Id": 13,
    "Crop": "Coffee",
    "Rainfall": 175,
    "Temperature": 22,
    "Soil Type": "well-drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 14,
    "Crop": "Cocoa",
    "Rainfall": 175,
    "Temperature": 27,
    "Soil Type": "well-drained alluvium",
    "Soil_Id": 6
  },
  {
    "Crop_Id": 15,
    "Crop": "Rubber",
    "Rainfall": 200,
    "Temperature": 14,
    "Soil Type": "well-drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 16,
    "Crop": "Jute",
    "Rainfall": 200,
    "Temperature": 30,
    "Soil Type": "well drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 17,
    "Crop": "Flax",
    "Rainfall": 18,
    "Temperature": 15,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 18,
    "Crop": "Coconut",
    "Rainfall": 175,
    "Temperature": 14,
    "Soil Type": "sandy alluvial",
    "Soil_Id": 10
  },
  {
    "Crop_Id": 19,
    "Crop": "Oil-palm",
    "Rainfall": 325,
    "Temperature": 28,
    "Soil Type": "alluvial soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 20,
    "Crop": "Clove",
    "Rainfall": 225,
    "Temperature": 30,
    "Soil Type": "Red alluvial Soil",
    "Soil_Id": 11
  },
  {
    "Crop_Id": 21,
    "Crop": "Black Pepper",
    "Rainfall": 250,
    "Temperature": 28,
    "Soil Type": "red-loam",
    "Soil_Id": 12
  },
  {
    "Crop_Id": 22,
    "Crop": "Cardamon",
    "Rainfall": 275,
    "Temperature": 23,
    "Soil Type": "Well drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 23,
    "Crop": "Turmeric",
    "Rainfall": 200,
    "Temperature": 25,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  }
]

data_temp =[{
    "Year": 2018,
    "Month": "Jan",
    "Temp": 28.66602
  },
  {
    "Year": 2018,
    "Month": "Feb",
    "Temp": 31.7442
  },
  {
    "Year": 2018,
    "Month": "Mar",
    "Temp": 34.44972
  },
  {
    "Year": 2018,
    "Month": "Apr",
    "Temp": 35.79923
  },
  {
    "Year": 2018,
    "Month": "May",
    "Temp": 34.45511
  },
  {
    "Year": 2018,
    "Month": "Jun",
    "Temp": 32.83266
  },
  {
    "Year": 2018,
    "Month": "Jul",
    "Temp": 32.55024
  },
  {
    "Year": 2018,
    "Month": "Aug",
    "Temp": 32.54397
  },
  {
    "Year": 2018,
    "Month": "Sep",
    "Temp": 32.29959
  },
  {
    "Year": 2018,
    "Month": "Oct",
    "Temp": 29.86055
  },
  {
    "Year": 2018,
    "Month": "Nov",
    "Temp": 27.31297
  },
  {
    "Year": 2018,
    "Month": "Dec",
    "Temp": 26.4762
  },
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
 	return render(request,'home/predict.html')

def predres(request):

	data = [
  {
    "Crop_Id": 0,
    "Crop": "Rice",
    "Rainfall": 125,
    "Temperature": 21,
    "Soil Type": "heavy-clayey",
    "Soil_Id": 0
  },
  {
    "Crop_Id": 1,
    "Crop": "Wheat",
    "Rainfall": 50,
    "Temperature": 19,
    "Soil Type": "well-drained-clay",
    "Soil_Id": 1
  },
  {
    "Crop_Id": 2,
    "Crop": "Maize",
    "Rainfall": 95,
    "Temperature": 21,
    "Soil Type": "deep-heavy clay",
    "Soil_Id": 2
  },
  {
    "Crop_Id": 3,
    "Crop": "Millets",
    "Rainfall": 50,
    "Temperature": 27,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 4,
    "Crop": "Bajra",
    "Rainfall": 43,
    "Temperature": 30,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 5,
    "Crop": "Pulses",
    "Rainfall": 43,
    "Temperature": 24,
    "Soil Type": "Sandy-loam",
    "Soil_Id": 3
  },
  {
    "Crop_Id": 6,
    "Crop": "Lentil",
    "Rainfall": 38,
    "Temperature": 20,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 7,
    "Crop": "Oilseeds",
    "Rainfall": 40,
    "Temperature": 23,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 8,
    "Crop": "Groundnut",
    "Rainfall": 63,
    "Temperature": 20,
    "Soil Type": "well-drained-sandy loams",
    "Soil_Id": 5
  },
  {
    "Crop_Id": 9,
    "Crop": "Sugarcane",
    "Rainfall": 125,
    "Temperature": 63,
    "Soil Type": "Well-drained alluvium",
    "Soil_Id": 6
  },
  {
    "Crop_Id": 10,
    "Crop": "Sugar beet",
    "Rainfall": 37,
    "Temperature": 18,
    "Soil Type": "Well-drained-loamy soil",
    "Soil_Id": 7
  },
  {
    "Crop_Id": 11,
    "Crop": "Cotton",
    "Rainfall": 85,
    "Temperature": 23,
    "Soil Type": "Well-drained-loamy soil",
    "Soil_Id": 7
  },
  {
    "Crop_Id": 12,
    "Crop": "Tea",
    "Rainfall": 175,
    "Temperature": 25,
    "Soil Type": "Light loamy Soil",
    "Soil_Id": 8
  },
  {
    "Crop_Id": 13,
    "Crop": "Coffee",
    "Rainfall": 175,
    "Temperature": 22,
    "Soil Type": "well-drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 14,
    "Crop": "Cocoa",
    "Rainfall": 175,
    "Temperature": 27,
    "Soil Type": "well-drained alluvium",
    "Soil_Id": 6
  },
  {
    "Crop_Id": 15,
    "Crop": "Rubber",
    "Rainfall": 200,
    "Temperature": 14,
    "Soil Type": "well-drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 16,
    "Crop": "Jute",
    "Rainfall": 200,
    "Temperature": 30,
    "Soil Type": "well drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 17,
    "Crop": "Flax",
    "Rainfall": 18,
    "Temperature": 15,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  },
  {
    "Crop_Id": 18,
    "Crop": "Coconut",
    "Rainfall": 175,
    "Temperature": 14,
    "Soil Type": "sandy alluvial",
    "Soil_Id": 10
  },
  {
    "Crop_Id": 19,
    "Crop": "Oil-palm",
    "Rainfall": 325,
    "Temperature": 28,
    "Soil Type": "alluvial soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 20,
    "Crop": "Clove",
    "Rainfall": 225,
    "Temperature": 30,
    "Soil Type": "Red alluvial Soil",
    "Soil_Id": 11
  },
  {
    "Crop_Id": 21,
    "Crop": "Black Pepper",
    "Rainfall": 250,
    "Temperature": 28,
    "Soil Type": "red-loam",
    "Soil_Id": 12
  },
  {
    "Crop_Id": 22,
    "Crop": "Cardamon",
    "Rainfall": 275,
    "Temperature": 23,
    "Soil Type": "Well drained alluvial Soil",
    "Soil_Id": 9
  },
  {
    "Crop_Id": 23,
    "Crop": "Turmeric",
    "Rainfall": 200,
    "Temperature": 25,
    "Soil Type": "clayey loam",
    "Soil_Id": 4
  }
]

	global v

	v = request.POST['crop']
	v = str(v)

	global soil_Type
	global name
	global rain
	global soil_Type_Id

	for i in range(len(data)):
		if data[i]['Crop']==v:
			name = data[i]['Crop']
			rain = data[i]['Rainfall']
			temp = data[i]['Temperature']
			soil_Type = data[i]['Soil Type']
			soil_Type_Id = data[i]['Soil_Id']

	print(data[0])

	return render(request,'home/predcrop.html', {'name': name, 'rain': rain, 'temp': temp, 'soil_Type': soil_Type})

	# json_string = ''


	# if request.method == 'POST': 
	# 	df1 = df[df.Crop == request.POST['crop']]
	# 	return render(request,'home/predcrop.html', {'cr': df1['Rainfall']})
	# else:
	# 	return render(request,'home/predcrop.html')

def predresyes(request):
	###Localhost api to change	 
	# with urllib.request.urlopen("http://127.0.0.1:5000/get_rainfall") as url:
	# 	data = str(url.read())

	# url = "http://127.0.0.1:5000/get_rainfall"
	# response = urllib.urlopen(url)
	# data = json.loads(response.read())

	data =[{
    "Year": 2018,
    "Month": "Jan",
    "Rainfall": 0
  },
  {
    "Year": 2018,
    "Month": "Feb",
    "Rainfall": 0
  },
  {
    "Year": 2018,
    "Month": "Mar",
    "Rainfall": 3.14448114
  },
  {
    "Year": 2018,
    "Month": "Apr",
    "Rainfall": 1.92699406
  },
  {
    "Year": 2018,
    "Month": "May",
    "Rainfall": 12.88658375
  },
  {
    "Year": 2018,
    "Month": "Jun",
    "Rainfall": 155.1600264
  },
  {
    "Year": 2018,
    "Month": "Jul",
    "Rainfall": 250.9730263
  },
  {
    "Year": 2018,
    "Month": "Aug",
    "Rainfall": 203.6405144
  },
  {
    "Year": 2018,
    "Month": "Sep",
    "Rainfall": 164.6351429
  },
  {
    "Year": 2018,
    "Month": "Oct",
    "Rainfall": 68.97461571
  },
  {
    "Year": 2018,
    "Month": "Nov",
    "Rainfall": 15.411257
  },
  {
    "Year": 2018,
    "Month": "Dec",
    "Rainfall": 0.34225687
  },
  {
    "Year": 2019,
    "Month": "Jan",
    "Rainfall": 0
  },
  {
    "Year": 2019,
    "Month": "Feb",
    "Rainfall": 0
  },
  {
    "Year": 2019,
    "Month": "Mar",
    "Rainfall": 2.84430148
  },
  {
    "Year": 2019,
    "Month": "Apr",
    "Rainfall": 1.6268144
  },
  {
    "Year": 2019,
    "Month": "May",
    "Rainfall": 12.5864041
  },
  {
    "Year": 2019,
    "Month": "Jun",
    "Rainfall": 154.8598467
  },
  {
    "Year": 2019,
    "Month": "Jul",
    "Rainfall": 250.6728467
  },
  {
    "Year": 2019,
    "Month": "Aug",
    "Rainfall": 203.3403347
  },
  {
    "Year": 2019,
    "Month": "Sep",
    "Rainfall": 164.3349632
  },
  {
    "Year": 2019,
    "Month": "Oct",
    "Rainfall": 68.67443605
  },
  {
    "Year": 2019,
    "Month": "Nov",
    "Rainfall": 15.11107734
  },
  {
    "Year": 2019,
    "Month": "Dec",
    "Rainfall": 0.04207721
  }
]
	global soil_Type
	global name
	global soil_Type_Id
	global rain

	print(data)
	import time
	strings = time.strftime("%Y,%m,%d,%H,%M,%S")
	t = strings.split(',')
	numbers = [ int(x) for x in t ]
	rainavg = 0
	tempavg = 0
	print('number[0]',numbers[0])
		
	for i in range(0,len(data)):
		if str(data[i]['Year']) == str(numbers[0]):
			if data[i]['Month']=='Jun' or data[i]['Month']=='Jul' or data[i]['Month']=='Aug' or data[i]['Month']=='Sep':
				rainavg = rainavg+data[i]['Rainfall']

	for i in range(0,len(data_temp)):
		if str(data_temp[i]['Year']) == str(numbers[0]):
			tempavg = tempavg+data_temp[i]['Temp']



	print(rainavg)
	print(tempavg/12)

	df = pd.DataFrame.from_dict(data_json, orient='columns')
	df.columns = ['Crop', 'Crop_Id', 'Rainfall', 'Soil_Type', 'Soil_Id', 'Temperature']

	print(df.head(10))
	print('ffffjjdj')
	print(soil_Type)
	df = df.drop(df[df.Soil_Type != soil_Type].index)
	print(df.head(10))
	# View the first ten rows
	

	print(df.iloc[:, [2,4,5]].values)
	X = df.iloc[:, [2,4,5]].values
	print(df.iloc[:, [0]].values)
	y = df.iloc[:, [1]].values


	# Splitting the dataset into the Training set and Test set
	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


	#Random Forest Classifier
	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
	classifier.fit(X, y)

	print(classifier.predict([[rainavg,tempavg,soil_Type_Id]]))

	res = classifier.predict([[rainavg,tempavg,soil_Type_Id]])[0]

	print('res: ',res)
	for i in range(len(data_json)):
		if data_json[i]['Crop_Id'] == res:
			op = data_json[i]['Crop']

	# url = "http://127.0.0.1:5000/get_market_trend"
	# html = urlopen(url)
	# soup = BeautifulSoup(html, 'lxml')

	#print(soup.get_text())

	# st = soup.get_text()

	# print(st)

	mt = 0
	mtv = 0


	for i in range(len(data_market)):
		if data_market[i]['Crop'] == op:

			mt = data_market[i]['market_trend']

		if data_market[i]['Crop'] == v:

			mtv = data_market[i]['market_trend']

	if mt<=mtv:
		op = v
		mt = mtv

	return render(request,'home/predcropyes.html', {"rainavg": rainavg/4, "predicted_crop": op, "market_trend": mt})


def predresno(request):

 	return render(request,'home/predresno.html')

def predresno2(request):
	
	if request.method == 'POST':
		r = request.POST['rain']
		t = request.POST['temp']
		s = request.POST['soil']
		print(r, t, s)

	data =[{
    "Year": 2018,
    "Month": "Jan",
    "Rainfall": 0
  },
  {
    "Year": 2018,
    "Month": "Feb",
    "Rainfall": 0
  },
  {
    "Year": 2018,
    "Month": "Mar",
    "Rainfall": 3.14448114
  },
  {
    "Year": 2018,
    "Month": "Apr",
    "Rainfall": 1.92699406
  },
  {
    "Year": 2018,
    "Month": "May",
    "Rainfall": 12.88658375
  },
  {
    "Year": 2018,
    "Month": "Jun",
    "Rainfall": 155.1600264
  },
  {
    "Year": 2018,
    "Month": "Jul",
    "Rainfall": 250.9730263
  },
  {
    "Year": 2018,
    "Month": "Aug",
    "Rainfall": 203.6405144
  },
  {
    "Year": 2018,
    "Month": "Sep",
    "Rainfall": 164.6351429
  },
  {
    "Year": 2018,
    "Month": "Oct",
    "Rainfall": 68.97461571
  },
  {
    "Year": 2018,
    "Month": "Nov",
    "Rainfall": 15.411257
  },
  {
    "Year": 2018,
    "Month": "Dec",
    "Rainfall": 0.34225687
  },
  {
    "Year": 2019,
    "Month": "Jan",
    "Rainfall": 0
  },
  {
    "Year": 2019,
    "Month": "Feb",
    "Rainfall": 0
  },
  {
    "Year": 2019,
    "Month": "Mar",
    "Rainfall": 2.84430148
  },
  {
    "Year": 2019,
    "Month": "Apr",
    "Rainfall": 1.6268144
  },
  {
    "Year": 2019,
    "Month": "May",
    "Rainfall": 12.5864041
  },
  {
    "Year": 2019,
    "Month": "Jun",
    "Rainfall": 154.8598467
  },
  {
    "Year": 2019,
    "Month": "Jul",
    "Rainfall": 250.6728467
  },
  {
    "Year": 2019,
    "Month": "Aug",
    "Rainfall": 203.3403347
  },
  {
    "Year": 2019,
    "Month": "Sep",
    "Rainfall": 164.3349632
  },
  {
    "Year": 2019,
    "Month": "Oct",
    "Rainfall": 68.67443605
  },
  {
    "Year": 2019,
    "Month": "Nov",
    "Rainfall": 15.11107734
  },
  {
    "Year": 2019,
    "Month": "Dec",
    "Rainfall": 0.04207721
  }
]
	global soil_Type
	global name
	global soil_Type_Id
	global rain

	soil_Type = s
	rain = r

	for i in range(len(data_json)):
		if data_json[i]['Soil Type']==s:
			soil_Type_Id = data_json[i]['Soil_Id']



	print(data)
	import time
	strings = time.strftime("%Y,%m,%d,%H,%M,%S")
	t = strings.split(',')
	numbers = [ int(x) for x in t ]
	rainavg = 0
	tempavg = 0
	print('number[0]',numbers[0])
		
	for i in range(0,len(data)):
		if str(data[i]['Year']) == str(numbers[0]):
			if data[i]['Month']=='Jun' or data[i]['Month']=='Jul' or data[i]['Month']=='Aug' or data[i]['Month']=='Sep':
				rainavg = rainavg+data[i]['Rainfall']

	for i in range(0,len(data_temp)):
		if str(data_temp[i]['Year']) == str(numbers[0]):
			tempavg = tempavg+data_temp[i]['Temp']



	print(rainavg)
	print(tempavg/12)

	rainavg = rainavg/4
	tempavg = tempavg/12

	df = pd.DataFrame.from_dict(data_json, orient='columns')
	df.columns = ['Crop', 'Crop_Id', 'Rainfall', 'Soil_Type', 'Soil_Id', 'Temperature']

	print(df.head(10))
	print('ffffjjdj')
	print(soil_Type)
	df = df.drop(df[df.Soil_Type != soil_Type].index)
	print(df.head(10))
	# View the first ten rows
	

	print(df.iloc[:, [2,4,5]].values)
	X = df.iloc[:, [2,4,5]].values
	print(df.iloc[:, [0]].values)
	y = df.iloc[:, [1]].values


	# Splitting the dataset into the Training set and Test set
	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


	#Random Forest Classifier
	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
	classifier.fit(X, y)

	print(classifier.predict([[rainavg,tempavg,soil_Type_Id]]))

	res = classifier.predict([[rainavg,tempavg,soil_Type_Id]])[0]

	print('res: ',res)
	for i in range(len(data_json)):
		if data_json[i]['Crop_Id'] == res:
			op = data_json[i]['Crop']

	# url = "http://127.0.0.1:5000/get_market_trend"
	# html = urlopen(url)
	# soup = BeautifulSoup(html, 'lxml')

	#print(soup.get_text())

	# st = soup.get_text()

	# print(st)

	mt = 0
	mtv = 0


	for i in range(len(data_market)):
		if data_market[i]['Crop'] == op:

			mt = data_market[i]['market_trend']

		if data_market[i]['Crop'] == v:

			mtv = data_market[i]['market_trend']

	if mt<=mtv:
		op = v
		mt = mtv


	return render(request,'home/predresno2.html', {"rainavg": rainavg, "predicted_crop": op, "market_trend": mt})