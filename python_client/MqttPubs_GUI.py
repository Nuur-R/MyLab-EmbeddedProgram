import tkinter as tk
import paho.mqtt.client as mqtt

mqttBroker = "broker.emqx.io"
pubTopic = "StudyClub/Restu/Subscribe"

# Fungsi untuk mengirim pesan
def send_message():
    message = message_entry.get()
    client.publish(pubTopic, message)

# Inisialisasi client MQTT
client = mqtt.Client()

# Menghubungkan ke broker MQTT
client.connect(mqttBroker, 1883, 60)

# Fungsi untuk keluar dari program
def exit_program():
    client.disconnect()
    root.destroy()

# Membuat tampilan GUI menggunakan Tkinter
root = tk.Tk()
root.title('Aplikasi MQTT Publisher')

# Label Topik
topic_label = tk.Label(root, text='Topik: ' + pubTopic)
topic_label.pack()

# Entry Pesan
message_label = tk.Label(root, text='Pesan:')
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

# Button Kirim
send_button = tk.Button(root, text='Kirim', command=send_message)
send_button.pack()

# Button Keluar
exit_button = tk.Button(root, text='Keluar', command=exit_program)
exit_button.pack()

# Menjalankan GUI
root.mainloop()

# Tutup koneksi MQTT
client.disconnect()
