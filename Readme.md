# Kelompok 4 Kelas C  

## Anggota Kelompok :
1. **Nathania Dyah Prameswari** (I0324093)  
2. **Salwa Ani Faiqoh** (I0324102)  
3. **Haqu Malik Umar** (I0324105)  
4. **Muhammad Anassakti Keswahyupi** (I0324118)  

## Tema: Perhitungan Kalori Harian  

### Deskripsi Singkat:
Sistem ini dirancang untuk membantu pengguna menghitung kebutuhan kalori harian berdasarkan parameter tertentu, seperti usia, jenis kelamin, dan juga tingkat aktivitas yang dilakukan. Selain itu, pengguna dapat menginput makanan (dalam gram) ataupun minuman (dalam ml) yang dikonsumsi dan sistem akan mengakumulasi total kalori pada hari tersebut dan akan memperingatkan lebih atau kurangnya kalori yang dibutuhkan, sehingga sistem dapat merekam dan menyimpan riwayat makanan atau minuman yang dikonsumsi. 

### Fitur:
- **Menginput makanan atau minuman** yang dikonsumsi dalam sehari dan kalorinya per (gram/ml) (disimpan di JSON).  
- **Menyimpan history makanan per hari** di file JSON untuk pelacakan kalori.

---
**Flowchart Perhitungan Kalori Harian**
![Flowchart Perhitungan Kalori Harian drawio](https://github.com/user-attachments/assets/74a190ee-337d-4594-b537-994adece6ce7)


### Cara menggunakan:
Mulai(start) : sistem dimulai dengan menu login
- kemudian akan muncul laman login dengan 2 pilihan
- input pilihan
- jika memilih tidak, program akan meminta user untuk menginput data diri, selanjutnya sistem akan membuat akun dan menyimpan data user ke dalam database, setelah berhasil, user akan lanjut ke langkah berikutnya untuk menghitung total kalori harian
- jika memilih ya, program akan meminta user untuk memasukan username dan password yang telah dibuat, jika validasi berhasil, user akan dilanjutkan ke sistem menghitung total kalori harian, jika validasi gagal, user akan kembali ke menu login
- Setelah login berhasil, sistem akan menghitung kebutuhan kalori harian sesuai data diri yang dimasukkan
- kemudian sistem akan menampilkan menu utama dengan 3 pilihan
- Jika memilih pilihan 1(menginput makanan yang dikonsumsi), user akan diminta memasukan nama makanan dan jumlahnya (gram), kemudian sistem kaan menyimpannya ke dalam database, sistem akan menanyakan kembali apakah user ingin menambahkan makanan kembali, jika ya, sistem akan mengulangi sistem menginput nama makanan, jika tidak, sistem akan menyimpan riwayat konsumsi harian
- jika memilih pilihan 2(riwayat makanan), sistem akan menampilkan riwayat konsumsi makanan harian
- jika memilih pilihan 3(logout), sistem akan keluar dari akun user.
Selesai(End): mengakhiri sistem bekerja
