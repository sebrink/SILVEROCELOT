#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import jwt
import Cookie
import urllib
import subprocess
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

      cursor.execute('select `Video Location` from `Video Store` where `Video Store`.`UID` = "{}" and `Video Store`.`Video Name` = "{}"'.format(decoded.get('username'), form['video'].value))
      rows = cursor.fetchall()
      try:
         subprocess.Popen('rm /var/www/html/videos/{}_{}'.format(decoded.get('username'), form['video'].value), shell=True)

         cursor.execute('delete from `Video Store` where `Video Store`.`UID` = "{}" and `Video Store`.`Video Name` = "{}"'.format(decoded.get('username'), form['video'].value))
         conn.commit()
      except Exception:
         pass

      print('<meta http-equiv="refresh" content="1; URL=\'/html/manage.html\'" />')
   except KeyError:
      print('\r\n')
      print('invalid token')
