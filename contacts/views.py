from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
@login_required
def index(req):
    return render(req, 'contacts/index.html')


@login_required
def createContact(req):
    pass



@login_required
def readContact(req):
    pass


@login_required
def updateContact(req):
    pass


@login_required
def deleteContact(req):
    pass