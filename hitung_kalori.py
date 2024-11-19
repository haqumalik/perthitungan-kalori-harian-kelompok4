


# Input kebutuhan kalori harian pengguna berdasarkan jenis kelamin dan usia
def kebutuhan_kalori(usia, jenis_kelamin):
    if jenis_kelamin.lower() == "pria":
        if usia < 18:
            return 2400
        elif 18 <= usia <= 40:
            return 2500
        elif 41 <= usia <= 65:
            return 2300
        else:
            return 2000
    elif jenis_kelamin.lower() == "wanita":
        if usia < 18:
            return 2000
        elif 18 <= usia <= 40:
            return 2200
        elif 41 <= usia <= 65:
            return 2000
        else:
            return 1800
    else:
        return 0

# Program utama
def hitung_kalori_harian():
    print("Selamat datang di program perhitungan kalori harian!")
    
    # Input data pengguna
    nama = input("Masukkan nama Anda: ")
    usia = int(input("Masukkan usia Anda: "))
    jenis_kelamin = input("Masukkan jenis kelamin Anda (pria/wanita): ")

    # Hitung kebutuhan kalori harian
    kalori_harian = kebutuhan_kalori(usia, jenis_kelamin)
    
    if kalori_harian == 0:
        print("Jenis kelamin tidak valid. Silakan coba lagi.")
        return
    
    print(f"\n{nama}, kebutuhan kalori harian Anda adalah {kalori_harian} kcal.")
    
    total_kalori = 0

    # Input makanan yang dikonsumsi
    while True:
        makanan = input("\nMasukkan makanan yang Anda konsumsi dalam sehari (atau ketik 'selesai' jika sudah): ").lower()
        
        if makanan == "selesai":
            break
        
        if makanan in dm:
            total_kalori += dm[makanan]
            print(f"{makanan.capitalize()} ditambahkan dengan {dm[makanan]} kcal.")
        else:
            print("Maaf, makanan tidak ditemukan dalam daftar.")

    # Hasil perhitungan total kalori
    print(f"\nTotal kalori yang Anda konsumsi hari ini adalah {total_kalori} kcal.")

    # Evaluasi konsumsi kalori
    if total_kalori < kalori_harian:
        print("Konsumsi kalori Anda masih kurang dari kebutuhan harian.")
    elif total_kalori == kalori_harian:
        print("Konsumsi kalori Anda sesuai dengan kebutuhan harian.")
    else:
        print("Konsumsi kalori Anda melebihi kebutuhan harian.")

# Panggil program
hitung_kalori_harian()
