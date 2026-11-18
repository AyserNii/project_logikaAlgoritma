from matriks_utils import cetak_garis, input_ordo, input_elemen_matriks, tampilkan_matriks

def hitung_perkalian(m1, m2, baris1, kolom1, kolom2):
    hasil = []
    for i in range(baris1):
        baris_hasil = []
        for j in range(kolom2):
            total = 0
            for k in range(kolom1):
                total += m1[i][k] * m2[k][j]
            baris_hasil.append(total)
        hasil.append(baris_hasil)
    return hasil

def proses_perkalian():
    cetak_garis()
    print(" OPERASI PERKALIAN MATRIKS ".center(50, "="))
    cetak_garis()
    print("Syarat Perkalian: Jumlah Kolom Matriks 1 HARUS sama dengan Jumlah Baris Matriks 2.\n")

    b1, k1 = input_ordo("Matriks 1")
    b2, k2 = input_ordo("Matriks 2")

    # Validasi khusus perkalian sesuai ketentuan soal
    if k1 != b2:
        print("\n" + "!" * 50)
        print("[GAGAL VALIDASI PERKALIAN]")
        print("Operasi perkalian matriks TIDAK DAPAT dilakukan!")
        print(f"Alasan: Kolom Matriks 1 ({k1}) != Baris Matriks 2 ({b2}).")
        print("Syarat perkalian matriks adalah kolom Matriks 1 harus sama dengan baris Matriks 2.")
        print("!" * 50)
        return

    print("\n" + "=" * 50)
    print("[VALIDASI BERHASIL]")
    print(f"Kolom Matriks 1 ({k1}) == Baris Matriks 2 ({b2}).")
    print(f"Matriks hasil nantinya akan berordo: {b1}x{k2}")
    print("=" * 50)

    m1 = input_elemen_matriks("Matriks 1", b1, k1)
    m2 = input_elemen_matriks("Matriks 2", b2, k2)

    tampilkan_matriks(m1, "Matriks 1")
    tampilkan_matriks(m2, "Matriks 2")

    hasil = hitung_perkalian(m1, m2, b1, k1, k2)

    print("\nHasil (Matriks 1 x Matriks 2):")
    tampilkan_matriks(hasil, f"Matriks Hasil ({b1}x{k2})")
