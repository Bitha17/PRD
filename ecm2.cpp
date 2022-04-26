#include <WiFi.h>
#include <HTTPClient.h>

#include "EmonLib.h"
EnergyMonitor emon1;

// Replace with your SSID and Password
const char* ssid     = "TbtVIB";
const char* password = "Gen1:2728";

String server = "http://maker.ifttt.com";
String eventName = "ctsensor_readings";
String IFTTT_Key = "bSyhpab4AIYwIs3zjzF00r289jih-zXax6c7eKV4eDZ";
String IFTTTUrl="http://maker.ifttt.com/trigger/ctsensor_readings/json/with/key/bSyhpab4AIYwIs3zjzF00r289jih-zXax6c7eKV4eDZ";

float value1;
float value2;

void setup() {
  Serial.begin(115200);
  emon1.current(34, 10.5);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Viola, Connected !!!");
}



void sendDataToSheet(void)
{
  String url = server + "/trigger/" + eventName + "/with/key/" + IFTTT_Key + "?value1=" + String((float)value1) + "&value2="+String((float)value2);  
  Serial.println(url);
  //Start to send data to IFTTT`
  HTTPClient http;
  Serial.print("[HTTP] begin...\n");
  http.begin(url); //HTTP

  Serial.print("[HTTP] GET...\n");
  // start connection and send HTTP header
  int httpCode = http.GET();
  // httpCode will be negative on error
  if(httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
    Serial.printf("[HTTP] GET... code: %d\n", httpCode);
    // file found at server
    if(httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(payload);
    }
  } else {
    Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }
  http.end();

}

void loop() {
  float I_total = 0; 
  float P_total = 0;
  for (int i = 0; i < 1800; i++){
    float I = emon1.calcIrms(1480);
    float P = I * 220.0;
    delay(1000);
    I_total = I_total + I;
    P_total = P_total + P;
  }

  value2 = I_total / 1800.0;
  value1 = P_total; 
  
  Serial.print("Values are ");
  Serial.print(value1);
  Serial.print(' ');
  Serial.print(value2);
  Serial.print(' ');
  sendDataToSheet();
  
}