Projects - Oregon LW301
=======

Retrieve Oregon LW301 data and index for later user
- NGINX reverse proxy incl. echo plugin 
- DNSMASQ for internal DNS, to route oregon data via reverse proxy
- PYTHON/BASH - scripts to push messages from Oregon access logs to rabbitmq
- RABBITMQ - simple queue to distribute messages from NGINX/access logs to logstash 
- LOGSTASH - consume RABBITMQ and publish to elasticsearch instance
- ELASTICSEARCH - index local weather data
- KIBANA - visualize the weather data

