let mqtt;
let reconnectTimeout = 2000;
let host = "broker.hivemq.com";
let port = 8000;

function onConnect() {
    // Once a connection has been made, make a subscription and send a message.

    console.log("Connected ");
    mqtt.subscribe("/ntnunbuenidh/CPUtemp");

    message = new Paho.MQTT.Message("on");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

}

function stop() {
    message = new Paho.MQTT.Message("off");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

    let div = document.getElementById('output');
    div.textContent = " "

}

function start() {
    message = new Paho.MQTT.Message("on");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

}


function onMessageArrived(msg) {
    out_msg = "Topic: " + msg.destinationName + ",   " + msg.payloadString
    console.log(out_msg)

    let div = document.getElementById('output');
    div.innerHTML += out_msg + "<br>"
}


function MQTTconnect() {
    console.log("connecting to " + host + " " + port);

    let x = Math.floor(Math.random() * 10000);
    let cname = "orderform-" + x;

    mqtt = new Paho.MQTT.Client(host, port, cname);

    let options = {
        timeout: 3,
        onSuccess: onConnect
    };

    mqtt.onMessageArrived = onMessageArrived
    mqtt.connect(options); //connect
}

MQTTconnect()