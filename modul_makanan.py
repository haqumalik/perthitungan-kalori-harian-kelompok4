import json
import os
import time
from datetime import datetime

class FoodSystem:
    def __init__(self, database_makanan, riwayat_file):
        self.database_makanan = database_makanan
        self.riwayat_file = riwayat_file
        self.data_makanan = {}
        self.load_makanan()

    def load_makanan(self):
        if os.path.exists(self.database_makanan):
            with open(self.database_makanan, "r") as file:
                self.data_makanan = json.load(file)
        else:
            self.data_makanan = {}

    def input_makanan(self, user_data, current_user):
        print("\n=== Input Makanan/Minuman ===")
        tanggal = datetime.now().strftime("%Y-%m-%d")

        if tanggal not in user_data[current_user]["riwayat_makanan"]:
            user_data[current_user]["riwayat_makanan"][tanggal] = []

        total_kalori_harian = 0  # Inisialisasi total kalori harian

        while True:
            nama_item = input("Masukkan nama makanan/minuman (ketik 'selesai' untuk keluar): ").strip().lower()
            if nama_item == "selesai":
                os.system("cls")
                print("tunggu yaa...")
                time.sleep(1)
                os.system("cls")
                break
            
            # Validasi apakah item ada di database
            if nama_item not in self.data_makanan["daftar_makanan"].keys():
                print(f"Item '{nama_item}' tidak ditemukan dalam database. Silakan coba lagi.")
                continue

            tipe_item = self.data_makanan["daftar_makanan"][nama_item]["jenis"]
            satuan = "gram" if tipe_item == "makanan" else "ml"

            jumlah = float(input(f"Berapa {satuan} {nama_item} yang dikonsumsi?: "))
            kalori_per_unit = self.data_makanan["daftar_makanan"][nama_item]["kalori"]
            
            # Menghitung total kalori berdasarkan satuan
            total_kalori = (kalori_per_unit * jumlah) / 100  # Kalori per 100 gram/ml

            user_data[current_user]["riwayat_makanan"][tanggal].append({
                "nama_item": nama_item,
                "tipe": tipe_item,
                "jumlah": jumlah,
                "kalori": total_kalori,
                "satuan": satuan,
            })
            print(f"Kalori untuk {jumlah} {satuan} {nama_item}: {total_kalori:.2f} kkal")
            total_kalori_harian += total_kalori  # Tambahkan kalori ke total harian

        self.simpan_riwayat(user_data)
        self.peringatan_kalori(total_kalori_harian, user_data[current_user]['kebutuhan_kalori_harian'])

    def simpan_riwayat(self, user_data):
        with open(self.riwayat_file, "w") as file:
            json.dump(user_data, file, indent=4)

    def peringatan_kalori(self, total_kalori_harian, kebutuhan_kalori_harian):
        print(f"\nTotal kalori yang dikonsumsi hari ini: {total_kalori_harian:.2f} kkal")
        if total_kalori_harian < kebutuhan_kalori_harian:
            print(f"Anda masih kurang {kebutuhan_kalori_harian - total_kalori_harian:.2f} kkal dari kebutuhan kalori harian.")
        elif total_kalori_harian > kebutuhan_kalori_harian:
            print(f"Anda telah melebihi kebutuhan kalori harian sebesar {total_kalori_harian - kebutuhan_kalori_harian:.2f} kkal.")
        else:
            print("Anda tepat memenuhi kebutuhan kalori harian Anda.")