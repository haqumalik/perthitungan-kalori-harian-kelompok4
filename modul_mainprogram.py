from modul_user import UserManager
from modul_kalori import KaloriManager
from modul_makanan import MakananManager
from modul_riwayat import RiwayatManager

def main():
    riwayat_file = "riwayat_makanan.json"
    database_makanan = "data.json"

    # Inisialisasi manajer pengguna
    user_manager = UserManager(riwayat_file)

    # Akses sistem
    while True:
        username = user_manager.login_or_register()
        if not username:
            continue

        user_info = user_manager.user_data[username]
        kalori_manager = KaloriManager()
        kebutuhan_kalori_harian = kalori_manager.hitung_kebutuhan_kalori(user_info["jenis_kelamin"], user_info["usia"])
        print(f"Kebutuhan kalori harian Anda: {kebutuhan_kalori_harian} kkal")

        makanan_manager = MakananManager(database_makanan, riwayat_file, user_manager.user_data, username)
        riwayat_manager = RiwayatManager(user_manager.user_data, username)

        while user_manager.current_user:
            print("\n=== Menu Utama ===")
            print("1. Input makanan")
            print("2. Lihat riwayat makanan")
            print("3. Logout")
            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                makanan_manager.input_makanan()
            elif pilihan == "2":
                riwayat_manager.lihat_riwayat()
            elif pilihan == "3":
                print(f"Logout berhasil. Sampai jumpa!, {user_manager.user_data[username]['nama']}!")
                user_manager.current_user = None
            else:
                print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()