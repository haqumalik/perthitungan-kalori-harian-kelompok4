from modul_user import UserSystem

def main():
    user_system = UserSystem("riwayat_makanan.json")
    user_system.akses_sistem()

# Jalankan program
if __name__ == "__main__":
    main()