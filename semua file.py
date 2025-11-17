# ==================================================
# UAS LOGIKA DISKRIT - Versi Interaktif
# Sistem Penentuan Jalur Pasien di Rumah Sakit (CLI)
# Safe for Windows (no emoji, ASCII box)
# ==================================================

from collections import deque

# -------------------------
# Utility: Cetak kotak ASCII rapi
# -------------------------
def cetak_box(judul, isi_baris):
    """Mencetak kotak ASCII dengan judul dan daftar baris isi."""
    # panjang baris = panjang maksimum dari judul/isi + padding
    semua = [judul] + list(map(str, isi_baris))
    lebar = max(len(s) for s in semua) + 4
    print("+" + "-" * lebar + "+")
    # Judul di tengah
    jud = "  " + judul
    print("|" + jud.ljust(lebar) + "|")
    print("|" + ("-" * lebar) + "|")
    for baris in isi_baris:
        print("|  " + str(baris).ljust(lebar - 2) + "|")
    print("+" + "-" * lebar + "+\n")


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


# -------------------------
# MODUL 4 : GRAF (Interaktif BFS)
# -------------------------
def modul_graf_interaktif():
    try:
        cetak_box("MODUL 4 : GRAF (Rute Rumah Sakit)", [
            "Graf default akan digunakan. Anda bisa memilih titik awal dan tujuan."
        ])
        # Graf sederhana default
        graph = {
            "Lobby": ["Pendaftaran", "UGD"],
            "Pendaftaran": ["Lobby", "Poli Umum", "Poli Gigi"],
            "Poli Umum": ["Pendaftaran", "Farmasi"],
            "Poli Gigi": ["Pendaftaran"],
            "UGD": ["Lobby", "ICU"],
            "ICU": ["UGD"],
            "Farmasi": ["Poli Umum"]
        }

        cetak_box("Nodes di Graf", [f"{k}: {v}" for k, v in graph.items()])

        start = input("Masukkan node awal (contoh: Lobby): ").strip()
        goal = input("Masukkan node tujuan (contoh: Farmasi): ").strip()

        if start not in graph:
            print(f"Node awal '{start}' tidak ditemukan dalam graf.")
            return
        if goal not in graph:
            print(f"Node tujuan '{goal}' tidak ditemukan dalam graf.")
            return

        # BFS mencari rute terpendek (jalan tanpa bobot)
        def bfs(start_node, goal_node):
            queue = deque([[start_node]])
            visited = set()
            while queue:
                path = queue.popleft()
                node = path[-1]
                if node == goal_node:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph.get(node, []):
                        if neighbor not in path:  # hindari loop sederhana
                            new_path = list(path)
                            new_path.append(neighbor)
                            queue.append(new_path)
            return None

        path = bfs(start, goal)
        if path:
            cetak_box("Hasil Pencarian Rute", [f"Rute terpendek: {' -> '.join(path)}", f"Jumlah langkah: {len(path)-1}"])
        else:
            print("Tidak ditemukan rute dari", start, "ke", goal)
    except Exception as e:
        print("Terjadi kesalahan di modul graf:", e)


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


# -------------------------
# MENU INTERAKTIF UTAMA
# -------------------------
def menu_utama():
    while True:
        cetak_box("SISTEM PENENTUAN RUTE PASIEN - MENU UTAMA", [
            "1. Modul 1 - Logika Proposisi",
            "2. Modul 2 - Logika Predikat",
            "3. Modul 3 - Himpunan & Relasi",
            "4. Modul 4 - Graf (Pencarian Rute)",
            "5. Modul 5 - Aljabar Boolean",
            "6. Jalankan Semua Modul (demo cepat)",
            "0. Keluar"
        ])
        pilihan = input("Pilih menu (0-6): ").strip()
        if pilihan == "1":
            modul_proposisi_interaktif()
        elif pilihan == "2":
            modul_predikat_interaktif()
        elif pilihan == "3":
            modul_himpunan_interaktif()
        elif pilihan == "4":
            modul_graf_interaktif()
        elif pilihan == "5":
            modul_boolean_interaktif()
        elif pilihan == "6":
            # demo cepat (tetap minta input minimal tapi dapat berjalan)
            print("\nMenjalankan demo cepat (akan meminta beberapa input)...\n")
            modul_proposisi_interaktif()
            modul_predikat_interaktif()
            modul_himpunan_interaktif()
            modul_graf_interaktif()
            modul_boolean_interaktif()
        elif pilihan == "0":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 0 sampai 6.")

# Entry point
if __name__ == "__main__":
    menu_utama()
