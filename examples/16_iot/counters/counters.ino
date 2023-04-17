

#include <SPI.h>
#include <WiFi.h>

char ssid[] = ""; //  your network SSID (name)
char pass[] = "";    // your network password (use for WPA, or use as key for WEP)

// example.com - for debugging purposes
// IPAddress server(93, 184, 216, 34);
//char server[] = "www.example.com";
// int port = 80;

// aws counters REST service
// IPAddress awsserver(3, 15, 207, 203);
//char server[] = "www.example.com";
//int awsport = 8081;

IPAddress server(51, 105, 124, 161);
int port = 8080;

int status = WL_IDLE_STATUS;

WiFiClient client;

const int DISCONNECTED = 0;
const int CONNECTED = 1;
int state = DISCONNECTED;

void printWifiStatus() {

  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

int redcnt = 0;
int greencnt = 0;

int pushhandled = 0;
byte debug = 0;

void printcnts () {
  Serial.print(redcnt);
  Serial.print(":");
  Serial.print(greencnt);
  Serial.println();
}


void blink (int n) {

  for (int i = 0; i < n; i++) {

    digitalWrite(8, LOW);
    delay(250);
    digitalWrite(8, HIGH);
    delay(250);
  }

}
void setup() {

  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, INPUT);
  pinMode(6, INPUT);
  pinMode(5, INPUT);
  pinMode(3, INPUT);

  blink(10);

  // check for the presence of the shield:
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv != "1.1.0") {
    Serial.println("Upgrade firmware");
  }

  int i = 0;
  while ((status != WL_CONNECTED) && (i < 3)) {

    Serial.print("Connecting to SSID [");
    Serial.print(i);
    Serial.print("] ");
    Serial.println(ssid);

    status = WiFi.begin(ssid, pass);

    delay(10000); // wait 10 seconds for connection:
    i++;
  }

  if (status == WL_CONNECTED) {
    Serial.println("Connected to wifi");
    printWifiStatus();
    state = CONNECTED;
  } else {
    Serial.println("Not connected to wifi");
  }

  blink(10);
  if (state == CONNECTED) {
    // doGet();
    // delay(5000);
    doGet();
    delay(5000);
  }
}

void loop() {

  while (client.available()) {
    char c = client.read();
    Serial.write(c);
  }

  int resetbtn = digitalRead(9);
  int redbtn = digitalRead(6);
  int greenbtn = digitalRead(5);
  int sendbtn = digitalRead(3);

  if ((resetbtn == LOW) && (redbtn == LOW) &&
      (greenbtn == LOW) && (sendbtn == LOW)) {

    pushhandled = 0;
  }

  if ((resetbtn == HIGH) && (!pushhandled)) {
    Serial.println("\nRESET");
    redcnt = 0;
    greencnt = 0;
    printcnts (); 
    blink(10);
    pushhandled = 1;
  }

  if ((redbtn == HIGH) && (!pushhandled)) {
    Serial.println("\nRED");
    redcnt++;
    printcnts (); 
    blink(2);
    pushhandled = 1;
  }

  if ((greenbtn == HIGH) && (!pushhandled)) {
    Serial.println("\nGREEN");
    greencnt++;
    printcnts (); 
    blink(2);
    pushhandled = 1;
  }

  if ((sendbtn == HIGH) && (!pushhandled)) {
    Serial.println("\nSEND");
    digitalWrite(8, LOW);

    if (state == CONNECTED) {
      doPut();
      delay(5000);
    }

    pushhandled = 1;
    digitalWrite(8, HIGH);
  }

  // if the server's disconnected, stop the client:
  // if (!client.connected()) {
  //  Serial.println();
  //  Serial.println("disconnecting from server.");
  //  client.stop();
}

void doGet() {

  client.stop();

  Serial.println("\ndoGet - Connecting to server...");
  if (client.connect(server, port)) {
    Serial.println("connected to server");
    // Make a HTTP request:
    client.println("GET /counters HTTP/1.1");
    client.println("Accept: application/json");
    //client.println("Host: ec2-3-19-66-128.us-east-2.compute.amazonaws.com");
    //client.println("Host: localhost");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Unable to connect to server");
  }
}

String jsonred = "{\"red\":";
String jsongreen = ",\"green\":";
String jsonend = "}";

void doPut() {

  client.stop();

  String json = jsonred;
  String clen = "Content-length: ";

  json.concat(redcnt);
  json.concat(jsongreen);
  json.concat(greencnt);
  json.concat("}");
  clen.concat(json.length());

  Serial.println("JSON");
  Serial.println(json);
  Serial.println("CLEN");
  Serial.println(clen);

  Serial.println("\ndoPut - Connecting to server...");
  if (client.connect(server, port)) {
    Serial.println("connected to server");

    // Make a HTTP request:
    client.println("PUT /counters HTTP/1.1");
    client.println("Host: smartoceanlin01.westeurope.cloudapp.azure.com");
    client.println("Content-type: application/json");
    client.println(clen); // FIXME
    client.println("Connection: close");
    client.println();

    client.println(json);
    client.println();

    client.println();
  } else {
    Serial.println("Unable to connect to server");
  }
}

void doGetExample() {

  client.stop();

  Serial.println("\ndoGet - Connecting to server...");
  if (client.connect(server, port)) {
    Serial.println("connected to server");
    // Make a HTTP request:
    client.println("GET /index.html HTTP/1.1");
    client.println("Host: www.example.com");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Unable to connect to server");
  }
}
