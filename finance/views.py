from django.shortcuts import render,redirect
from .models import history,total_budget
import datetime

now = datetime.datetime.now()

def home(request):
    #Past history of That farmer
    history_all = history.objects.all()
    history_all = history_all.filter(farmer_name__contains= request.user.username) # Filtering the result with that farmer

    #Total budget Fetching
    totalbudget = total_budget.objects.all()
    totalbudget = totalbudget.filter(farmer_name__contains= request.user.username) # Filtering the result with that farmer

    if totalbudget:
        #calculating remaining budget
        bal = 0
        for i in history_all:
            bal+=i.amount

        for x in totalbudget:
            print(x)
            rbud = x.amount - bal
            tbudget = x.amount

        #Clubbing everything in one and then passing it
        content = {
            'history' : history_all,
            'budget' : tbudget,
            'rbudget' : rbud,
        }

        return render(request,'home/finance.html',content)
    else:
        content = {
            'history' : history_all,
            'budget' : 0,
            'rbudget' : 0,
        }
        return render(request,'home/finance.html',content)

def expense(request):
    return render(request, 'home/finance_exp.html')

def totalbudget(request):
    return render(request, 'home/finance_tbud.html')

def totalbudget_confirm(request):
    if request.method == 'POST':
        bud = request.POST['bud']        
        temp = total_budget(farmer_name = request.user.username ,amount = bud)
        temp.save()
        return redirect('finance-home')

def expense_confirm(request):
    if request.method == 'POST':
        fname = request.POST['name']
        price = request.POST['amount']
        fdate = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
        temp = history(farmer_name = request.user.username ,name = fname, amount = price, date = fdate)
        temp.save()
        return redirect('finance-home')

def emi(request):

    #Total budget Fetching
    totalbudget = total_budget.objects.all()
    totalbudget = totalbudget.filter(farmer_name__contains= request.user.username) # Filtering the result with that farmer

    if totalbudget:
        #calculating remaining budget

        for x in totalbudget:
            tbudget = x.amount

        temp = tbudget*0.8
        tbudget-=temp

        #Clubbing everything in one and then passing it
        content = {
            'threshold' : tbudget,
        }
        return render(request,'home/emi.html',content)
    else:
        content = {
            'threshold' : 0,
        }
        return render(request,'home/emi.html',content)