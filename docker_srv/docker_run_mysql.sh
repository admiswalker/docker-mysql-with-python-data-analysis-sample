#!/bin/sh

docker run --rm --name docker-mysql-5-7 -d \
  -v $PWD/db-5-7:/var/lib/mysql \
  -v $PWD/config:/etc/mysql/conf.d \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=test \
  -e MYSQL_USER=testuser \
  -e MYSQL_PASSWORD=testpass \
  -p 127.0.0.1:3306:3306 \
  -u `id -u`:`id -g` \
  mysql:5.7.37

