print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

while n <= 0:
    n = int(input("n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print()
    print(f"Jumlah baris {i} = {total_baris}")

print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")