#!/usr/bin/python
import paho.mqtt.client as mqtt
import time

#MQTT Client
client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher: connected...")
    else:
        print("Publisher: Error CONNACK code: %d" % (rc))

def on_publish(client, userdata, mid):
    print("Publisher: published message with id -> " + str(mid))

def connect_broker():
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect("localhost")

def main():
    connect_broker()
    value = 0
    try:
        client.loop_start()
        while True:
            client.publish("messwerte/test", str(value), qos=1)
            value += 1
            time.sleep(5)
    except:
        client.loop_stop()
        print("Publisher: stoped")
        
main()
