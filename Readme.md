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
![Perhitungan_Kalori_Harian drawio 1](https://github.com/user-attachments/assets/346dd914-c6af-4141-805c-df7fa9d1f2fb)



### Cara menggunakan:
Mulai(start) : sistem dimulai dengan menu login
- kemudian akan muncul laman login dengan 2 pilihan yaitu login dan register
- input pilihan
- jika user belum mempunyai akun, program akan meminta user untuk menginput username, password, dan biodata. jika akun telah terbuat, user akan lanjut ke fungsi berikutnya.
- jika user telah memiliki akun, user diminta untuk menginput username dan password yang telah dibuat, jika username dan password telah tervalidasi, user akan lanjut ke fungsi berikutnya.
- Setelah login berhasil, sistem akan menghitung kebutuhan kalori harian sesuai data diri yang dimasukkan
- kemudian sistem akan menampilkan menu utama dengan 3 pilihan
- Jika memilih pilihan 1(menginput makanan yang dikonsumsi), user akan diminta memasukan nama makanan dan jumlahnya (per 100 gram), kemudian sistem akan menyimpannya ke dalam database, sistem akan menanyakan kembali apakah user ingin menambahkan makanan kembali, jika ya, sistem akan mengulangi fungsi menginput nama makanan, jika tidak, sistem akan menyimpan riwayat konsumsi harian dan kembali ke menu utama.
- jika memilih pilihan 2(riwayat makanan), sistem akan menampilkan 3 pilihan kembali. jika memilih pilihan 1(riwayat hari ini), sistem akan menampilkan kalori makanan dan minuman hari ini yang tersimpan di dalam database dan kembali ke menu utama. jika memilih pilihan 2(riwayat tanggal tertentu), user diminta untuk menginput tanggal yang diinginkan dan sistem akan menampilkan tanggal yang telah diinput yang telah tersimpan di dalam database kemudian kembali ke menu utama. jika memilih pilihan 3(seluruh riwayat), sistem akan menampilkan seluruh riwayat kalori makanan yang telah tersimpan di dalam database.
- jika memilih pilihan 3(edit biodata), sistem akan meminta user untuk mengisi biodata yang baru dan akan menyimpan biodata baru ke dalam database.
- jika memilih pilihan 4(logout), sistem akan keluar dari akun user dan kembali ke halaman login.
Selesai(End): mengakhiri sistem bekerja
