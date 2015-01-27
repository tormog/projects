#!/bin/bash

# Simple script to pipe new lines from access log to python publisher script
tail -F /var/log/nginx/access.proxy.log | egrep --line-buffered "POST.*update.*BlackBox" | awk -W interactive '{print "date::"$4" "$5" data::"$13}' | python rabbitmq_publish_logs.py --queue oregon
