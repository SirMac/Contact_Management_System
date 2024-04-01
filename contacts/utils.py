from django.shortcuts import render, redirect
from django.contrib.messages import error, success
from django.urls import reverse
from .contactValidators import ValidateContact
from .models import Contact
import logging

def addNewContact(req):
    firstName = req.POST['firstname']
    lastName = req.POST['lastname']
    company = req.POST['company']
    phone = req.POST['phone']
    email = req.POST['email']
    website = req.POST['website']
    unitNumber = req.POST['unitNumber']
    civicNumber = req.POST['civicNumber']
    street = req.POST['street']
    city = req.POST['city']
    province = req.POST['province']
    postalCode = req.POST['postalCode']


    validContact = ValidateContact(req.POST)

    if validContact.checkDuplicate():
        message = f'Email ({email}) already exists'
        logging.warning(message)
        error(request=req, message=message)
        return redirect('contacts:createContact')

    
    messages = validContact.errorMessages
    
    if messages:
        for message in messages:
            logging.error(message)
            error(request=req, message=message)
        return redirect('contacts:createContact')


    contact = Contact(
        firstName = firstName, 
        lastName = lastName, 
        company = company, 
        phone = phone, 
        email = email, 
        website = website, 
        unitNumber = unitNumber, 
        civicNumber = civicNumber, 
        street = street, 
        city = city, 
        province = province.upper(), 
        postalCode = postalCode.upper()
    )
    contact.save()
    return redirect('contacts:index')





def doUpdateContact(req, id):
    firstName = req.POST['firstname']
    lastName = req.POST['lastname']
    company = req.POST['company']
    phone = req.POST['phone']
    email = req.POST['email']
    website = req.POST['website']
    unitNumber = req.POST['unitNumber']
    civicNumber = req.POST['civicNumber']
    street = req.POST['street']
    city = req.POST['city']
    province = req.POST['province']
    postalCode = req.POST['postalCode']

    referer = req.session['urlref']

    validContact = ValidateContact(req.POST)
    messages = validContact.errorMessages
    
    if messages:
        for message in messages:
            logging.error(message)
            error(request=req, message=message)
        return redirect(reverse('contacts:updateContact', args=(id,)))


    try:
        contact = Contact.objects.get(pk=id)
    except (KeyError, Contact.DoesNotExist):
        logging.error(KeyError)
        error(req, message='Update failed. Try again.')
        return render(req, 'contacts/updateContact.html')
    else:
        contact.firstName = firstName
        contact.lastName = lastName
        contact.company = company
        contact.phone = phone
        contact.email = email
        contact.website = website
        contact.unitNumber = unitNumber
        contact.civicNumber = civicNumber
        contact.street = street
        contact.city = city
        contact.province = province
        contact.postalCode = postalCode
        contact.save()

    del req.session['urlref']
    success(req, message='Contact updated successfully')
    return redirect(referer)






def getAllContacts():
    try:
        contacts = Contact.objects.all()
    except (KeyError, Contact.DoesNotExist):
        return None
    else:
        return contacts
            
