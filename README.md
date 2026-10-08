# Pertemuan 06 Nested Loop Python

**Algoritma dan Pemrograman | Pertemuan 06**

Nama: Maulyditha Revania A.
NIM: 2225250100
Kelas: 3A

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam pemrograman Python.

## Cara Menjalankan

Program dapat dijalankan menggunakan perintah:

```bash
python3 latihan/01_pasangan_indeks.py
python3 latihan/02_pola_segitiga.py
python3 latihan/03_jumlah_per_baris.py
python3 latihan/04_hitung_pasangan.py
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

### Loop luar

Loop luar menggunakan variabel `i` untuk menentukan baris tabel perkalian dari 1 sampai `n`.

### Loop dalam

Loop dalam menggunakan variabel `j` untuk menentukan kolom dari 1 sampai `n`.

### Akumulator

Variabel `total_baris` digunakan untuk menghitung jumlah hasil perkalian pada setiap baris. Variabel ini direset pada setiap awal baris.

Variabel `total_semua` digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris. Variabel ini tidak direset sampai seluruh proses selesai.

### Counter

Variabel `count_genap` digunakan untuk menghitung banyak hasil perkalian yang bernilai genap. Counter bertambah satu jika `hasil % 2 == 0`.

## Hasil Pengujian

| Input n | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status   |
| ------: | --------------: | ----------: | -----------------: | -------- |
|       1 |               1 |           1 |                  0 | Berhasil |
|       2 |               4 |           9 |                  3 | Berhasil |
|       3 |               9 |          36 |                  5 | Berhasil |

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali dan loop dalam juga berjalan sebanyak `n` kali untuk setiap iterasi loop luar.

Dengan demikian, badan loop dalam berjalan sebanyak:

```text
n × n = n²
```

kali.

Contohnya, jika `n = 3`, maka pernyataan `hasil = i * j` dijalankan sebanyak:

```text
3 × 3 = 9 kali
```

## Refleksi

Salah satu kesalahan yang dapat terjadi pada nested loop adalah meletakkan `total_baris = 0` di luar loop luar. Jika hal tersebut dilakukan, jumlah dari baris sebelumnya akan ikut terbawa ke baris berikutnya.

Perbaikannya adalah meletakkan `total_baris = 0` di dalam loop luar sehingga setiap baris memiliki akumulator sendiri.

## Refleksi Teknis

### 1. Mengapa `total_baris` direset di setiap iterasi loop luar?

Karena `total_baris` digunakan untuk menghitung jumlah hasil pada satu baris saja. Setelah pindah ke baris berikutnya, nilainya harus dimulai kembali dari 0.

### 2. Mengapa `total_semua` tidak direset di setiap baris?

Karena `total_semua` digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris. Jika direset setiap baris, jumlah keseluruhan tidak dapat diperoleh.

### 3. Untuk n, berapa kali pernyataan `hasil = i * j` dieksekusi?

Pernyataan tersebut dieksekusi sebanyak `n²` kali karena terdapat `n` iterasi pada loop luar dan `n` iterasi pada loop dalam.

### 4. Bagaimana membuktikan `count_genap` benar?

Setiap hasil perkalian diperiksa menggunakan kondisi:

```python
if hasil % 2 == 0:
```

Jika hasil habis dibagi 2, berarti hasil tersebut genap dan `count_genap` ditambah satu. Karena setiap pasangan `(i, j)` diperiksa tepat satu kali, setiap hasil genap juga dihitung tepat satu kali.

### 5. Apa bagian program yang paling banyak melakukan operasi ketika n membesar?

Bagian nested loop paling banyak melakukan operasi karena jumlah iterasinya adalah `n²`. Ketika nilai `n` bertambah, jumlah operasi meningkat secara kuadrat.
