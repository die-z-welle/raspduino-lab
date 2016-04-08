#!/usr/bin/python
import paho.mqtt.client as mqtt
from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep

client = mqtt.Client()
PIN = 0

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

    connection = SerialManager(device='/dev/ttyACM0')
    a = ArduinoApi(connection=connection)
    a.pinMode(PIN, a.INPUT)

    try:
        client.loop_start()
        while True:
            value = a.analogRead(PIN)
            client.publish("messwerte/test", str(value), qos=1)
            print "value:" + str(value)
            sleep(1)
    except:
        client.loop_stop()
        print("publisher stopped")

main()
