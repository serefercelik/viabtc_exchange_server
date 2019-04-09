#!/bin/bash
MYSQL_ROOT_PASSWORD="root"

#!/bin/bash
echo "file0 and file1 yazdırılıyor."
mysql -uroot -p$MYSQL_ROOT_PASSWORD <<EOF
source $WORK_PATH/$FILE_0;
source $WORK_PATH/$FILE_1;
EOF
#
echo "file0 and file1 bitti."

sh /docker-entrypoint-initdb.d/init_trade_history.sh1
