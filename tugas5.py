def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0

    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        return (
            f"Student(nama='{self.nama}', "
            f"nim='{self.nim}', "
            f"rata={self.rata_nilai()}, "
            f"status={self.status()})"
        )


if __name__ == "__main__":

    print("=== FUNCTIONS ===")

    print(greet("Arifian"))

    print("tambah(5, 7) =", tambah(5, 7))
    print("tambah(10) =", tambah(10))

    print("rata_rata([80, 90, 100]) =", rata_rata([80, 90, 100]))
    print("rata_rata([]) =", rata_rata([]))

    print()
    print("=== CLASS STUDENT ===")

    mahasiswa1 = Student("Budi", "A123")

    mahasiswa1.tambah_nilai(80)
    mahasiswa1.tambah_nilai(85)
    mahasiswa1.tambah_nilai(82.5)

    print(mahasiswa1)
    print("Rata-rata:", mahasiswa1.rata_nilai())
    print("Status:", mahasiswa1.status())

    print()

    mahasiswa2 = Student("Arie", "A124")

    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(68)

    print(mahasiswa2)
    print("Rata-rata:", mahasiswa2.rata_nilai())
    print("Status:", mahasiswa2.status())
