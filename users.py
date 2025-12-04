import csv
import os

class UserSystem:
    def __init__(self, filename="users.csv"):
        self.filename = filename

        if not os.path.exists(filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["username", "password"])

    def register(self, username, password):
        if not username.strip() or not password.strip():
            return False, "Username dan password tidak boleh kosong!"

        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if not row:      # ← FIX baris kosong
                    continue
                if row[0] == username:
                    return False, "Username sudah dipakai."

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])

        return True, "Registrasi berhasil!"

    def login(self, username, password):
        if not username.strip() or not password.strip():
            return False, "Username dan password tidak boleh kosong!"

        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if not row:      # ← FIX baris kosong
                    continue
                if row[0] == username and row[1] == password:
                    return True, "Login berhasil!"

        return False, "Username atau password salah."
