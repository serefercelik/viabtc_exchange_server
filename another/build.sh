#! /bin/bash

cflags=$(/usr/bin/mysql_config --cflags)
libs=$(/usr/bin/mysql_config --libs)

cflags=${cflags//\//\\\/}
libs=${libs//\//\\\/}

c="s/INCS =/INCS =${cflags}/g"
l="s/LIBS =/LIBS =${libs}/g"

cd  /src/matchengine
sed -i "$c" makefile
sed -i "$l" makefile
make

cd  /src/marketprice/
make clean
make

cd  /src/accesshttp/
make clean
make

cd /src/accessws
make clean
make

cd /src/alertcenter
make clean
make

cd /src/readhistory
sed -i "$c" makefile
sed -i "$l" makefile
make

