import json
import os
from datetime import datetime

class MakananManager:
    def __init__(self, database_makanan, riwayat_file, user_data, current_user):
        self.database_makanan = database_makanan
        self.riwayat_file = riwayat_file
        self.user_data = user_data
        self.current_user = current_user
        self.load_makanan()

    def load_makanan(self):
        global data_makan
        if os.path.exists(self.database_makanan):
            with open(self.database_makanan, "r") as file:
                                data_makan = json.load(file)
        else:
            self.data_makanan = {}

    def input_makanan(self):
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

            tipe_item = data_makan["daftar_makanan"][nama_item]["jenis"]
            satuan = "gram" if tipe_item == "makanan" else "ml"

            jumlah = float(input(f"Berapa {satuan} {nama_item} yang dikonsumsi?: "))
            kalori_per_unit = data_makan["daftar_makanan"][nama_item]["kalori"]
            
            # Menghitung total kalori berdasarkan satuan
            total_kalori = (kalori_per_unit * jumlah) / 100

            user_data["riwayat_makanan"][tanggal].append({
                "nama_item": nama_item,
                "tipe": tipe_item,
                "jumlah": jumlah,
                "kalori": total_kalori,
                "satuan": satuan,
            })
            print(f"Kalori untuk {jumlah} {satuan} {nama_item}: {total_kalori:.2f} kkal")

        self.simpan_riwayat()

    def simpan_riwayat(self):
        with open(self.riwayat_file, "w") as file:
            json.dump(self.user_data, file, indent=4)