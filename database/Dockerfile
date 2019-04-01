FROM mysql:5.7

COPY setup.sql /mysql/setup.sql
ADD setup.sql /docker-entrypoint-initdb.d
