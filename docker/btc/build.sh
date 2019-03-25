#! /bin/bash

cflags=$(/usr/bin/mysql_config --cflags)
libs=$(/usr/bin/mysql_config --libs)

cflags=${cflags//\//\\\/}
libs=${libs//\//\\\/}

c="s/INCS =/INCS =${cflags}/g"
l="s/LIBS =/LIBS =${libs}/g"

cd  /src/viabtc/matchengine
sed -i "$c" makefile
sed -i "$l" makefile
make

cd  /src/viabtc/marketprice/
make

cd  /src/viabtc/accesshttp/
make

cd /src/viabtc/accessws
make

cd /src/viabtc/alertcenter
make

cd /src/viabtc/readhistory
sed -i "$c" makefile
sed -i "$l" makefile
make
