# -------------------------
# MODUL 3 : HIMPUNAN & RELASI
# -------------------------
def modul_himpunan_interaktif():
    try:
        cetak_box("MODUL 3 : HIMPUNAN & RELASI", [
            "Masukkan dua himpunan pasien (dipisah koma)."
        ])
        a_text = input("Himpunan A (mis. Ani,Budi,Farid): ").strip()
        b_text = input("Himpunan B (mis. Budi,Citra,Doni): ").strip()

        setA = {s.strip() for s in a_text.split(",") if s.strip()}
        setB = {s.strip() for s in b_text.split(",") if s.strip()}

        hasil = [
            f"Pasien A: {sorted(setA)}",
            f"Pasien B: {sorted(setB)}",
            "",
            f"Irisan A ∩ B : {sorted(setA & setB)}",
            f"Gabungan A ∪ B: {sorted(setA | setB)}",
            f"Selisih A - B : {sorted(setA - setB)}"
        ]
        cetak_box("Hasil Operasi Himpunan", hasil)
    except Exception as e:
        print("Terjadi kesalahan di modul himpunan:", e)

