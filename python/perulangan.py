# Perulangan di Python

# 1. Perulangan dengan for
# for digunakan untuk iterasi melalui sebuah iterable (seperti list, tuple, string, atau rentang angka)

# Iterasi melalui list
buah = ["apel", "jeruk", "pisang"]
for item in buah:
    print(item)

# Iterasi melalui string
kata = "Python"
for huruf in kata:
    print(huruf)

# Iterasi menggunakan range
for i in range(5):  # Menghasilkan angka dari 0 hingga 4
    print(i)

# Iterasi dengan start, stop, dan step
for i in range(1, 10, 2):  # Menghasilkan angka dari 1 hingga 9 dengan step 2
    print(i)

# Menggunakan for dengan dict
profile = {
    "nama": "Gilang",
    "umur": 23,
    "hobi": ["gaming", "belajar"]
}
for key, value in profile.items():
    print(f"{key}: {value}")

# 2. Perulangan dengan while
# while digunakan untuk iterasi selama kondisi tertentu bernilai True

# Contoh while loop dengan kondisi sederhana
x = 0
while x < 5:
    print(x)
    x += 1  # Increment x

# Contoh while loop dengan break
y = 0
while True:
    if y > 5:
        break
    print(y)
    y += 1

# 3. Perulangan Bersarang (Nested Loops)
# Menggunakan perulangan di dalam perulangan lain

# Nested for loop
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # Untuk baris baru setelah setiap baris inner loop

# Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # Untuk baris baru setelah setiap baris inner loop
    i += 1

# 4. Penggunaan break dan continue
# break digunakan untuk menghentikan loop secara tiba-tiba
# continue digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya

# Contoh break
for i in range(10):
    if i == 5:
        break
    print(i)

# Contoh continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Hanya mencetak angka ganjil

# 5. List Comprehensions
# List comprehensions adalah cara singkat untuk membuat list baru dengan menerapkan kondisi dan ekspresi

# Contoh sederhana list comprehension
angka = [1, 2, 3, 4, 5]
kuadrat = [x**2 for x in angka]
print(kuadrat)

# List comprehension dengan kondisi
genap = [x for x in angka if x % 2 == 0]
print(genap)

# 6. Enumerate
# Fungsi enumerate digunakan untuk mendapatkan indeks dan nilai saat iterasi melalui iterable

daftar = ["a", "b", "c"]
for indeks, nilai in enumerate(daftar):
    print(f"Indeks {indeks}: Nilai {nilai}")

# 7. Zip
# Fungsi zip digunakan untuk menggabungkan beberapa iterable menjadi iterator tuple

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for item1, item2 in zip(list1, list2):
    print(f"{item1} - {item2}")
