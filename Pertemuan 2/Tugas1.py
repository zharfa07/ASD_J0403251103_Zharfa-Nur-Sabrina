# =============================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus : Sistem Stok Barang Kantin (Berbasis File .txt)

# Nama  : Zharfa Nur Sabrina 
# NIM   : J0403251103
# Kelas : B2
# =============================================================

# --------------------------------
# Konstanta nama file 
# --------------------------------
nama_file = "stok_barang.txt"

# --------------------------------
# Fungsi : Membaca Data dari file 
# --------------------------------
def baca_stok(nama_file): 
    """
    Membaca data stok dari file teks.
    Format per baris : KodeBarang, NamaBarang, Stok
    Output:
    - stock_dict (dictionary)
      key   = kode_barang
      value = {"nama": nama_barang, "stok" : stok_int}
    """
    stok_dict = {}

    with open(nama_file, "r", encoding="utf-8") as file :
        for baris in file:
            baris = baris.strip()
            parts = baris.split(",")
            if len != 3:
                continue
            kode, nama, stok = parts
            stok_dict[kode] = {"nama": nama_barang, "stok" : stok_int}
            kode, nama, stok = baris.split(",")

            stok_dict[kode] = {
                "nama": nama_barang, 
                "stok" : stok_int
                }
            return stok_dict
        
# --------------------------------
# Fungsi : Menyimpan Data ke file 
# --------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "r", encoding="utf-8") as file :
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")
            pass
# --------------------------------
# Fungsi : Menampilkan semua data
# --------------------------------
def tampilkan_semua(stok_dict):
    """ 
    Menampilkan semua barang di stok_dict. 
    """
    if len(stok_dict) == 0:
        print("Stok Barang Kosong!")
        return
    print("=== Stok Barang ===")
    print(f"{'kode' : <8} | {'nama' : <12} | {'stok' : >5}")
    print("-" *30)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<8} | {'nama' : <12} | {'stok' : >5}")
        pass

# -------------------------------------
# Fungsi : Cari barang berdasarkan kode 
# -------------------------------------

def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang : ").strip()

    if cari_barang in stok_dict:
        nama = stok_dict[cari_barang]["nama"]
        stok = stok_dict[cari_barang]["stok"]
        print("\n=== Barang Ditemukan ===")
        print(f"Kode    : {cari_barang}")
        print(f"Nama    : {nama}")
        print(f"Stok    : {stok}")
    else:
        print("\n=== Barang Tidak Ditemukan ===")
    pass

# --------------------------------
# Fungsi : Tambah Barang Baru
# --------------------------------
def tambah_barang(stok_dict):
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru : ").strip()
    nama = input("Masukkan nama barang : ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan")
        return
    
    stok_awal = int(input("Masukkan  stok barang : "))
    stok_dict[kode] = {
                "nama": nama_barang, 
                "stok" : stok_int
                }
    return 
    print("Barang berhasil ditambahkan")

# --------------------------------
# Fungsi : Update stok barang
# --------------------------------

def update_stok(stok_dict):
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """
    kode = input("Masukkan kode barang yang ingin diupdate : ").strip()

    if kode not in stok_dict :
        print("Kode Barang tidak di temukan, update dibatalkan!")
        return
    
    print("Pilih jenis update : ")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2) : ").strip()
    jumlah = int(input("Masukkan jumlah : "))

    if pilihan == "1":
        stok = stok + jumlah
    elif pilihan =="2":
        stok = stok - jumlah
    pass

# --------------------------------
# Fungsi : Program Utama
# --------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan smeua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambahkan barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih Menu : ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(stok_barang)
        elif pilihan == "0": 
            print("\n--- Program Selesai ---")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
    if __main__ == "__main__":
        main()