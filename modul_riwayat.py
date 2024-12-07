import os
import time
from datetime import datetime

class HistorySystem:
    def __init__(self, user_data):
        self.user_data = user_data

    def lihat_riwayat(self, current_user):
        print("\n=== Lihat Riwayat Makanan ===")
        riwayat = self.user_data[current_user]["riwayat_makanan"]
        self.current_user = current_user


        if not riwayat:
            print("Belum ada riwayat makanan/minuman.")
            return

        pilihan = input(" (1) Riwayat Hari Ini\n (2) Riwayat Tanggal Tertentu\n (3) Seluruh Riwayat\nPilih 1, 2 atau 3 :").strip()

        if pilihan == "1":
            os.system("cls")
            print("tunggu yaa...")
            time.sleep(1)
            os.system("cls")
            tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
            self.tampilkan_riwayat_per_tanggal(riwayat, tanggal_hari_ini)
        elif pilihan == "2":
            os.system("cls")
            print("tunggu yaa...")
            time.sleep(1)
            os.system("cls")
            tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ").strip()
            os.system("cls")
            print("tunggu yaa...")
            time.sleep(1)
            os.system("cls")
            self.tampilkan_riwayat_per_tanggal(riwayat, tanggal)
        elif pilihan == "3":
            os.system("cls")
            print("tunggu yaa...")
            time.sleep(1)
            os.system("cls")
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