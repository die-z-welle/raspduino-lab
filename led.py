#!/usr/bin/python
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

LED_PIN = 16

#MQTT Client
client = mqtt.Client()

def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("LED: connected...")
    else:
        print("LED: Error CONNACK code: %d" % (rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("LED: Subscribed...")

def on_message(client, userdata, msg):
    print("LED: Topic: " + msg.topic + " Message: " + str(msg.payload))
    if int(msg.payload) > 50:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
	
def connect_broker():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.connect("localhost")
	
def main():
    gpio_init()
    connect_broker()

    client.subscribe("messwerte/test", qos=1)
    client.loop_forever()
	
    GPIO.cleanup()

main()
