const mqtt = require('mqtt');

const mqttBroker = 'mqtt://broker.emqx.io';
const subsTopic = 'StudyClub/Restu/Publis';

// Membuat koneksi ke broker MQTT
const client = mqtt.connect(mqttBroker);

// Fungsi callback ketika koneksi berhasil
client.on('connect', () => {
  console.log('Terhubung ke broker MQTT');
  client.subscribe(subsTopic);
});

// Fungsi callback ketika menerima pesan
client.on('message', (topic, message) => {
  console.log('Pesan diterima pada topik:', topic);
  console.log('Isi pesan:', message.toString());
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
