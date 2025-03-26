# GameTebakAngka
Permainan sederhana di mana pemain mencoba menebak angka yang telah dipilih secara acak oleh komputer dalam rentang 1 hingga 100.

**Cara bermain:**
- Komputer memilih angka secara acak.
- Pemain memasukkan angka tebakan.
- Program memberikan petunjuk apakah tebakan terlalu kecil atau terlalu besar.
- Pemain terus menebak hingga menemukan angka yang benar.
- Setelah berhasil, program menampilkan jumlah percobaan serta riwayat tebakan pemain.
  
**Fitur dalam game:**
-	Validasi input (memastikan input berupa angka dan dalam rentang 1-100)
-	Menyimpan riwayat tebakan dalam list
-	Menggunakan perulangan while agar game terus berjalan hingga pemain menang
-	Menampilkan jumlah percobaan saat pemain berhasil menebak angka

-----------------------------------------------------------------------------------------
**Penjelasan Code :**

import random  # Library untuk menghasilkan angka acak

import time  # Library untuk memberikan jeda waktu


  def game_tebak_angka():
    print("\n=== GAME TEBAK ANGKA ===")
    print("Saya telah memilih angka antara 1 hingga 100. Coba tebak!")  
    angka_rahasia = random.randint(1, 100)  # Komputer memilih angka acak antara 1 hingga 100
    percobaan = 0  # Variabel untuk menyimpan jumlah percobaan yang dilakukan pemain
    riwayat_tebakan = []  # Struktur data: list untuk menyimpan semua tebakan pemain
    
    while True:  # Loop utama game yang terus berjalan hingga angka benar ditebak
        try:
            tebakan = int(input("Masukkan tebakanmu: "))  # Meminta input angka dari pengguna
            if tebakan < 1 or tebakan > 100:  # Memeriksa apakah angka berada dalam rentang yang benar
                print("Harap masukkan angka antara 1 hingga 100!\n")
                continue  # Kembali ke awal loop jika angka tidak valid
            
            percobaan += 1  # Menambah jumlah percobaan setiap kali pengguna menebak
            riwayat_tebakan.append(tebakan)  # Menyimpan tebakan pengguna dalam list
            
            if tebakan < angka_rahasia:  # Jika tebakan terlalu kecil
                print("Terlalu kecil! Coba lagi.\n")
            elif tebakan > angka_rahasia:  # Jika tebakan terlalu besar
                print("Terlalu besar! Coba lagi.\n")
            else:  # Jika tebakan benar
                print(f"Selamat! Kamu menebak angka {angka_rahasia} dengan {percobaan} percobaan.")
                print("Riwayat tebakanmu:", riwayat_tebakan)  # Menampilkan semua angka yang telah ditebak
                break  # Keluar dari loop karena angka sudah ditebak dengan benar
        except ValueError:  # Menangani kesalahan jika input bukan angka
            print("Masukkan angka yang valid!\n")
    
    print("Terima kasih sudah bermain!")
    time.sleep(2)  # Memberikan jeda 2 detik sebelum program selesai
    game_tebak_angka()  # Memanggil fungsi utama untuk menjalankan game

-----------------------------------------------------------------------------------------------

**Penjelasan Konsep dalam Program:**
1. Struktur Kontrol :
-	while True untuk mengulang permainan sampai angka benar ditebak.
-	if-elif-else untuk mengevaluasi tebakan pengguna.
-	try-except untuk menangani kesalahan input.
2. Struktur Data:
-	list (riwayat_tebakan) untuk menyimpan semua angka yang ditebak pengguna.
3. Library:
-	random untuk memilih angka acak.
-	time.sleep(2) untuk memberi jeda sebelum keluar dari program.
