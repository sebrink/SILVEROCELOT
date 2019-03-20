FROM ubuntu

EXPOSE 80

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python

RUN apt-get -y install python-mysqldb

RUN a2enmod cgi
RUN service apache2 restart

RUN echo "                       \n \
<Directory /var/www/html>        \n \
   Options +ExecCGI              \n \
   AddHandler cgi-script .py     \n \
   DirectoryIndex html/login.html\n \
</Directory>                     \n \
<Directory /var/www/html/python> \n \
   Options +ExecCGI 		 \n \
   AddHandler cgi-script .py     \n \
</Directory>                     \n \
" >> /etc/apache2/apache2.conf

RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python /usr/local/bin/python

CMD /usr/sbin/apache2ctl -D FOREGROUND
