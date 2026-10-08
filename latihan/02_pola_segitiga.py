n = int(input("n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()