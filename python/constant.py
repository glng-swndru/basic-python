# Di Python, tidak ada konsep "constant" yang secara bawaan dideklarasikan seperti di beberapa bahasa pemrograman lain. Namun, ada praktik umum yang digunakan untuk menunjukkan bahwa suatu variabel adalah konstan, yaitu dengan menggunakan huruf kapital untuk nama variabel tersebut.
# contohnya:
PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458  # dalam meter per detik

# Dalam contoh di atas:
# PI, GRAVITY, dan SPEED_OF_LIGHT diharapkan menjadi konstanta, artinya nilainya tidak diubah selama program berjalan.
# Prinsip:
# Meskipun secara konvensi variabel yang ditulis dengan huruf kapital dianggap sebagai konstanta, Python tidak memaksa atau melindungi nilai-nilai ini dari perubahan. Artinya, Anda masih bisa mengubah nilai dari variabel yang seharusnya konstan tersebut, tetapi ini tidak dianjurkan.

# kita juga bisa memakai pustaka standar python seperti `Final` dari `typing`
# Contohnya:
from typing import Final

PI: Final = 3.14
print("pi: %f" % (PI)) # outputnya -> pi: 3.14000
