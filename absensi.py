import csv
from datetime import datetime
import os

class Absensi:
    def __init__(self, filename="data_absensi.csv"):
        self.filename = filename

        # Kalau file belum ada → buat header
        if not os.path.exists(filename):
            with open(self.filename, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["NIM", "Nama", "Waktu"])

    def catat(self, nim, nama):
        # Simpan waktu absensi
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nim, nama, waktu])

    def get_records(self):
        # Ambil seluruh isi CSV
        if not os.path.exists(self.filename):
            return []

        records = []
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                if len(row) == 3:
                    records.append(tuple(row))

        return records
