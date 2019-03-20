#!/usr/bin/python

import cgi
import MySQLdb
from hashlib import sha256

form = cgi.FieldStorage()

print('Content-Type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="MEEP1234", db="webdata")
cursor = conn.cursor()

username = form.getvalue('username')
password = sha256(str(form.getvalue('password'))).hexdigest()
displayName = form.getvalue('displayName')

cursor.execute('select `UID` from `User Store` where `UID` = "{}"'.format(username))

ret = cursor.fetchall()

if len(ret) > 0:
	print('Already Exists')
else:
	cursor.execute('insert into `User Store` (`UID`, `Password`, `Display Name`) values ("{}", "{}", "{}")'.format(username, password, displayName))
	conn.commit()
	print('User Created')
