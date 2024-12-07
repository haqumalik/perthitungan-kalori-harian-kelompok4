from datetime import datetime

class RiwayatManager:
    def __init__(self, user_data, current_user):
        self.user_data = user_data
        self.current_user = current_user

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