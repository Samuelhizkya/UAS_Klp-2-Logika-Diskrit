# -------------------------
# MODUL 1 : LOGIKA PROPOSISI
# -------------------------
def modul_proposisi_interaktif():
    try:
        cetak_box("MODUL 1 : LOGIKA PROPOSISI", [
            "Input nilai proposisi (ketik True/False). Contoh: True"
        ])
        kamar_tersedia = input("Apakah kamar tersedia? (True/False): ").strip().title() == "True"
        pasien_darurat = input("Apakah pasien darurat? (True/False): ").strip().title() == "True"
        dokter_hadir = input("Apakah dokter hadir? (True/False): ").strip().title() == "True"

        hasil = [
            f"Kamar tersedia: {kamar_tersedia}",
            f"Pasien darurat: {pasien_darurat}",
            f"Dokter hadir : {dokter_hadir}",
            "",
            "--- Operasi Logika ---",
            f"Konjungsi (AND) kamar & darurat: {kamar_tersedia and pasien_darurat}",
            f"Disjungsi (OR) kamar | dokter   : {kamar_tersedia or dokter_hadir}",
            f"Implikasi (Jika darurat -> dokter hadir): {(not pasien_darurat) or dokter_hadir}",
            f"Negasi (NOT dokter hadir): {not dokter_hadir}",
        ]
        cetak_box("Hasil - MODUL 1", hasil)
    except Exception as e:
        print("Terjadi kesalahan di modul proposisi:", e)
