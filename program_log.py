import serial
from datetime import datetime

# Ganti COM3 sesuai dengan port Arduino di komputermu
ser = serial.Serial('COM4', 9600, timeout=1)

print("📡 Mencatat data kadar gas...")

with open("log_gas.txt", "a") as file:
    while True:
        data = ser.readline().decode().strip()
        if data:
            try:
                gas = int(data)
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log = f"{waktu} - Kadar Gas: {gas}"
                print(log)
                file.write(log + "\n")
            except:
                pass  # Abaikan error konversi
