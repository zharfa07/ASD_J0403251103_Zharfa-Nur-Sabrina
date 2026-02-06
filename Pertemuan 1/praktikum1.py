#=============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#=============================================================

#membuka file dengan mode read ("r")

#membuka file dalam satu string
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("\n===Hasil Read===")
print("Tipe Data :", type(isi_file)) 
print("Jumlah Karakter :", len(isi_file))
print("Jumlah Baris :", isi_file.count("\n")+1)

#membaca file per baris
print("\n===Membaca File per Baris===")
Jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file :
    for baris in file:
        Jumlah_baris = Jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru (newline) untuk mengambil data murni
        print("baris ke-", Jumlah_baris)
        print("Isinya :", baris)

#=============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : parsing baris menjadi kolom data
#=============================================================

print("\n")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file :
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#=============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca File dan Menyimpan ke List
#=============================================================

data_list = [] #list untuk menampung data mahasiswa
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file :
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan sebagai list "[nama,nim,nilai]"
        data_list.append([nim, nama, int(nilai)])

print("\n=== Data Mahasiswa dalam List ===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print("Jumlah Record :", len(data_list))

print("=== Menampilkan Data Record tertentu ===")
print("Contoh Record Pertama :", data_list[0]) #array dimulai dari 0

#=============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary
#=============================================================

data_dict = {} #buat variabel untuk dictionary (key-value)
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file :
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {          #key
            "nama" : nama,          #values
            "nilai" : int(nilai)    #values
        }

print("\n=== Data Mahasiswa dalam Dictionary ===")
print(data_list)
