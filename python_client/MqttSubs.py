import paho.mqtt.client as mqtt

mqttBroker = "broker.emqx.io"
subsTopic = "StudyClub/Restu/Publis"

# Fungsi callback ketika koneksi ke broker MQTT berhasil
def on_connect(client, userdata, flags, rc):
    print("Terhubung ke broker MQTT dengan kode: " + str(rc))
    client.subscribe(subsTopic)  # Langganan ke topik yang diinginkan

# Fungsi callback ketika menerima pesan dari broker MQTT
def on_message(client, userdata, msg):
    print("Pesan diterima pada topik: " + msg.topic)
    print("Isi pesan: " + str(msg.payload.decode()))

# Inisialisasi client MQTT
client = mqtt.Client()

# Mengatur callback functions
client.on_connect = on_connect
client.on_message = on_message

# Menghubungkan ke broker MQTT
client.connect(mqttBroker, 1883, 60)

# Loop forever untuk menerima pesan
client.loop_forever()
