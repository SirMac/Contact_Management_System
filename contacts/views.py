from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error, success
from django.db.models import Q
from django.urls import reverse
from .contactValidators import ValidateContact
from .utils import addNewContact, doUpdateContact, getAllContacts
from .models import Contact
import logging



@login_required
def index(req):
    return readContact(req)
    


@login_required
def createContact(req):
    if req.method == 'GET':
        return render(req, 'contacts/addContact.html')
    
    return addNewContact(req)



@login_required
def readContact(req):
    readAllContacts = req.GET.get('readall')

    if readAllContacts is None:
        return render(req, 'contacts/index.html')
    

    if readAllContacts.lower() == 'yes':
        contacts = getAllContacts()
        if contacts is None:
            logging.error('No contact found.')
            error(req, message='No contact found.')
            return render(req, 'contacts/index.html')
        
        context = {'contacts': contacts}
        return render(req, 'contacts/index.html', context=context)
            

    firstname = req.GET.get('firstname')
    lastname = req.GET.get('lastname')
    email = req.GET.get('email')


    if len(firstname)==0 and len(lastname)==0 and len(email)==0:
        logging.error('Provide at least one input')
        error(req, message='Provide at least one input')
        return redirect('contacts:index')
    
    
    contacts = Contact.objects.filter(
        Q(firstName__iexact=firstname) |
        Q(lastName__iexact=lastname) |
        Q(email__iexact=email) 
    )
        
    if len(contacts) == 0:
        logging.warning('No record found')
        error(req, message='No record found')
        return redirect('contacts:index')

    context = {'contacts': contacts}
    return render(req, 'contacts/index.html', context=context)
    
    
    

@login_required
def updateContact(req, id):
    if req.method == 'GET':
        if not req.session.get('urlref'):
            req.session['urlref'] = req.META.get('HTTP_REFERER')
        contact = get_object_or_404(Contact, pk=id)
        context = {'contact': contact}
        return render(req, 'contacts/updateContact.html', context=context)

    return doUpdateContact(req, id)    



@login_required
def deleteContact(req, id):
    try:
        contact = Contact.objects.get(pk=id)
    except (KeyError, Contact.DoesNotExist):
        logging.error(KeyError)
        error(req, message='Contact delete failed. Try again')
    else:
        success(req, message='Contact deleted successfully')
        contact.delete()
    return redirect(req.META.get('HTTP_REFERER'))



@login_required
def viewDetail(req, id):
    contact = get_object_or_404(Contact, pk=id)
    context = {'contact': contact}
    return render(req, 'contacts/detail.html', context=context)



# ----------- Utils ----------------
