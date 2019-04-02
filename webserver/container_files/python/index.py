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
   print('Status: 302 Not Found')
   print('Location: /html/login.html')
   print('\r\n')
   print('<!doctype html>')
   print('<html lang=en>')
   print(' <head>')
   print('  <title>Redirect</title>')
   print(' </head>')
   print(' <body>')
   print('  redirecto seato cuz. Hit the button if not automatically redirected...')
   print('<form action="/html/login.php">')
   print('<input type="submit" value="Redirect..." />')
   print('</form>')
   print(' </body>')
   print('</html>');
else:
   try:
      decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
      print('\r\n')	 
      print('<!doctype html>')
      print('<html lang=en>')
      print(' <head>')
      print('  <title>You are logged in</title>')
      print(' </head>')
      print(' <body>')
      print('Welcome back ' + decoded.get('username') + '!')
      print(' </body>')
      print('</html>');
   except KeyError:
      print('Status: 302 Found')
      print('Location: /html/login.html')
      print('\r\n')
      print('<!doctype html>')
      print('<html lang=en>')
      print(' <head>')
      print('  <title>Redirect</title>')
      print(' </head>')
      print(' <body>')
      print('  redirecto seato cuz. Hit the button if not automatically redirected...')
      print('<form action="/html/login.php">')
      print('<input type="submit" value="Redirect..." />')
      print('</form>')
      print(' </body>')
      print('</html>');
   
