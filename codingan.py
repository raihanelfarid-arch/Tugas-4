# Program meminta nama dan menyimpannya ke file guest.txt.

nama = input("Masukkan nama Anda: ")

with open("guest.txt", "w") as file:       #untuk membuka file dengan mode write (menulis)
    file.write(nama)                             #menulis nama ke file

print("Nama berhasil disimpan ke guest.txt")


# Program menyimpan banyak nama menggunakan perulangan while

with open("guest_book.txt", "a") as file:
    while True:
        nama = input("Masukkan nama (ketik 'q' untuk keluar): ")

        if nama.lower() == 'q':
            print("Program selesai.")
            break

        file.write(nama + "\n")

        print(f"Nama {nama} berhasil ditambahkan.")


# Program menjumlahkan dua angka dengan penanganan error

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")

except ValueError:
    print("⚠️ Terjadi kesalahan! Harap masukkan angka yang valid.")




# Program menyimpan banyak nama menggunakan perulangan while

with open("guest_book.txt", "a") as file:
    while True:
        nama = input("Masukkan nama (ketik 'q' untuk keluar): ")

        if nama.lower() == 'q':
            print("Program selesai.")
            break

        file.write(nama + "\n")

        print(f"Nama {nama} berhasil ditambahkan.")   





# program kalkulator sederhana dan unit testing

import math
import unittest

# =========================
# CLASS KALKULATOR
# =========================
class Kalkulator:

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return a / b

    def modulus(self, a, b):
        return a % b

    def pangkat(self, a, b):
        return a ** b

    def akar(self, a):
        if a < 0:
            raise ValueError("Tidak bisa akar dari bilangan negatif")
        return math.sqrt(a)

    def faktorial(self, a):
        if a < 0:
            raise ValueError("Tidak bisa faktorial bilangan negatif")
        return math.factorial(a)


# =========================
# PROGRAM UTAMA 
# =========================
def main():
    k = Kalkulator()

    print("=== Kalkulator ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Modulus")
    print("6. Pangkat")
    print("7. Akar")
    print("8. Faktorial")

    pilihan = input("Pilih operasi (1-8): ")

    try:
        if pilihan in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
        elif pilihan in ["7", "8"]:
            a = float(input("Masukkan angka: "))
        else:
            print("Pilihan tidak valid")
            return

        if pilihan == "1":
            print("Hasil:", k.tambah(a, b))
        elif pilihan == "2":
            print("Hasil:", k.kurang(a, b))
        elif pilihan == "3":
            print("Hasil:", k.kali(a, b))
        elif pilihan == "4":
            print("Hasil:", k.bagi(a, b))
        elif pilihan == "5":
            print("Hasil:", k.modulus(a, b))
        elif pilihan == "6":
            print("Hasil:", k.pangkat(a, b))
        elif pilihan == "7":
            print("Hasil:", k.akar(a))
        elif pilihan == "8":
            print("Hasil:", k.faktorial(int(a)))

    except ValueError as e:
        print("Error:", e)


# =========================
# UNIT TESTING
# =========================
class TestKalkulator(unittest.TestCase):

    def setUp(self):
        self.k = Kalkulator()

    def test_tambah(self):
        self.assertEqual(self.k.tambah(2, 3), 5)

    def test_kurang(self):
        self.assertEqual(self.k.kurang(5, 3), 2)

    def test_kali(self):
        self.assertEqual(self.k.kali(2, 4), 8)

    def test_bagi(self):
        self.assertEqual(self.k.bagi(10, 2), 5)

    def test_modulus(self):
        self.assertEqual(self.k.modulus(10, 3), 1)

    def test_pangkat(self):
        self.assertEqual(self.k.pangkat(2, 3), 8)

    def test_akar(self):
        self.assertEqual(self.k.akar(9), 3)

    def test_faktorial(self):
        self.assertEqual(self.k.faktorial(5), 120)

    def test_bagi_nol(self):
        with self.assertRaises(ValueError):
            self.k.bagi(5, 0)

    def test_akar_negatif(self):
        with self.assertRaises(ValueError):
            self.k.akar(-4)


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    print("1. Jalankan Kalkulator")
    print("2. Jalankan Unit Test")

    pilih = input("Pilih mode (1/2): ")

    if pilih == "1":
        main()
    elif pilih == "2":
        unittest.main()
    else:
        print("Pilihan tidak valid")
