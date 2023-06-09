import paho.mqtt.client as mqtt

mqttBroker = "broker.emqx.io"
pubTopic = "StudyClub/Restu/Subscribe"

# Inisialisasi client MQTT
client = mqtt.Client()

# Menghubungkan ke broker MQTT
client.connect(mqttBroker, 1883, 60)

# Mengirim pesan
message = "Ini adalah pesan yang akan dikirim Lewat Python sekali kirim"
client.publish(pubTopic, message)

# Putus koneksi MQTT
client.disconnect()
