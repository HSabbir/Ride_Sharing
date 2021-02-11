from django.shortcuts import render
from django.http.request import HttpRequest

from .calculation import *

driverlist = []

def rider(request, x, y,x1,y1):
    coordinate = {'x':x,'y':y,'x1':x1,'y1':y1}
    index = assignDriverToRider([x,y],driverlist)
    print(driverlist[index])
    driver.pop(index)
    return render(request,'index.html',{'coordinate':coordinate})

def driver(request, x, y):
    global driverlist

    driverlist +=[[x, y]]
    coordinate = {'x': x, 'y': y}
    return render(request, 'index.html', {'coordinate': coordinate})

