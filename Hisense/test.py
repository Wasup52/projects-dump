import paho.mqtt.client as mqtt

client = mqtt.Client("hisensetv")

host = "192.168.1.12"
host = "broker.hivemq.com"

client.connect(host, 1883)

client.publish("test", "test")