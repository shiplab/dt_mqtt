let mqtt;
let reconnectTimeout = 2000;
let host = "broker.hivemq.com";
let port = 8000;
let tt =500;

function onConnect() {
    // Once a connection has been made, make a subscription and send a message.

    console.log("Connected ");
    mqtt.subscribe("/ntnunbuenidh/outputState");

    message = new Paho.MQTT.Message("b");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

}

function forward() {
    console.log("forward ");
    message = new Paho.MQTT.Message("f");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

    setTimeout(function() {
        stop();
      }, tt);

    let div = document.getElementById('output');
    div.textContent = " "

}

function backward() {
    console.log("backward ");
    message = new Paho.MQTT.Message("b");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

    setTimeout(function() {
        stop();
      }, tt);

    let div = document.getElementById('output');
    div.textContent = " "

}

function left() {
    console.log("left ");
    message = new Paho.MQTT.Message("l");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

    setTimeout(function() {
        stop();
      }, tt);

    let div = document.getElementById('output');
    div.textContent = " "

}

function right() {
    console.log("right ");
    message = new Paho.MQTT.Message("r");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);

    setTimeout(function() {
        stop();
      }, tt);

    let div = document.getElementById('output');
    div.textContent = " "

}

function stop() {
    message = new Paho.MQTT.Message("s");
    message.destinationName = "/ntnunbuenidh/state";
    mqtt.send(message);
    console.log("stop ");
}

function onMessageArrived(msg) {
    out_msg = "Topic: " +",   " + msg.payloadString
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