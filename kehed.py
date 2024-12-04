import json
import os
from datetime import datetime

class SistemKalori:
    def __init__(self):
        self.database_makanan = "data.json"
        self.riwayat_file = "riwayat_makanan.json"
        self.user_data = {}
        self.current_user = None
        self.kebutuhan_kalori_harian = 0
        self.load_riwayat()

    def load_riwayat(self):
        if os.path.exists(self.riwayat_file):
            with open(self.riwayat_file, "r") as file:
                self.user_data = json.load(file)
        else:
            self.user_data = {}

    def load_makanan(self):
        global data_makan
        if os.path.exists(self.database_makanan):
            with open(self.database_makanan, "r") as file:
                data_makan = json.load(file)
        else:
            self.data_makanan = {}
            
    def simpan_riwayat(self):
        with open(self.riwayat_file, "w") as file:
            json.dump(self.user_data, file, indent=4)

    def login_or_register(self):
        while True:
            print("=== Menu Login atau Register ===")
            pilihan = input("Pilih (1) Login (2) Register: ").strip()
            if pilihan == "1":
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

    def hitung_kebutuhan_kalori(self, jenis_kelamin, usia):
        if jenis_kelamin == "L":
            return 2500 - (10 * (usia // 10))
        elif jenis_kelamin == "P":
            return 2000 - (8 * (usia // 10))
        return 2000

    
    def input_makanan(self):
        self.load_makanan()
        print("\n=== Input Makanan/Minuman ===")
        tanggal = datetime.now().strftime("%Y-%m-%d")
        user_data = self.user_data[self.current_user]

        if tanggal not in user_data["riwayat_makanan"]:
            user_data["riwayat_makanan"][tanggal] = []

        while True:
            nama_item = input("Masukkan nama makanan/minuman (ketik 'selesai' untuk keluar): ").strip().lower()
            if nama_item == "selesai":
                break
            
            # Validasi apakah item ada di database
            if nama_item not in data_makan["daftar_makanan"].keys():
                print(f"Item '{nama_item}' tidak ditemukan dalam database. Silakan coba lagi.")
                continue

            # Ambil data item dari database
            # nama_item = data_makan["daftar_makanan"][nama_item]
            
            # Validasi tipe data nama_item (harus berupa dictionary)
            # if not isinstance(nama_item, dict):
            #     print(f"Kesalahan data untuk item '{nama_item}'.")
            #     continue

            tipe_item = data_makan["daftar_makanan"][nama_item]["jenis"]  # Menggunakan 'jenis' untuk menentukan tipe item
            satuan = "gram" if tipe_item == "makanan" else "ml"

            jumlah = float(input(f"Berapa {satuan} {nama_item} yang dikonsumsi?: "))
            kalori_per_unit = data_makan["daftar_makanan"][nama_item]["kalori"]
            
                        # Menghitung total kalori berdasarkan satuan
            if tipe_item == "makanan":
                total_kalori = (kalori_per_unit * jumlah) / 100  # Kalori per 100 gram
            else:  # minuman
                total_kalori = (kalori_per_unit * jumlah) / 100  # Kalori per 100 ml

            user_data["riwayat_makanan"][tanggal].append({
                "nama_item": nama_item,
                "tipe": tipe_item,
                "jumlah": jumlah,
                "kalori": total_kalori,
                "satuan": satuan,
            })
            print(f"Kalori untuk {jumlah} {satuan} {nama_item}: {total_kalori:.2f} kkal")

        self.simpan_riwayat()

    # (kode lainnya tetap sama)

# Jalankan program

    
    def lihat_riwayat(self):
        print("\n=== Lihat Riwayat Makanan ===")
        user_data = self.user_data[self.current_user]
        riwayat = user_data["riwayat_makanan"]

        if not riwayat:
            print("Belum ada riwayat makanan/minuman.")
            return

        pilihan = input("Pilih (1) Riwayat Hari Ini (2) Riwayat Tanggal Tertentu (3) Seluruh Riwayat: ").strip()

        if pilihan == "1":
            tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
            self.tampilkan_riwayat_per_tanggal(riwayat, tanggal_hari_ini)
        elif pilihan == "2":
            tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ").strip()
            self.tampilkan_riwayat_per_tanggal(riwayat, tanggal)
        elif pilihan == "3":
            for tanggal, data_item in riwayat.items():
                print(f"\nTanggal: {tanggal}")
                self.tampilkan_riwayat_per_tanggal(riwayat, tanggal)
        else:
            print("Pilihan tidak valid.")

    def tampilkan_riwayat_per_tanggal(self, riwayat, tanggal):
        if tanggal in riwayat:
            total_kalori_harian = 0
            for item in riwayat[tanggal]:
                print(f"- {item['nama_item'].capitalize()} ({item['tipe']}) - {item['jumlah']} {item['satuan']} - {item['kalori']:.2f} kkal")
                total_kalori_harian += item["kalori"]

            print(f"\nTotal kalori yang dikonsumsi pada {tanggal}: {total_kalori_harian:.2f} kkal\n")
        else:
            print(f"Tidak ada riwayat pada tanggal {tanggal}.")

    def logout(self):
        print(f"Logout berhasil. Sampai jumpa!, {self.user_data[self.current_user]['nama']}!")
        self.current_user = None

    def akses_sistem(self):
        while True:
            username = self.login_or_register()
            if not username:
                continue

            user_info = self.user_data[username]
            self.kebutuhan_kalori_harian = self.hitung_kebutuhan_kalori(user_info["jenis_kelamin"], user_info["usia"])
            print(f"Kebutuhan kalori harian Anda: {self.kebutuhan_kalori_harian} kkal")

            while self.current_user:
                print("\n=== Menu Utama ===")
                print("1. Input makanan")
                print("2. Lihat riwayat makanan")
                print("3. Logout")
                pilihan = input("Pilih menu: ").strip()

                if pilihan == "1":
                    self.input_makanan()
                elif pilihan == "2":
                    self.lihat_riwayat()
                elif pilihan == "3":
                    self.logout()
                else:
                    print("Pilihan tidak valid.")

# Jalankan program
if __name__ == "__main__":
    sistem = SistemKalori()
    sistem.akses_sistem()