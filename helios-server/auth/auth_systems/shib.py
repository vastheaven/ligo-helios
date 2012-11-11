"""
Google Authentication

"""

from django.http import *
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings

import sys, os, cgi, urllib, urllib2, re
import json
import urlparse
from xml.etree import ElementTree

from openid import view_helpers

# some parameters to indicate that status updating is not possible
STATUS_UPDATES = False

# display tweaks
LOGIN_MESSAGE = "Log in with my LIGO Account"

user_data ={}

# FIXME!
# TRUST_ROOT = 'http://localhost:8000'
# RETURN_TO = 'http://localhost:8000/auth/after'

def get_auth_url(request, redirect_url):
  url = 'https://gravity.astro.cf.ac.uk/secure/helios-login.php?redirect_url='+redirect_url
  #url = redirect_url
  #print url  
  return url

def get_user_info_after_auth(request):
  name = request.GET.get('name', '')
  uid = request.GET.get('uid','')
  email = request.GET.get('email','')
  #data = json.load(urllib2.urlopen('https://gravity.astro.cf.ac.uk/secure/helios-getuserinfo.php'))
  return {'type' : 'shib', 'user_id': uid, 'name': name, 'info': {'email': email}, 'token':{}}
    
def do_logout(user):
  """
  logout of Google
  """
  return None
  
def update_status(token, message):
  """
  simple update
  """
  pass

def send_message(user_id, name, user_info, subject, body):
  """
  send email to google users. user_id is the email for google.
  """
  send_mail(subject, body, settings.SERVER_EMAIL, ["%s <%s>" % (name, user_id)], fail_silently=False)
  
def check_constraint(constraint, user_info):
  """
  for eligibility
  """
  pass
