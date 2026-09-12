nama = "Budi"              
umur = 20                    
tinggi = 170.5               
mahasiswa = True             
hobi = ["Membaca", "Coding", "Gaming", "Musik", "Olahraga"] 

print("=== Deklarasi Variabel dan Tipe Data ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", mahasiswa)
print("Hobi:", hobi)

print("\n=== Manipulasi String ===")

teks = "Pemrograman Python"

print("Teks:", teks)
print("Gabungan string:", "Saya belajar " + teks)
print("Panjang teks:", len(teks))
print("Huruf besar:", teks.upper())
print("Huruf kecil:", teks.lower())
print("\n=== Operasi Matematika Sederhana ===")

angka1 = 20
angka2 = 6

print("Angka 1:", angka1)
print("Angka 2:", angka2)
print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pembagian bulat:", angka1 // angka2)
print("Sisa pembagian:", angka1 % angka2)

print("\n=== List dan Akses Elemen ===")

buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Semangka"]

print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen ketiga:", buah[2])

buah.append("Anggur")
print("Setelah append:", buah)

buah.remove("Jeruk")
print("Setelah remove:", buah)


print("\n=== Perkenalan ===")

nama_user = input("Masukkan nama Anda: ")
umur_user = int(input("Masukkan umur Anda: "))

print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
