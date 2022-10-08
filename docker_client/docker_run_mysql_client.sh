#!/bin/sh
docker run -it --network host --rm mysql mysql -h127.0.0.1 -uroot -prootpass
