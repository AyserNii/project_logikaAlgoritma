# Panduan Belajar & Dokumentasi: Program Operasi Matriks Python

Program ini dirancang secara **modular** (terpisah per file) untuk memudahkan pemahaman konsep **Logika dan Algoritma**, khususnya materi manipulasi **Array 2 Dimensi (Matriks)**.

---

## 📁 Struktur Direktori & Peran File

```text
Project_logikaALgoritma/
│
├── main.py             # File utama pengeksekusi program & navigasi menu
├── matriks_utils.py    # Modul fungsi bantuan (input ordo, input elemen, cetak)
├── pertambahan.py      # Modul logika operasi pertambahan matriks
├── pengurangan.py      # Modul logika operasi pengurangan matriks
├── perkalian.py        # Modul logika operasi perkalian matriks & validasi ordo
└── README.md           # Panduan lengkap materi pembelajaran & kode
```

---

## 📖 Bedah Kode & Penjelasan Tiap File

---

### 1. [matriks_utils.py](file:///c:/Users/Resya%20Anggara/OneDrive/Documents/Project_logikaALgoritma/matriks_utils.py) — Modul Utilitas / Bantuan
File ini memuat fungsi-fungsi umum yang sering dipakai berulang kali (*reusable functions*).

#### a. `input_ordo(nama_matriks)`
* **Fungsi**: Meminta user memasukkan jumlah baris dan kolom secara dinamis (fleksibel).
* **Konsep Logika**:
  * Menggunakan perulangan `while True` dan blok `try-except ValueError` untuk mencegah error saat pengguna tidak sengaja mengetik huruf/simbol alih-alih angka.
  * Memvalidasi bahwa jumlah baris dan kolom harus bilangan positif ($> 0$).
```python
while True:
    try:
        baris = int(input(f"Masukkan jumlah baris {nama_matriks}: "))
        kolom = int(input(f"Masukkan jumlah kolom {nama_matriks}: "))
        if baris <= 0 or kolom <= 0:
            print("[!] Jumlah baris dan kolom harus lebih dari 0.")
            continue
        return baris, kolom
    except ValueError:
        print("[!] Masukan harus berupa angka bulat.")
```

#### b. `input_elemen_matriks(nama_matriks, baris, kolom)`
* **Fungsi**: Mengisi elemen-elemen matriks menggunakan konsep *Nested Loop* (perulangan bersarang).
* **Konsep Logika**:
  * `for i in range(baris)`: Berjalan dari baris ke-1 hingga baris terakhir.
  * `for j in range(kolom)`: Berjalan dari kolom ke-1 hingga kolom terakhir pada baris tersebut.
  * Hasil disimpan dalam bentuk matriks (list of lists di Python): `matriks[i][j]`.

#### c. `tampilkan_matriks(matriks, nama)`
* **Fungsi**: Menampilkan array 2 dimensi ke layar agar berbentuk kotak tabel matriks yang rapi.
* **Konsep Logika**:
  * `"\t".join(...)` menggabungkan setiap angka dalam baris dengan tabulasi agar kolom lurus sejajar.

---

### 2. [pertambahan.py](file:///c:/Users/Resya%20Anggara/OneDrive/Documents/Project_logikaALgoritma/pertambahan.py) — Modul Pertambahan Matriks

#### Syarat Matematika
Dua matriks hanya dapat dijumlahkan jika memiliki **ordo yang sama persis** ($m \times n$).
Rumus:
$$C_{ij} = A_{ij} + B_{ij}$$

#### Penjelasan Fungsi:
1. **`hitung_pertambahan(m1, m2, baris, kolom)`**:
   * Melakukan penjumlahan elemen demi elemen pada posisi index yang sama:
   ```python
   for i in range(baris):
       baris_hasil = []
       for j in range(kolom):
           baris_hasil.append(m1[i][j] + m2[i][j])
       hasil.append(baris_hasil)
   ```
2. **`proses_pertambahan()`**:
   * Memvalidasi ordo:
   ```python
   if b1 != b2 or k1 != k2:
       print("Gagal: Ordo kedua matriks harus sama!")
       return
   ```

---

### 3. [pengurangan.py](file:///c:/Users/Resya%20Anggara/OneDrive/Documents/Project_logikaALgoritma/pengurangan.py) — Modul Pengurangan Matriks

#### Syarat Matematika
Sama seperti pertambahan, ordo kedua matriks harus **sama persis** ($m \times n$).
Rumus:
$$C_{ij} = A_{ij} - B_{ij}$$

#### Penjelasan Fungsi:
1. **`hitung_pengurangan(m1, m2, baris, kolom)`**:
   * Melakukan pengurangan elemen demi elemen:
   ```python
   for i in range(baris):
       baris_hasil = []
       for j in range(kolom):
           baris_hasil.append(m1[i][j] - m2[i][j])
       hasil.append(baris_hasil)
   ```
2. **`proses_pengurangan()`**:
   * Memvalidasi kesamaan ordo Matriks 1 dan Matriks 2 sebelum meminta input elemen.

---

### 4. [perkalian.py](file:///c:/Users/Resya%20Anggara/OneDrive/Documents/Project_logikaALgoritma/perkalian.py) — Modul Perkalian Matriks

#### Syarat Matematika (Sangat Penting)
Perkalian matriks $A \times B$ hanya sah bila:
$$\text{Jumlah Kolom Matriks 1} = \text{Jumlah Baris Matriks 2}$$
Jika Matriks 1 berordo $m \times p$ dan Matriks 2 berordo $p \times n$, hasilnya adalah matriks berordo $m \times n$.
Rumus:
$$C_{ij} = \sum_{k=0}^{p-1} A_{ik} \times B_{kj}$$

#### Penjelasan Kode:
1. **Validasi Ordo**:
   ```python
   # Khusus perkalian, dicek apakah k1 == b2
   if k1 != b2:
       print("[GAGAL VALIDASI PERKALIAN]")
       print(f"Alasan: Kolom Matriks 1 ({k1}) != Baris Matriks 2 ({b2}).")
       return
   ```
2. **`hitung_perkalian(m1, m2, baris1, kolom1, kolom2)`**:
   * Menggunakan perulangan 3 tingkat (*3-level nested loop*):
     * Loop `i`: Menelusuri baris Matriks 1 ($0 \dots \text{baris1}-1$)
     * Loop `j`: Menelusuri kolom Matriks 2 ($0 \dots \text{kolom2}-1$)
     * Loop `k`: Menghitung perkalian baris dengan kolom lalu dijumlahkan (`total += m1[i][k] * m2[k][j]`).
   ```python
   for i in range(baris1):
       baris_hasil = []
       for j in range(kolom2):
           total = 0
           for k in range(kolom1):
               total += m1[i][k] * m2[k][j]
           baris_hasil.append(total)
       hasil.append(baris_hasil)
   ```

---

### 5. [main.py](file:///c:/Users/Resya%20Anggara/OneDrive/Documents/Project_logikaALgoritma/main.py) — File Eksekusi Utama
File ini sengaja dibuat bersih dan ringkas tanpa memuat logika hitung yang rumit. Tugasnya murni:
1. Mengimpor fungsi dari file modul lain:
   ```python
   from pertambahan import proses_pertambahan
   from pengurangan import proses_pengurangan
   from perkalian import proses_perkalian
   ```
2. Menampilkan menu pilihan (1-4).
3. Memanggil modul fungsi yang dipilih oleh pengguna.
4. Menanyakan konfirmasi `(y/n)` apakah pengguna ingin mengulang program.

---

## 🚀 Cara Menjalankan Program

Buka terminal di folder project, lalu ketik perintah:

```bash
python main.py
```

---

## 💡 Rangkuman Konsep untuk Bahan Presentasi / Ujian

| Konsep | Penerapan di Program |
| :--- | :--- |
| **Modularitas** | Memecah fungsi ke file terpisah (`import ... from ...`) agar kode teratur. |
| **Array 2 Dimensi** | Representasi matriks menggunakan list di dalam list (`[[a, b], [c, d]]`). |
| **Nested Loop (Perulangan Bersarang)** | `for i` dan `for j` untuk membaca dan mencetak elemen baris dan kolom. |
| **Perulangan 3 Tingkat** | `for i`, `for j`, `for k` untuk algoritma perkalian baris kali kolom. |
| **Defensive Programming / Validasi** | Penggunaan `try-except` untuk menangani input non-angka dan `if` untuk memeriksa kesesuaian ordo matematika. |
