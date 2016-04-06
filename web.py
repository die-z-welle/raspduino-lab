#!/usr/bin/python
import paho.mqtt.client as mqtt

client = mqtt.Client()

def write_value(value):
    index_file = open("/var/www/html/index.html", "w")
    index_file.write(value)
    index_file.close()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Web: connected...")
    else:
        print("Web: Error CONNACK code: %d" % (rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Web: Subscribed...")

def on_message(client, userdata, msg):
    print("Web: Topic: " + msg.topic + " Message: " + str(msg.payload))
    write_value(str(msg.payload))
	
def connect_broker():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.connect("localhost")
	
def main():
    connect_broker()    
    client.subscribe("messwerte/test", qos=1)
    client.loop_forever()
    
main()
