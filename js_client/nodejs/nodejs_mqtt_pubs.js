const mqtt = require('mqtt');

const mqttBroker = 'mqtt://broker.emqx.io';
const pubTopic = 'StudyClub/Restu/Publis';

// Membuat koneksi ke broker MQTT
const client = mqtt.connect(mqttBroker);

// Fungsi callback ketika koneksi berhasil
client.on('connect', () => {
  console.log('Terhubung ke broker MQTT');
});

// Fungsi untuk mengirim data ke broker MQTT
function publishMessage(payload) {
  client.publish(pubTopic, payload);
  console.log('Pesan terkirim:', payload);
}

// Contoh penggunaan
publishMessage('Hello, MQTT! ini dari NodeJS nya si daus');
