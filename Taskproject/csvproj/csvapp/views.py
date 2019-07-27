from django.shortcuts import render
from csvapp.forms import LoginForm,FileForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'csvapp/base.html')

def login(request):
    form=LoginForm()
    if request.method=='POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'csvapp/login.html',{'form':form})

def upload(request):
    form=FileForm()
    if request.method=='POST':
        form =FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'csvapp/upload_csv.html',{'form':form})
    return render(request,'csvapp/graph.html',{'form':form})


import csv
from collections import Counter
import matplotlib.pyplot as plt
def plots(request):
    with open('assignment.csv',newline='') as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        if(reader!=''):
            for row in reader:
                d={}
                c=[]
                for row1 in row[1:]:
                    d[row1]=d.get(row1,0)+1
                    if row1 is not int and row1!='':
                        c.append(int(row1))
                    elif row1 is str:
                        pass
                        
                #print(c)
                tmp=Counter(c)
                #print(tmp)
                votes=[]
                for i in tmp:
                    votes.append([i,tmp[i]])
                plt.bar([row[0] for row in votes],[row[1] for row in votes])
                plt.axis([0,5,0,20])
                plt.show()
            return HttpResponse('<h1>All charts are Completed Successfully <h1>')
        else:
            pass
