# 1) Meminta tiga angka satu per satu
setoran1 = int(input("Masukkan setoran Mingguan1: "))
setoran2 = int(input("Masukkan setoran Mingguan2: "))
setoran3 = int(input("Masukkan setoran Mingguan3: "))

# 4) Jika ada input ≤ 0, tampilkan pesan error
if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid. Semua setoran harus lebih dari 0.")
else:
    # 2) Menjumlahkan semua setoran
    total = setoran1 + setoran2 + setoran3
    print(f"Total setoran: Rp{total:,}")

    # 3) Menentukan kategori total setoran
    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")
