#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>

const char* ssid = "moto";
const char* password = "Monic4#M4dronero";
const char* mqtt_server ="192.168.43.99";
//"192.168.1.7"; //Definir

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[10];
String Val=" ";
int value = 0;
int h=0;
int d=100000;

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  }

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("myoWare")) {
      Serial.println("connected");
      // Subscribe
      client.subscribe("outTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 1 seconds before retrying
      delay(1000);
    }
  }
}
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 10) {
    lastMsg = now;
    h=0;
    d=100000;
   for (int i=0; i<100; i++) {
      value=analogRead(33);
      delay(10);
      if (value > h){
        h=value;
        }
       if (value < d){
        d=value;
        }                   
}
    char datosst[8];
    Val=(String)h+"-"+(String)d;         
    Serial.print("Data: ");
    Serial.println(Val);
    String stringOne = Val;
    char Buf[10];
    stringOne.toCharArray(Buf, 10);
    client.publish("outTopic", Buf);   
  }
}
