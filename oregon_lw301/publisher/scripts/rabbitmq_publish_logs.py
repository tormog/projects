#!/usr/bin/env python
import argparse
import pika
import sys

parser = argparse.ArgumentParser(description='Publish to rabbitmq')
parser.add_argument('--host', default='192.168.10.10', help='Hostname to rabbitmq')
parser.add_argument('--port', default=25672, type=int, help='Port to rabbitmq')
parser.add_argument('--queue', default='es', help='Queuename to publish to')
args = parser.parse_args()

print "Publishing to host:%s port:%s queue:%s" % (args.host,args.port,args.queue)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=args.host,port=args.port))
channel = connection.channel()

channel.queue_declare(queue=args.queue)
while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break
    if not line:
        break
    channel.basic_publish(exchange='',routing_key=args.queue,body=line) 
    print "Published to queue ",args.queue 

connection.close()

