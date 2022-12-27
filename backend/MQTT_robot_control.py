import random
import time

from paho.mqtt import client as mqtt_client
import gpiozero as gz
import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())


state = True
broker = 'broker.hivemq.com'
port = 1883
topic = "/ntnunbuenidh/outputState"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)
        
    client.subscribe("/ntnunbuenidh/state")


def on_message(client, userdata, msg):
    print(msg.payload)
    print(msg.topic+" "+str(msg.payload))
    global state
    if str(msg.payload) == "b'f'":
        state = 11
        print(state)
    if str(msg.payload) == "b'b'":
        state = 22
        print(state)
    if str(msg.payload) == "b'r'":
        state = 33
        print(state)
    if str(msg.payload) == "b'l'":
        state = 44
        print(state)
    if str(msg.payload) == "b's'":
        state = 55
        print(state)

def publish(client):
    msg_count = 0
    global state
    while True:
        if state == 11:
            time.sleep(1)
            msg = "forward"
            print(msg, state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
                kit.motor1.throttle = 1.0
                kit.motor2.throttle = 1.0
            else:
                print(msg)
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            msg_count += 1
            
        if state == 22:
            time.sleep(1)
            msg = "backward"
            print(msg, state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
                kit.motor1.throttle = -1.0
                kit.motor2.throttle = -1.0
            else:
                print(msg)
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            msg_count += 1
        
        if state == 33:
            time.sleep(1)
            msg = "right"
            print(msg, state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
                kit.motor1.throttle = 1.0
                kit.motor2.throttle = -1.0
            else:
                print(msg)
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            msg_count += 1
            
        if state == 44:
            time.sleep(1)
            msg = "left"
            print(msg, state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
                kit.motor1.throttle = -1.0
                kit.motor2.throttle = 1.0
            else:
                print(msg)
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            msg_count += 1
        if state == 55:
            time.sleep(1)
            msg = "stop"
            print(msg, state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
                kit.motor1.throttle = 0.0
                kit.motor2.throttle = 0.0
            else:
                print(msg)
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            msg_count += 1

def run():
    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(broker, port)
    
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
