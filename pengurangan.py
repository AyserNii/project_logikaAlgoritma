from matriks_utils import cetak_garis, input_ordo, input_elemen_matriks, tampilkan_matriks

def hitung_pengurangan(m1, m2, baris, kolom):
    hasil = []
    for i in range(baris):
        baris_hasil = []
        for j in range(kolom):
            baris_hasil.append(m1[i][j] - m2[i][j])
        hasil.append(baris_hasil)
    return hasil

def proses_pengurangan():
    cetak_garis()
    print(" OPERASI PENGURANGAN MATRIKS ".center(50, "="))
    cetak_garis()
    print("Catatan: Syarat pengurangan matriks adalah ordo kedua matriks harus SAMA.\n")

    b1, k1 = input_ordo("Matriks 1")
    b2, k2 = input_ordo("Matriks 2")

    # Validasi kesamaan ordo
    if b1 != b2 or k1 != k2:
        print("\n[GAGAL VALIDASI]")
        print("Operasi pengurangan tidak dapat dilakukan!")
        print(f"Alasan: Ordo Matriks 1 ({b1}x{k1}) TIDAK SAMA dengan ordo Matriks 2 ({b2}x{k2}).")
        return

    print(f"\n[VALIDASI BERHASIL] Kedua matriks berordo sama ({b1}x{k1}).")

    m1 = input_elemen_matriks("Matriks 1", b1, k1)
    m2 = input_elemen_matriks("Matriks 2", b2, k2)

    tampilkan_matriks(m1, "Matriks 1")
    tampilkan_matriks(m2, "Matriks 2")

    hasil = hitung_pengurangan(m1, m2, b1, k1)

    print("\nHasil (Matriks 1 - Matriks 2):")
    tampilkan_matriks(hasil, f"Matriks Hasil ({b1}x{k1})")
