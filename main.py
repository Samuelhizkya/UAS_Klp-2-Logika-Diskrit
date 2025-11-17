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
