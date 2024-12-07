class KaloriManager:
    def hitung_kebutuhan_kalori(self, jenis_kelamin, usia):
        if jenis_kelamin == "L":
            return 2500 - (10 * (usia // 10))
        elif jenis_kelamin == "P":
            return 2000 - (8 * (usia // 10))
        return 2000