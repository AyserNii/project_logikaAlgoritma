"""
File Utama Program (Running Menu)
Mata Kuliah: Logika & Algoritma
"""

import sys
from matriks_utils import cetak_garis
from pertambahan import proses_pertambahan
from pengurangan import proses_pengurangan
from perkalian import proses_perkalian

def main():
    while True:
        cetak_garis(50)
        print("      PROGRAM OPERASI MATRIKS (LOGIKA & ALGORITMA)      ")
        cetak_garis(50)
        print("1. Pertambahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Keluar")
        cetak_garis(50)

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            proses_pertambahan()
        elif pilihan == "2":
            proses_pengurangan()
        elif pilihan == "3":
            proses_perkalian()
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            sys.exit(0)
        else:
            print("\n[!] Pilihan menu tidak valid. Silakan pilih 1, 2, 3, atau 4.\n")

        print("\n")
        kembali = input("Apakah ingin melakukan operasi lain? (y/n): ").strip().lower()
        if kembali != 'y':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        print("\n")

if __name__ == "__main__":
    main()
