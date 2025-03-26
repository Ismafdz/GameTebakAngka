import random
import time

def game_tebak_angka():
    print("\n=== GAME TEBAK ANGKA ===")
    print("Saya telah memilih angka antara 1 hingga 100. Coba tebak!")
    
    angka_rahasia = random.randint(1, 100)  # Komputer memilih angka acak
    percobaan = 0  # Menyimpan jumlah percobaan
    riwayat_tebakan = []  # Struktur data: list untuk menyimpan tebakan sebelumnya
    
    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            if tebakan < 1 or tebakan > 100:
                print("Harap masukkan angka antara 1 hingga 100!\n")
                continue
            
            percobaan += 1
            riwayat_tebakan.append(tebakan)
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba lagi.\n")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba lagi.\n")
            else:
                print(f"Selamat! Kamu menebak angka {angka_rahasia} dengan {percobaan} percobaan.")
                print("Riwayat tebakanmu:", riwayat_tebakan)
                break
        except ValueError:
            print("Masukkan angka yang valid!\n")
    
    print("Terima kasih sudah bermain!")
    time.sleep(2)

game_tebak_angka()
