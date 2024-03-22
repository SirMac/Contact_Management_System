from django.shortcuts import render
from django.http import HttpResponse





def login(req):
    return render(req, 'login.html')


def index(req):
    return HttpResponse('Index Page')