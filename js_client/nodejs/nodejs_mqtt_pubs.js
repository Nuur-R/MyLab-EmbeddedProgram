const mqtt = require('mqtt');

const mqttBroker = 'mqtt://broker.emqx.io';
const pubTopic = 'StudyClub/Restu/Publis';

// Membuat koneksi ke broker MQTT
const client = mqtt.connect(mqttBroker);

// Fungsi callback ketika koneksi berhasil
client.on('connect', () => {
  console.log('Terhubung ke broker MQTT');
});

// Handle error jika terjadi masalah
client.on('error', (error) => {
  console.error('Error:', error);
});

// Handle event ketika client disconnect
client.on('disconnect', () => {
  console.log('Terputus dari broker MQTT');
});

// Handle event ketika client close
client.on('close', () => {
  console.log('Koneksi MQTT ditutup');
});

// Handle event ketika client reconnect
client.on('reconnect', () => {
  console.log('Menghubungkan ulang ke broker MQTT...');
});

// Handle event ketika client offline
client.on('offline', () => {
  console.log('Klien offline');
});

// Fungsi untuk mengirim data ke broker MQTT
function publishMessage(payload) {
  client.publish(pubTopic, payload);
  console.log('Pesan terkirim:', payload);
}

// Contoh penggunaan
publishMessage('Hello, MQTT!');
