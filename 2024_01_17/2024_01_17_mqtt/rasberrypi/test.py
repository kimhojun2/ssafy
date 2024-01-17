import paho.mqtt.publish as publisher

publisher.single("iot","led_on",hostname="127.0.0.1")