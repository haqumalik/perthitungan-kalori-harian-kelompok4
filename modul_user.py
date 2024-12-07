import json
import os
import time

class UserManager:
    def __init__(self, riwayat_file):
        self.riwayat_file = riwayat_file
        self.user_data = {}
        self.current_user = None
        self.load_riwayat()

    def load_riwayat(self):
        if os.path.exists(self.riwayat_file):
            with open(self.riwayat_file, "r") as file:
                self.user_data = json.load(file)
        else:
            self.user_data = {}

    def simpan_riwayat(self):
        with open(self.riwayat_file, "w") as file:
            json.dump(self.user_data, file, indent=4)

    def login_or_register(self):
        while True:
            print("=== Menu Login atau Register ===")
            pilihan = input("Pilih (1) Login (2) Register: ").strip()
            if pilihan == "1":
                os.system("cls")
                print("memuat login...")
                time.sleep(2)
                os.system("cls")
                username = self.login()
                if username:
                    return username
            elif pilihan == "2":
                username = self.register()
                return username
            else:
                print("Pilihan tidak valid. Silakan pilih (1) atau (2).")

    def login(self):
        print("=== Login ===")
        username = input("Masukkan username: ").strip()
        if username in self.user_data:
            for _ in range(3):
                password = input("Masukkan password: ").strip()
                if self.user_data[username]["password"] == password:
                    os.system("cls")
                    print("login berhasil")
                    time.sleep(2)
                    os.system("cls")
                    print(f"Selamat datang kembali, {self.user_data[username]['nama']}!")
                    self.current_user = username
                    return username
                else:
                    print("Password salah. Silakan coba lagi.")
            print("Anda telah gagal login 3 kali. Silakan coba lagi nanti.")
            return None
        else:
            print(f"Username {username} tidak ditemukan.")
            pilihan = input("Apakah Anda ingin membuat akun baru? (ya/tidak): ").strip().lower()
            if pilihan == "ya":
                return self.register(username)
            else:
                print("Silakan coba login dengan username lain.")
                return None

    def register(self, username=None):
        if not username:
            username = input("Masukkan username yang ingin digunakan: ").strip()
        nama = input("Masukkan nama Anda: ").strip()
        jenis_kelamin = input("Masukkan jenis kelamin Anda (L/P): ").strip().upper()
        usia = int(input("Masukkan usia Anda (tahun): "))
        password = input("Buat password: ").strip()

        self.user_data[username] = {
            "nama": nama,
            "jenis_kelamin": jenis_kelamin,
            "usia": usia,
            "password": password,
            "riwayat_makanan": {}
        }
        self.simpan_riwayat()
        print(f"Akun dengan username {username} berhasil dibuat!")
        return username