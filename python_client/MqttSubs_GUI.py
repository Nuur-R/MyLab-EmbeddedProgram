import paho.mqtt.client as mqtt
import tkinter as tk

mqttBroker = "broker.emqx.io"
subsTopic = "StudyClub/Restu/Publis"

# Fungsi callback ketika koneksi ke broker MQTT berhasil
def on_connect(client, userdata, flags, rc):
    status_label.config(text='Terhubung ke broker MQTT dengan kode: ' + str(rc))
    client.subscribe(subsTopic)  # Langganan ke topik yang diinginkan

# Fungsi callback ketika menerima pesan dari broker MQTT
def on_message(client, userdata, msg):
    output_text.insert(tk.END, 'Pesan diterima pada topik: ' + msg.topic + '\n')
    output_text.insert(tk.END, 'Isi pesan: ' + str(msg.payload.decode()) + '\n')
    output_text.insert(tk.END, '--------------------------------------\n')
    output_text.see(tk.END)  # Auto-scroll ke bawah

# Inisialisasi client MQTT
client = mqtt.Client()

# Mengatur callback functions
client.on_connect = on_connect
client.on_message = on_message

# Menghubungkan ke broker MQTT
client.connect(mqttBroker, 1883, 60)

# Fungsi untuk keluar dari program
def exit_program():
    client.disconnect()
    root.destroy()

# Membuat tampilan GUI menggunakan Tkinter
root = tk.Tk()
root.title('Aplikasi MQTT Subscriber')

# Label Status
status_label = tk.Label(root, text='Status: ')
status_label.pack()

# Label Topik
topic_label = tk.Label(root, text='Topik: ' + subsTopic)
topic_label.pack()

# Output Text
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Button Keluar
exit_button = tk.Button(root, text='Keluar', command=exit_program)
exit_button.pack()

# Loop untuk menerima pesan dan memperbarui GUI
client.loop_start()
root.mainloop()

# Tutup koneksi MQTT
client.loop_stop()
