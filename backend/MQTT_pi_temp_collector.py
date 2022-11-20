import random
import time

from paho.mqtt import client as mqtt_client
import gpiozero as gz


state = True
broker = 'broker.hivemq.com'
port = 1883
topic = "/ntnunbuenidh/CPUtemp"
# generate client ID with pub prefix randomly
#client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

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
    if str(msg.payload) == "b'on'":
        state = True
        print(state)
    if str(msg.payload) == "b'off'":
        state = False
        print(state)

def publish(client):
    msg_count = 0
    global state
    while True:
        if state == True:
            time.sleep(1)
            c_temp = gz.CPUTemperature().temperature
            c_temp = round(c_temp, 1)
            msg = c_temp
            print("rr", state)
        
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(msg)
            else:
                print(msg)
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
