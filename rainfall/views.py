from django.shortcuts import render

data =[
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


def home(request):
	ll = []
	rainavg = 0  
	for i in range(0,len(data)):
		if str(data[i]['Year']) == '2019':
			if data[i]['Month']=='Jun' or data[i]['Month']=='Jul' or data[i]['Month']=='Aug' or data[i]['Month']=='Sep':
				rainavg = rainavg+data[i]['Rainfall']
	
	for i in range(len(data)):
		ll.append(data[i]['Rainfall'])
    
	return render(request,'home/rainfall.html', {"data": ll , "rainavg":(rainavg/4)})