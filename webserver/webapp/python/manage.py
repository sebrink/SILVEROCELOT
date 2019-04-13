#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import jwt
import Cookie
import urllib
from os import environ
from datetime import datetime, timedelta
import json

print('Content-type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="MEEP1234", db="webdata")
cursor = conn.cursor()

form = cgi.FieldStorage()

token = None

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
   print('invalid token')
else:
   try:
      print('\r\n')

      decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
      cursor.execute('select * from `User Store` where `User Store`.`UID` = "{}"'.format(decoded.get('username')))
      ret = cursor.fetchall()

      if len(ret) == 0:
         print('invalid token')
         exit()

      if datetime.now() > datetime.strptime(decoded.get('expireDate'), '%Y-%m-%dT%H:%M:%S.%f'):
         print('invalid token')
         exit()


      cursor.execute('select `Display Name`,`Video Name`, `Video Location` from `Video Store` join `User Store` where `User Store`.`UID` = `Video Store`.`UID` and `User Store`.`UID` = "{}"'.format(decoded.get('username')))
      rows = cursor.fetchall()
      for row in rows:
         print("""<video width="320" height="240" poster={} controls>
                  <source src="{}" type="video/mp4">
                  <source src="{}" type="video/webm">
                  Your browser does not support the video tag.
                  </video>""".format(row[2], row[2], row[2]))
         print("""<form action="/python/delete.py" method="get">
                        <button type="submit" name="video" value="{}">Delete</button>
                  </form><br>""".format(row[1]))
         print('User: {} Title: {}'.format(row[0],row[1]))
         print('</br>')

   except KeyError:
      print('\r\n')
      print('invalid token')
