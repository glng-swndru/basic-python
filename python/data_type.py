# Tipe Data di Python

# Numbers
# Integer adalah bilangan bulat
int_num = 10
# Float adalah bilangan desimal
float_num = 10.5
# Complex adalah bilangan kompleks
complex_num = 1 + 2j

print(f"Integer: {int_num}")
print(f"Float: {float_num}")
print(f"Complex: {complex_num}")

# String
# String sebaris
string_1 = "Halo Gilang"
# String multi baris
string_2 = """Selamat
Belajar
Python"""

print(string_1)
print(string_2)

# Boolean
# Boolean hanya memiliki dua nilai: True atau False
bool_1 = True
bool_2 = False
print(f"Boolean 1: {bool_1}")
print(f"Boolean 2: {bool_2}")

# None
# None adalah tipe data khusus yang menunjukkan bahwa variabel tidak memiliki nilai
data = "Hello"
print(f"Data sebelum None: {data}")

data = None
print(f"Data setelah None: {data}")

data = "Python"
print(f"Data setelah diubah: {data}")

# List
# List adalah koleksi yang bersifat mutable (dapat diubah) dan dapat menampung berbagai tipe data
# List dengan elemen integer
list_1 = [2, 4, 8, 16]
# List dengan elemen string
list_2 = ["grayson", "jason", "tim", "damian"]
# List dengan berbagai tipe data
list_3 = [24, False, "Hello Python"]
print(f"Elemen ketiga dari list_2: {list_2[2]}")

# Mengubah elemen pertama dari list_1
list_1[0] = 10
print(f"List 1 setelah perubahan: {list_1}")

# Tuple
# Tuple adalah koleksi yang bersifat immutable (tidak dapat diubah) dan juga dapat menampung berbagai tipe data
# Tuple dengan elemen integer
tuple_1 = (2, 3, 4)
# Tuple dengan elemen string
tuple_2 = ("numenor", "valinor")
# Tuple dengan berbagai tipe data
tuple_3 = (24, False, "Hello Python")
print(f"Elemen pertama dari tuple_2: {tuple_2[0]}")

# Dictionary
# Dictionary adalah koleksi key-value pairs yang memungkinkan pengambilan nilai berdasarkan kunci (key)
profile_1 = {
    "name": "Gilang",
    "is_male": True,
    "age": 23,
    "hobbies": ["Gaming", "Learning"]
}
print(f"Name dari profile_1: {profile_1['name']}")

# Mengecek apakah sebuah key ada di dalam dictionary
is_name = "name" in profile_1
print(f"Apakah key 'name' ada di profile_1? {is_name}")

# Set
# Set adalah koleksi yang tidak mengizinkan elemen duplikat dan tidak menyimpan urutan elemen
set_1 = {"pineapple", "spaghetti"}
print(f"Isi dari set_1: {set_1}")

# Bytes
# Bytes adalah tipe data yang digunakan untuk menyimpan data biner
byte_data = b"Hello"
print(f"Byte data: {byte_data}")

# Penjelasan Tambahan:
# Numbers: Mencakup int, float, dan complex.
# String: Penjelasan tentang string sebaris dan multi baris.
# Boolean: Menjelaskan nilai True dan False.
# None: Contoh penggunaan None.
# List: Contoh list yang bersifat mutable.
# Tuple: Contoh tuple yang bersifat immutable.
# Dictionary: Menyimpan data dalam key-value pairs.
# Set: Menyimpan koleksi data yang unik.
# Bytes: Digunakan untuk data biner.