import paho.mqtt.client as mqtt #MQTT library for Python
import time                     #Time library for listening time

def message(random_client_name, c, listen_message):       #MQTT message listening function
    print(str(listen_message.payload.decode("utf-8")))

c = mqtt.Client()        #called into "c" MQTT Client 

c.on_message = message   #message function called and started wait

c.connect("broker.mqttdashboard.com")   #Connecting MQTT Broker

c.publish("ev-ev","GEL")                # "GEL" message sent to broker with "ev-ev" topic

c.subscribe("ev-ev-ev")                 # Client is subscribing "ev-ev-ev" topic for listen to message
c.loop_start()                          # Listening Started...
time.sleep(1)                           # 
c.loop_stop()                           # Listening Stopped. 
