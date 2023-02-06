from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def List(req):
    return HttpResponse('<h1>Hotel Add</h1>')

def Add(r):
    context = {}
    context['username'] = 'Asd@yahoo.com'
    return render(r, 'rooms.html', context)