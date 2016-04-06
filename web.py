#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import paho.mqtt.client as mqtt

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

def write_value(value):
    index_file = open("index.html", "w")
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
    print("Web: Serving at port ", PORT)
    httpd.serve_forever()
    
    client.subscribe("messwerte/test", qos=1)
    client.loop_forever()
    
main()