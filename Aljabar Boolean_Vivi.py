# -------------------------
# MODUL 5 : ALJABAR BOOLEAN & LOGIKA DIGITAL
# -------------------------
def modul_boolean_interaktif():
    try:
        cetak_box("MODUL 5 : ALJABAR BOOLEAN", [
            "Masukkan kondisi (True/False)"
        ])
        darurat = input("Darurat? (True/False): ").strip().title() == "True"
        ada_kamar = input("Ada kamar? (True/False): ").strip().title() == "True"

        diterima = (darurat and ada_kamar) or (darurat and not ada_kamar)

        cetak_box("Hasil Triase Sederhana", [
            f"Status darurat: {darurat}",
            f"Ada kamar: {ada_kamar}",
            f"Apakah pasien diterima?: {diterima}"
        ])
    except Exception as e:
        print("Terjadi kesalahan di modul boolean:", e)


