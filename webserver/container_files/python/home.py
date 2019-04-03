#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import jwt
import Cookie
import urllib
from os import environ
import json

print('Content-type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="MEEP1234", db="webdata")
cursor = conn.cursor()

form = cgi.FieldStorage()

token = None

if environ.has_key('HTTP_COOKIE'):
   for cookie in os.environ['HTTP_COOKIE'].split('; '):
      (key, value ) = cookie.split('=');
      if key == "session":
         token = value


session = None

if 'HTTP_COOKIE' in os.environ:
   cookie_string=os.environ.get('HTTP_COOKIE')
   c=Cookie.SimpleCookie()
   c.load(cookie_string)

   try:
      session=c['session'].value
   except KeyError:
      pass

if session is None:
   print('\r\n')
   print('invlaid token')
else:
   try:
      decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
      print('\r\n')	 

      cursor.execute('select `Display Name`,`Video Name`, `Video Location` from `Video Store` join `User Store` where `User Store`.`UID` = `Video Store`.`UID`')
      rows = cursor.fetchall()
      for row in rows:
         print("""<video width="320" height="240" poster={} controls>
                  <source src="{}" type="video/mp4">
                  <source src="{}" type="video/webm">
                  Your browser does not support the video tag.
                  </video></br>""".format(row[2], row[2], row[2]))
         print('User: {} Title: {}'.format(row[0],row[1]))
         print('</br>')
    
   except KeyError:
      print('\r\n')
      print('invalid token') 
