#!/usr/bin/python
import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber: connected...")
    else:
        print("Subscriber: Error CONNACK code: %d" % (rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber: Subscribed...")

def on_message(client, userdata, msg):
    print("Web: Topic: " + msg.topic + " Message: " + str(msg.payload))
	
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
