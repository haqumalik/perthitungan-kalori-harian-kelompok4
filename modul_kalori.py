class CalorieCalculator:
    @staticmethod
    def hitung_kebutuhan_kalori(jenis_kelamin, usia, tinggi_badan, berat_badan, aktivitas):
        if jenis_kelamin == "L":
            bmr = 66 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
        elif jenis_kelamin == "P":
            bmr = 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
        else:
            bmr = 2000  # Default jika jenis kelamin tidak valid

        # Faktor aktivitas berdasarkan input 1-5
        faktor_aktivitas = {
            1: 1.2,  # Sangat ringan (tidak aktif)
            2: 1.375,  # Ringan (aktivitas ringan/sedikit olahraga)
            3: 1.55,  # Sedang (olahraga 3-5 hari/minggu)
            4: 1.725,  # Berat (olahraga 6-7 hari/minggu)
            5: 1.9,  # Sangat berat (dua kali sehari atau pekerjaan fisik)
        }

        return bmr * faktor_aktivitas.get(aktivitas, 1.2)  # Default ke faktor 1.2 jika tidak valid