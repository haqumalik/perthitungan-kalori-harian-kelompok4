import json
import os
import time
from datetime import datetime
from modul_kalori import CalorieCalculator
from modul_makanan import FoodSystem
from modul_riwayat import HistorySystem


class UserSystem:
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
            
            print("=== Selamat Datang di Calorie Tracker===")
            pilihan = input(" (1) Login\n (2) Register\nPilih 1 atau 2 : ").strip()
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
                print("Tunggu sebentar...")
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
        tinggi_badan = float(input("Masukkan tinggi badan Anda (cm): "))
        berat_badan = float(input("Masukkan berat badan Anda (kg): "))
        aktivitas = int(input("Pilihan tingkat aktivitas :\n 1. Sangat ringan (tidak aktif)\n 2. Ringan (aktivitas ringan/sedikit olahraga)\n 3. Sedang (olahraga 3-5 hari/minggu)\n 4. Berat (olahraga 6-7 hari/minggu)\n 5. Sangat berat (dua kali sehari atau pekerjaan fisik)\n Masukkan tingkat aktivitas Anda (1-5) :"))
        password = input("Buat password: ").strip()

        self.user_data[username] = {
            "nama": nama,
            "jenis_kelamin": jenis_kelamin,
            "usia": usia,
            "tinggi_badan": tinggi_badan,
            "berat_badan": berat_badan,
            "aktivitas": aktivitas,
            "password": password,
            "riwayat_makanan": {}
        }
        self.simpan_riwayat()
        print(f"Akun dengan username {username} berhasil dibuat!")
        os.system("cls")
        print("Tunggu sebentar...")
        time.sleep(2)
        os.system("cls")
        return username

    def edit_biodata(self):
        print("\n=== Edit Biodata ===")
        user_info = self.user_data[self.current_user]

        # Menampilkan biodata saat ini
        print(f"Nama: {user_info['nama']}")
        print(f"Jenis Kelamin: {user_info['jenis_kelamin']}")
        print(f"Usia: {user_info['usia']}")
        print(f"Tinggi Badan: {user_info['tinggi_badan']} cm")
        print(f"Berat Badan: {user_info['berat_badan']} kg")
        print(f"Tingkat Aktivitas: {user_info['aktivitas']}")

        # Mengedit biodata
        user_info['nama'] = input("Masukkan nama baru (tekan enter untuk tetap): ") or user_info['nama']
        jenis_kelamin = input("Masukkan jenis kelamin baru (L/P, tekan enter untuk tetap): ").strip().upper()
        if jenis_kelamin in ['L', 'P']:
            user_info['jenis_kelamin'] = jenis_kelamin
        usia = input("Masukkan usia baru (tekan enter untuk tetap): ")
        if usia.isdigit():
            user_info['usia'] = int(usia)
        tinggi_badan = input("Masukkan tinggi badan baru (cm, tekan enter untuk tetap): ")
        if tinggi_badan.replace('.', '', 1).isdigit():
            user_info['tinggi_badan'] = float(tinggi_badan)
        berat_badan = input("Masukkan berat badan baru (kg, tekan enter untuk tetap): ")
        if berat_badan.replace('.', '', 1).isdigit():
            user_info['berat_badan'] = float(berat_badan)
        aktivitas = input("Pilihan tingkat aktivitas :\n 1. Sangat ringan (tidak aktif)\n 2. Ringan (aktivitas ringan/sedikit olahraga)\n 3. Sedang (olahraga 3-5 hari/minggu)\n 4. Berat (olahraga 6-7 hari/minggu)\n 5. Sangat berat (dua kali sehari atau pekerjaan fisik)\n Masukkan tingkat aktivitas Anda (1-5) :")
        if aktivitas.isdigit() and 1 <= int(aktivitas) <= 5:
            user_info['aktivitas'] = int(aktivitas)
            os.system("cls")
            print("tunggu yaa...")
            time.sleep(1)
            os.system("cls")

        self.simpan_riwayat()
        print("Biodata berhasil diperbarui!")
        print(f"Kebutuhan kalori harian Anda: {CalorieCalculator.hitung_kebutuhan_kalori(jenis_kelamin, (usia), (tinggi_badan), (berat_badan), (aktivitas))}")
    

    def akses_sistem(self):
        food_system = FoodSystem("data.json", self.riwayat_file)
        history_system = HistorySystem(self.user_data)

        while True:
            username = self.login_or_register()
            if not username:
                continue

            user_info = self.user_data[username]
            user_info['kebutuhan_kalori_harian'] = CalorieCalculator.hitung_kebutuhan_kalori(
                user_info["jenis_kelamin"],
                user_info["usia"],
                user_info["tinggi_badan"],
                user_info["berat_badan"],
                user_info["aktivitas"]
            )
            print(f"Kebutuhan kalori harian Anda: {user_info['kebutuhan_kalori_harian']:.2f} kkal")

            while self.current_user:
                print("\n=== Menu Utama ===")
                print("1. Input makanan")
                print("2. Lihat riwayat makanan")
                print("3. Edit biodata")
                print("4. Logout")
                pilihan = input("Pilih menu: ").strip()

                if pilihan == "1":
                    os.system("cls")
                    print("tunggu yaa...")
                    time.sleep(1)
                    os.system("cls")
                    food_system.input_makanan(self.user_data, self.current_user)
                elif pilihan == "2":
                    os.system("cls")
                    print("tunggu yaa...")
                    time.sleep(1)
                    os.system("cls")
                    history_system.lihat_riwayat(self.current_user)
                elif pilihan == "3":
                    os.system("cls")
                    print("tunggu yaa...")
                    time.sleep(1)
                    os.system("cls")
                    self.edit_biodata()
                elif pilihan == "4":
                    os.system("cls")
                    print("tunggu yaa...")
                    time.sleep(1)
                    os.system("cls")
                    self.logout()
                else:
                    print("Pilihan tidak valid.")

    def logout(self):
        print(f"Logout berhasil. Sampai jumpa!, {self.user_data[self.current_user]['nama']}!")
        self.current_user = None