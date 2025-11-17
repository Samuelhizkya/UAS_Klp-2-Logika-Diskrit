# -------------------------
# MODUL 2 : LOGIKA PREDIKAT (Relasi & Kuantor)
# -------------------------
def modul_predikat_interaktif():
    try:
        cetak_box("MODUL 2 : LOGIKA PREDIKAT", [
            "Masukkan daftar pasien (dipisah koma), contoh: Ani,Budi,Citra"
        ])
        teks = input("Daftar pasien: ").strip()
        pasien = [p.strip() for p in teks.split(",") if p.strip()]
        if not pasien:
            print("Tidak ada pasien yang dimasukkan. Kembali ke menu.")
            return

        ruang = {}
        print("Masukkan tujuan setiap pasien (kosongkan jika tidak ada).")
        for p in pasien:
            tujuan = input(f"Tujuan {p} (mis. Poli Umum / UGD): ").strip()
            ruang[p] = tujuan

        cetak_box("Data Ruangan Pasien", [f"{p} -> {ruang[p] or '-'}" for p in pasien])

        # Relasi contoh: tanya apakah ada pasien menuju UGD
        pert = input("Cek: Apakah ada pasien menuju (ketik nama ruang, contoh: UGD) ? (kosong=lewati): ").strip()
        if pert:
            ada = any(ruang[p].lower() == pert.lower() for p in pasien if ruang[p])
            print(f"Ada pasien menuju {pert}?: {ada}")

        semua_punya_ruang = all(ruang[p] != "" for p in pasien)
        ada_ke_ugd = any(ruang[p].lower() == "ugd" for p in pasien if ruang[p])

        cetak_box("Kuantor & Hasil Predikat", [
            f"Apakah semua pasien punya tujuan? {semua_punya_ruang}",
            f"Ada pasien menuju UGD? {ada_ke_ugd}"
        ])
    except Exception as e:
        print("Terjadi kesalahan di modul predikat:", e)
