import time,json
import paho.mqtt.client as mqtt_client
content = str({
    'id':1,
    "packet_no":126,
    "temperature":30,
    "humidity":60,
    "tds":1100,
    "pH":5.0
})
# setting callbacks for events :connect, publish, subscribe
# this callback print message about connecting status
def on_connect(client,userdata,flags,rc,properties = None):
    print("connected with result code :"+str(rc))
# this callback print message when your publishing was successful
def on_publish(client,userdat,mid,properties = None):
    print("published: "+str(mid))
# print which topic was subscribed to
def on_subscribe(client,userdata,mid,granted_qos,properties=None):
    print("subscribed: "+str(mid)+" "+str(granted_qos))
# print message that was sent back to client
def on_message(client,userdata,message):
    print("message: "+message.topic+" "+str(message.qos)+" "+str(message.payload))
#initialize client
client = mqtt_client.Client(client_id="dinhhieune",userdata=None,protocol=mqtt_client.MQTTv5)
client.on_connect = on_connect
client.connect("broker.mqttdashboard.com",1883)
#assign callbacks
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
#subscribe to all topics of encyclopedia
client.subscribe("iot",qos=1)
#publish content to mqtt broker
client.publish("iot",payload=content,qos=1)
client.loop_forever()
