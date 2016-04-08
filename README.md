# raspduino-lab
"Challenge Projekte 2": Arduino Sensor-Reading to Raspberry-Broker Lab

## Setup
Prerequisites:

    mosquitto
    mosquitto-clients
    python
    npm
    nodejs
  
python libraries setup:

    pip install nanpy
    pip install paho.mqtt.client
  
npm libraries setup:

    npm install --prefix /usr/lib nodejs-websocket
  
## Run the application

Step 1:
  Wire up everything

Step 2 - run publisher:

    python publisher.py

Step 3 - run subscribers:

    python lcd.py
    python led.py
    node webserver.js
  
Step 4 - open index.html in preferred browser (adjust socket-address if necessary)
