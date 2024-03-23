from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# @api_view(['GET'])
def loginIndex(req):
    return render(req, 'accounts/login.html')
    


# @api_view(['POST'])
def authenticateUser(req):
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(request=req, username=username, password=password)
    if user is not None:
        login(req, user)
        return redirect('contacts:index')
    else:
        return redirect('users:login')




@api_view(['GET'])
def register(req):
    return render(req, 'accounts/register.html')



@api_view(['POST'])
def registerUser(req):
    pass
    # user = User.save()
    # user.set_password(user.password)
    # user.save()


def logoutUser(req):
    logout(req)
    return redirect('users:login')