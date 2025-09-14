# Nama = Qonitah Khansa' Ayu Madani Alamsyah
# NIM  = 2509116113
# Kelas= Sistem Informasi C'25
# PRAKTIKUM MINI PROJECT 1 (Sistem Manajemen Stok Cemilan)

stok_cemilan = []  # List untuk menyimpan tuple cemilan

print("selamat datang di stok cemilan asa!, ini adalah program buat nyatet cemilan kamu biar ga lupa^^ ")
print("Program ini buat nyatet cemilan kamu biar ga lupa ^^")

while True:
    print("\n=== Menu Manajemen Stok Cemilan ===")
    print("1. Tambah cemilan🍟🧃")
    print("2. Lihat daftar cemilan🔍")
    print("3. Hapus cemilan😞")
    print("4. Keluar")

    pilihan = input("mau pilih yang mana? (1/2/3/4): ")

    # Tambah cemilan
    if pilihan == "1":
        nama = input("Nama cemilan: ")
        rasa = input("Rasa cemilan (manis/asin/pedas): ")
        jumlah = input("Jumlah stok: ")
        status = input("Status (ada/habis/expired): ")

        # Simpan data dalam bentuk tuple
        cemilan = (nama, rasa, jumlah, status)
        stok_cemilan.append(cemilan)

        print("Yey! Cemilan berhasil ditambahkan!")

    # Lihat daftar cemilan
    elif pilihan == "2":
        if len(stok_cemilan) == 0:
            print("Belum ada cemilan yang dicatat nih.")
        else:
            print("\nDaftar Cemilan:")
            nomor = 1
            for cemilan in stok_cemilan:
                print(f"{nomor}. Nama: {cemilan[0]}, Rasa: {cemilan[1]}, Jumlah: {cemilan[2]}, Status: {cemilan[3]}")
                nomor += 1

    # Hapus cemilan
    elif pilihan == "3":
        if len(stok_cemilan) == 0:
            print("Belum ada cemilan yang bisa dihapus nih.")
        else:
            nomor = 1
            for cemilan in stok_cemilan:
                print(f"{nomor}. {cemilan[0]} ({cemilan[1]})")
                nomor += 1

            hapus = int(input("Nomor cemilan yang mau dihapus: "))
            if hapus >= 1 and hapus <= len(stok_cemilan):
                terhapus = stok_cemilan.pop(hapus-1)
                print(f"oke, Cemilan sudah dihapus.")
            else:
                print("Nomor tidak valid.")

    # Keluar
    elif pilihan == "4":
        print("Program ditutup. Jangan lupa beli cemilan kalau sudah habis ya!")
        break

    else:
        print("Pilihan tidak dikenal. Coba lagi.")