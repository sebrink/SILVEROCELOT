#!/usr/bin/python

import cgi
import MySQLdb
import jwt
import Cookie
import os
import json
from hashlib import sha256

session = None

if 'HTTP_COOKIE' in os.environ:
   #print('GOT COOKIES YALL')
   cookie_string=os.environ.get('HTTP_COOKIE')
   c=Cookie.SimpleCookie()
   c.load(cookie_string)

   try:
      session=c['session'].value
   except KeyError:
      pass

print('Content-Type: text/html')

if session is None:
   print('\r\n')
   print('invlaid token')
else:
   try:
      decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
      print('\r\n')	 
      print(decoded)
   except KeyError:
      print('\r\n')
      print('invalid token')   
