from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact
import logging
import re

class ValidateContact:
    
  def __init__(self, userData):
    self.errorMessages = []
    self.firstName = userData['firstname']
    self.lastName = userData['lastname']
    self.company = userData['company']
    self.phone = userData['phone']
    self.email = userData['email']
    self.website = userData['website']
    self.unitNumber = userData['unitNumber']
    self.civicNumber = userData['civicNumber']
    self.street = userData['street']
    self.city = userData['city']
    self.province = userData['province']
    self.postalCode = userData['postalCode']
    self.validateEmail()
    self.validatePhoneNumber()
    self.validateWebsite()
    self.validateNumber()
    self.validateProvince()
    self.validatePostalCode()
      

  def checkDuplicate(self):
    try:
      Contact.objects.get(email=self.email)
    except (KeyError, Contact.DoesNotExist):
      return False
    else:
      return True
  

  def validatePhoneNumber(self):
    message = "Phone number must be in the format: '+1 (111) 111-1111'"
    phoneRegex = r'^\+1\s\(\d{3}\)\s\d{3}-\d{4}$'
    matchedPhoneNumber = re.search(phoneRegex, self.phone)
    if matchedPhoneNumber == None:
      logging.error(message)
      self.errorMessages.append(message)


  def validateWebsite(self):
    message = "Website must be in the format: 'http(s)://x.x'"
    websiteRegex = r'^https?://\w+\.\w+$'
    matchedWebsite = re.search(websiteRegex, self.website)
    if matchedWebsite == None:
      logging.error(message)
      self.errorMessages.append(message)


  def validateEmail(self):
    message = 'Email address invalid'
    try:
      validate_email(self.email) 
    except ValidationError as e:
      logging.error(str(e))
      self.errorMessages.append(message)


  def validateNumber(self):
    if not self.civicNumber.isnumeric():
      logging.error('Civic number must be numeic')
      self.errorMessages.append('Civic number must be numeic')

    if not self.unitNumber.isnumeric():
      logging.error('Unit number must be numeic')
      self.errorMessages.append('Unit number must be numeic')

    
  def validateProvince(self):
    message = 'Province must be two letters'
    provinceRegex = r'^[a-zA-Z]{2}'
    matchedProvince = re.search(provinceRegex, self.province)
    if matchedProvince == None:
      logging.error(message)
      self.errorMessages.append(message)  
    

  def validatePostalCode(self):
    message = 'Postal code must be in the format 1A1 or A1A'
    postalCode_regex = r'^[a-zA-Z0-9]{3}'
    matchedPostalCode = re.search(postalCode_regex, self.postalCode)
    if matchedPostalCode == None:
      logging.error(message)
      self.errorMessages.append(message)
    