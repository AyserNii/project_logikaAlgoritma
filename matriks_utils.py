
def cetak_garis(panjang=50):
    print("=" * panjang)

def input_ordo(nama_matriks):
    """
    Mengambil input ordo (baris dan kolom) untuk matriks
    dengan validasi memastikan bilangan bulat positif.
    """
    while True:
        try:
            baris = int(input(f"Masukkan jumlah baris {nama_matriks}: "))
            kolom = int(input(f"Masukkan jumlah kolom {nama_matriks}: "))
            if baris <= 0 or kolom <= 0:
                print("[!] Jumlah baris dan kolom harus lebih dari 0. Silakan coba lagi.\n")
                continue
            return baris, kolom
        except ValueError:
            print("[!] Masukan harus berupa angka bulat. Silakan coba lagi.\n")

def input_elemen_matriks(nama_matriks, baris, kolom):
    """
    Mengambil input nilai/elemen matriks berdasarkan ordo baris x kolom.
    """
    print(f"\n--- Input Elemen {nama_matriks} ({baris}x{kolom}) ---")
    matriks = []
    for i in range(baris):
        baris_elemen = []
        for j in range(kolom):
            while True:
                try:
                    nilai = float(input(f"Elemen {nama_matriks}[{i + 1}][{j + 1}]: "))
                    # Simpan sebagai int jika nilai tidak memiliki desimal
                    if nilai.is_integer():
                        nilai = int(nilai)
                    baris_elemen.append(nilai)
                    break
                except ValueError:
                    print("  [!] Harap masukkan angka yang valid!")
        matriks.append(baris_elemen)
    return matriks

def tampilkan_matriks(matriks, nama="Matriks"):
    """
    Menampilkan matriks dalam bentuk tabel baris x kolom yang rapi.
    """
    print(f"\n{nama}:")
    for baris in matriks:
        print("[ " + "\t".join(str(elemen) for elemen in baris) + " ]")
