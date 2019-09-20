#!/usr/bin/env bash

db_name="$1"
if [ ${#db_name} -le 3 ]; then echo "DB name not provided!" ; exit
fi
echo "Taking backup of "$1" ........."
pg_dump -U postgres -h 127.0.0.1 -d "$1" -Fc > db_ops/sftms_dump.sql
echo "Finished"