# Operator di Python

"""Operator Aritmatika
Operator aritmatika digunakan untuk melakukan operasi matematis seperti penambahan, pengurangan, dll.
"""
# Operasi tambah (+)
num = 2 + 2  # -> 4
# Penanda nilai positif (Unari +)
num = +2  # -> 2
# Operasi pengurangan (-)
num = 4 - 2  # -> 2
# Penanda nilai negatif (Unari -)
num = -2  # -> -2
# Operasi perkalian (*)
num = 3 * 3  # -> 9
# Operasi pembagian (/)
num = 8 / 2  # -> 4.0
# Operasi pembagian dengan hasil dibulatkan ke bawah (//)
num = 10 // 3  # -> 3
# Operasi modulo (pencarian sisa bagi hasil)
num = 7 % 4  # -> 3
# Operasi pangkat (**)
num = 3 ** 2  # -> 9

"""Operasi Assignment
Operator assignment digunakan untuk memberikan nilai ke variabel.
"""
# Penugasan nilai (=)
num = 5  # -> 5
# Penugasan dengan penambahan (+=)
num += 3  # -> 8 (sama dengan num = num + 3)
# Penugasan dengan pengurangan (-=)
num -= 2  # -> 6 (sama dengan num = num - 2)
# Penugasan dengan perkalian (*=)
num *= 2  # -> 12 (sama dengan num = num * 2)
# Penugasan dengan pembagian (/=)
num /= 3  # -> 4.0 (sama dengan num = num / 3)
# Penugasan dengan pembagian yang dibulatkan ke bawah (//=)
num //= 2  # -> 2 (sama dengan num = num // 2)
# Penugasan dengan modulo (%=)
num %= 2  # -> 0 (sama dengan num = num % 2)
# Penugasan dengan pangkat (**=)
num **= 3  # -> 0 (sama dengan num = num ** 3)

"""Operator Perbandingan
Operator perbandingan digunakan untuk membandingkan dua nilai dan mengembalikan nilai boolean (`True` atau `False`).
"""
# Sama dengan (==)
res = 4 == 4  # -> True
res = 4 == "4"  # -> False
# Tidak sama dengan (!=)
res = 4 != 5  # -> True
# Lebih besar dari (>)
res = 4 > 5  # -> False
# Lebih kecil dari (<)
res = 4 < 5  # -> True
# Lebih besar atau sama dengan (>=)
res = 5 >= 5  # -> True
# Lebih kecil atau sama dengan (<=)
res = 4 <= 5  # -> True

"""Operator Logika
Operator logika digunakan untuk operasi logika seperti AND, OR, dan NOT.
"""
# AND logika
res = (4 == 5) and (2 != 3)  # -> False
# OR logika
res = (4 == 5) or (2 != 3)  # -> True
# NOT logika
res = not (2 == 3)  # -> True

"""Operator Bitwise
Operator bitwise bekerja pada level bit untuk melakukan operasi seperti AND, OR, XOR, NOT, dll.
"""
# AND bitwise (&)
res = 4 & 5  # -> 4 (0100 & 0101 = 0100)
# OR bitwise (|)
res = 4 | 5  # -> 5 (0100 | 0101 = 0101)
# XOR bitwise (^)
res = 4 ^ 5  # -> 1 (0100 ^ 0101 = 0001)
# NOT bitwise (~)
res = ~4  # -> -5 (bitwise complement of 4, i.e., -(4+1))
# Left Shift (<<)
res = 4 << 1  # -> 8 (0100 << 1 = 1000)
# Right Shift (>>)
res = 4 >> 1  # -> 2 (0100 >> 1 = 0010)

"""Operator Keanggotaan (Membership Operators)
Operator keanggotaan digunakan untuk menguji apakah elemen tertentu ada dalam kumpulan (seperti list, tuple, atau string).
"""
# Operator 'in'
res = 'a' in 'apple'  # -> True
res = 5 in [1, 2, 3, 4]  # -> False
# Operator 'not in'
res = 'b' not in 'apple'  # -> True

"""Operator Identitas (Identity Operators)
Operator identitas digunakan untuk membandingkan apakah dua variabel menunjuk ke objek yang sama.
"""
# Operator 'is'
a = [1, 2, 3]
b = a
res = a is b  # -> True
# Operator 'is not'
c = a[:]
res = a is not c  # -> True

"""Operator Ternary
Operator ternary digunakan untuk menulis ekspresi kondisional dalam satu baris.
"""
# Bentuk umum: [on_true] if [expression] else [on_false]
num = 5
res = "Greater than 3" if num > 3 else "Less than or equal to 3"
# -> "Greater than 3"