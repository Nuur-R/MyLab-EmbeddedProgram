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
