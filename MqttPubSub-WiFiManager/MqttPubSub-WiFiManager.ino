#include <WiFiManager.h>        // Library untuk konfigurasi WiFi
#include <PubSubClient.h>       // Library MQTT

// Konfigurasi WiFi
char mqttServer[40] = "broker.emqx.io";
char mqttPort[6] = "1883";
char mqttUser[40] = "";
char mqttPassword[40] = "";
char mqttTopicPub[40] = "StudyClub/NuurR/Publis";
char mqttTopicSub[40] = "StudyClub/NuurR/Subscribe";

WiFiManager wifiManager;
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

void setup() {
  Serial.begin(115200);

  // Konfigurasi WiFiManager
  wifiManager.autoConnect("Mqtt-Nuur");

  // Mengatur server dan port MQTT
  mqttClient.setServer(mqttServer, atoi(mqttPort));

  // Mengatur callback untuk menerima pesan
  mqttClient.setCallback(callback);
}

void loop() {
  // Jika tidak terhubung ke broker MQTT, coba terhubung
  if (!mqttClient.connected()) {
    reconnectMQTT();
  }

  // Langganan (subscribe) ke topik
  mqttClient.subscribe(mqttTopicSub);

  // Publish pesan pada topik
  mqttClient.publish(mqttTopicPub, "Hello, MQTT ini Firdaus!");

  // Tunggu 5 detik sebelum melakukan publish lagi
  delay(5000);

  // Kirim pesan pada loop()
  mqttClient.loop();
}

void callback(char* topic, byte* payload, unsigned int length) {
  // Menerima pesan dari broker MQTT
  Serial.print("Pesan yang diterima pada topik: ");
  Serial.println(topic);

  Serial.print("Isi pesan: ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnectMQTT() {
  // Loop hingga terhubung ke broker MQTT
  while (!mqttClient.connected()) {
    Serial.println("Terhubung ke broker MQTT...");

    // Jika terhubung, publish pesan ke topik dan tampilkan status
    if (mqttClient.connect("ArduinoClient", mqttUser, mqttPassword)) {
      Serial.println("Terhubung!");
      mqttClient.publish(mqttTopicPub, "Arduino terhubung ke broker MQTT!");
    } else {
      // Jika gagal terhubung, tunggu 2 detik dan coba lagi
      Serial.print("Gagal terhubung ke broker MQTT, coba lagi dalam 2 detik...");
      delay(2000);
    }
  }
}
