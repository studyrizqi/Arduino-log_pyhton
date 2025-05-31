import serial
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Buka koneksi ke Arduino
ser = serial.Serial('COM4', 9600, timeout=1)

# Buat file CSV dan tulis header
csv_file = 'log_gas.csv'
df = pd.DataFrame(columns=["Waktu", "NilaiGas"])
df.to_csv(csv_file, index=False)

# Inisialisasi grafik
plt.ion()
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot_date(x_data, y_data, '-', label="Sensor Gas")

try:
    while True:
        if ser.in_waiting:
            data = ser.readline().decode().strip()
            if data.isdigit():
                nilai = int(data)
                waktu = datetime.now()

                # Simpan ke CSV
                df_temp = pd.DataFrame([[waktu, nilai]], columns=["Waktu", "NilaiGas"])
                df_temp.to_csv(csv_file, mode='a', index=False, header=False)

                # Update data grafik
                x_data.append(waktu)
                y_data.append(nilai)

                ax.clear()
                ax.plot(x_data[-20:], y_data[-20:], '-o')  # Tampilkan 20 data terakhir
                ax.set_title("Grafik Gas MQ2 Real-Time")
                ax.set_xlabel("Waktu")
                ax.set_ylabel("Nilai Sensor")
                plt.pause(0.1)

except KeyboardInterrupt:
    print("Program dihentikan.")

finally:
    ser.close()
