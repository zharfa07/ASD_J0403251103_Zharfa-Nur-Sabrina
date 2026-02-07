# =============================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus : Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Zharfa Nur Sabrina 
# NIM   : J0403251103
# Kelas : B2
# =============================================================

# --------------------------------
# Konstanta nama file 
# --------------------------------
nama_file = "stok_barang.txt"

# --------------------------------
# Fungsi 1 : Membaca Data dari file 
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
    stok_dict = {} #inisialisasi stok di dictionary

    #membuka file dan membaca seluruh baris
    with open(nama_file, "r", encoding="utf-8") as file :
        for baris in file:
            baris = baris.strip() #untuk menghilangkan karakter baris baru
            parts = baris.split(",") #untuk memisahkan kolom, memecah menjadi data satuan (per koma)

            if len(parts) != 3: #format baris
                continue

            kode, nama, stok = parts #memecah data per baris
            stok_dict[kode] = {"nama": nama, "stok" : int(stok)}
            kode, nama, stok = baris.split(",")

            # menyimpan data dalam dictionary stok ke dictionary dengan key -> kode
            stok_dict[kode] = {    #key
                "nama": nama,      #value
                "stok" : int(stok) #value, ubah nilai ke integer
                }
        return stok_dict
        
# --------------------------------
# Fungsi 2 : Menyimpan Data ke file 
# --------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    #menulisk ulang seluruh isi file berdasarkan dictionary
    with open(nama_file, "w", encoding="utf-8") as file : 
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n") #menulis data ke file
            pass

# --------------------------------
# Fungsi 3 : Menampilkan semua data
# --------------------------------
def tampilkan_semua(stok_dict):
    """ 
    Menampilkan semua barang di stok_dict. 
    """
    if len(stok_dict) == 0: #mengecek stok apabila kosong
        print("Stok Barang Kosong!")
        return
    #membuat header tabel
    print("=== Stok Barang ===")
    print(f"{'kode' : <8} | {'nama' : <12} | {'stok' : >5}") #format : kode | nama | stok
    print("-" *32) #membuat garis header
    for kode in sorted(stok_dict.keys()): #mengurutkan data
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode: <8} | {nama: <12} | {stok: >5}") #membuat tampilan yang rapi (<: rata kiri, >:rata kanan, angka: lebar kolom karakter)
        pass

# -------------------------------------
# Fungsi 4 : Cari barang berdasarkan kode 
# -------------------------------------

def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang : ").strip()

    #mengecek apakah kode ada di dictionary
    if kode in stok_dict: 
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print("\n=== Barang Ditemukan ===")
        print(f"Kode    : {kode}")
        print(f"Nama    : {nama}")
        print(f"Stok    : {stok}")
    else:
        print("\n=== Barang Tidak Ditemukan ===")
    pass

# --------------------------------
# Fungsi 5 : Tambah Barang Baru
# --------------------------------
def tambah_barang(stok_dict):
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru : ").strip().upper()
    nama = input("Masukkan nama barang baru : ").strip()

    #mengecek apakah kode ada di dictionary
    if kode in stok_dict: 
        print("Kode sudah digunakan") #validasi kode tidak duplikat
        return
    
    #input stok awal dalam bentuk integer
    try:
        stok_awal = int(input("Masukkan  stok barang : "))
    except ValueError: 
        print("Stok harus berupa angka")
        return
    
    #menyimpan barang baru ke dictionary
    stok_dict[kode] = {
        "nama": nama, 
        "stok" : stok_awal
    }
    print("Barang berhasil ditambahkan")

# --------------------------------
# Fungsi 6 : Update stok barang
# --------------------------------

def update_stok(stok_dict):
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """
    # mencari kode barang yang akan diupdate stoknya
    kode = input("Masukkan kode barang yang ingin diupdate stoknya : ").strip()

    #mengecek apakah kode ada di dictionary
    if kode not in stok_dict : 
        print("Kode Barang tidak di temukan, update dibatalkan!")
        return
    
    print("Pilih jenis update : ") #menampilkan pilihan jenis update stok
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2) : ").strip()
    
    #input jumlah stok yang akan diubah
    try: 
        jumlah = int(input("Masukkan jumlah stok yang ingin diupdate (0-100) : ").strip())
    except ValueError:
        print("Jumlah harus berupa angka. Update dibatalkan")
        return
    if jumlah < 0 or jumlah > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")
        return
    
    stok_lama = stok_dict[kode]["stok"] #menyimpan stok sebelum diubah

    if pilihan == "1":
        stok_baru = stok_lama + jumlah
        print("Stok berhasil diupdate")
    elif pilihan =="2":
        if stok_lama - jumlah < 0:
            print("Update dibatalkan. Stok tidak boleh negatif")
            return
        stok_baru = stok_lama - jumlah
        print("Stok berhasil diupdate")
    else:
        print("Pilihan tidak valid!")
        return
    
    stok_dict[kode]["stok"] = stok_baru #menyimpan stok baru ke dictionary
    
    # hasil update stok
    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")
    pass

# --------------------------------
# Fungsi 7 : Program Utama
# --------------------------------
def main(): #main fungsi prioritas yang akan secara otomatis selalu dibuka lebih awal
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang") #fs no.3
        print("2. Cari barang berdasarkan kode") #fs no.4
        print("3. Tambahkan barang baru") #fs no.5
        print("4. Update stok barang") #fs no.6
        print("5. Simpan ke file") #fs no.2
        print("0. Keluar")
        
        pilihan = input("Pilih Menu : ").strip()

        #memanggil data
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Stok berhasil tersimpan")
        elif pilihan == "0": 
            print("\n--- Program Selesai ---")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
if __name__ == "__main__":
    main()
