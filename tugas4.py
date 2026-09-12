print("=== LIST ===")

data = ["Budi", 20, 85.5, "Surabaya", True, 100, "Python"]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])

print("Slicing [1:6:2]:", data[1:6:2])

print("\nSebelum append:", data)
data.append("OOP")
print("Sesudah append:", data)

print("\nSebelum insert:", data)
data.insert(1, "Mahasiswa")
print("Sesudah insert:", data)

print("\nSebelum extend:", data)
data.extend(["AI", "Coding"])
print("Sesudah extend:", data)

print("\nSebelum pop:", data)
item_pop = data.pop()
print("Item yang di-pop:", item_pop)
print("Sesudah pop:", data)

print("\nSebelum remove:", data)
data.remove(True)
print("Sesudah remove:", data)

print("\n=== TUPLE ===")

mahasiswa = ("Arifian", "A12345", 2026, "Sidoarjo", "AI", 20)

print("Tuple:", mahasiswa)
print("Panjang tuple:", len(mahasiswa))
print("Elemen indeks 0:", mahasiswa[0])
print("Elemen indeks 2:", mahasiswa[2])

nama, nim, angkatan, *rest = mahasiswa

print("Hasil unpacking:")
print("Nama:", nama)
print("NIM:", nim)
print("Angkatan:", angkatan)
print("Rest:", rest)

print("\n=== SET ===")

set_a = {"Python", "Java", "C++", "Python", "C"}
set_b = {"Python", "JavaScript", "C++", "Go"}

print("Set A:", set_a)
print("Set B:", set_b)

print("Duplikat 'Python' otomatis dihilangkan dari Set A.")

print("\nUnion (A | B):")
print(set_a | set_b)

print("\nIntersection (A & B):")
print(set_a & set_b)

print("\nDifference (A - B):")
print(set_a - set_b)

print("\nSymmetric Difference (A ^ B):")
print(set_a ^ set_b)

print("\n=== DICTIONARY ===")

data_mahasiswa = {
    "nama": "Arifian",
    "nim": "A12345",
    "angkatan": 2026,
    "kota": "Sidoarjo"
}

print("Dictionary awal:", data_mahasiswa)

data_mahasiswa["jurusan"] = "Kecerdasan Artifisial"
print("\nSetelah tambah key:", data_mahasiswa)

data_mahasiswa["kota"] = "Surabaya"
print("Setelah mengubah kota:", data_mahasiswa)

del data_mahasiswa["angkatan"]
print("Setelah menghapus angkatan:", data_mahasiswa)

print("\nKeys:")
print(data_mahasiswa.keys())

print("\nValues:")
print(data_mahasiswa.values())

print("\nItems:")
print(data_mahasiswa.items())

print("\nIterasi dictionary:")
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")

print("\n=== NESTED STRUCTURES ===")

buku = [
    {
        "judul": "Python Dasar",
        "penulis": "Andi",
        "tahun": 2021
    },
    {
        "judul": "Pemrograman OOP",
        "penulis": "Budi",
        "tahun": 2023
    },
    {
        "judul": "Artificial Intelligence",
        "penulis": "Citra",
        "tahun": 2024
    },
    {
        "judul": "Machine Learning",
        "penulis": "Deni",
        "tahun": 2025
    }
]

print("Daftar semua judul buku:")

for item in buku:
    print("-", item["judul"])

tahun_filter = 2023

buku_terbaru = [
    item for item in buku
    if item["tahun"] >= tahun_filter
]

print(f"\nBuku terbit >= {tahun_filter}:")

for item in buku_terbaru:
    print(f"- {item['judul']} ({item['tahun']})")

print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))

print("Daftar angka:", angka)

angka_genap = [x for x in angka if x % 2 == 0]

angka_kuadrat = [x ** 2 for x in angka]

print("Angka genap:", angka_genap)
print("Kuadrat:", angka_kuadrat)

angka_status = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1, 11)
}

print("\nDict angka genap/ganjil:")
print(angka_status)

kalimat = "Pemrograman Python dan Artificial Intelligence"

huruf_unik = {
    huruf.lower()
    for huruf in kalimat
    if huruf.isalpha()
}

print("\nKalimat:", kalimat)
print("Huruf unik:", huruf_unik)

print("\n=== KEANGGOTAAN & PENCARIAN ===")

bahasa = ["Python", "Java", "C++", "JavaScript"]

print("Apakah Python ada di list?", "Python" in bahasa)
print("Apakah Rust ada di list?", "Rust" in bahasa)

bahasa_set = {"Python", "Java", "C++", "Go"}

print("Apakah Python ada di set?", "Python" in bahasa_set)
print("Apakah Rust ada di set?", "Rust" in bahasa_set)

item = "C++"

if item in bahasa:
    posisi = bahasa.index(item)
    print(f"{item} ditemukan pada indeks {posisi}.")
else:
    print(f"{item} tidak ditemukan.")

item = "Rust"

if item in bahasa:
    posisi = bahasa.index(item)
    print(f"{item} ditemukan pada indeks {posisi}.")
else:
    print(f"{item} tidak ditemukan.")
