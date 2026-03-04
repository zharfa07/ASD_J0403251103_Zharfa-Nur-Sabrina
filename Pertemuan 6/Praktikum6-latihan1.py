# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
# ===================================================

def insertion_sort(data):
    # indeks dimulai dari angka 1, karena indeks 0 dianggap sudah terurut
    #  Insertion Sort  membandingkan mulai dari elemen kedua ke kiri.
    for i in range(1, len(data)):
        key = data[i] #key berfungsi untuk menyimpan data yang disisipkan ke posisi yang benar disebelah kiri yang sudah terurut
        j = i - 1

        while j >= 0 and data[j] > key: 
        # menggunakan while karena jumlah pergeseran masih belum diketahui pasti  
        # dan memungkinakan untuk terus berjalan selama kondisi terpenuhi
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key #terjadi proses pergeseran elemen ke kanan agar key bisa ditempatkan di posisi yang benar.

    return data


# Soal:
# 1. Mengapa perulangan dimulai dari indeks 1? 
#   ==> karena indeks 0 dianggap sudah terurut
# 2. Apa fungsi variabel key? 
#   ==> key berfungsi untuk menyimpan nilai yang disisipkan ke posisi yang benar
# 3. Mengapa digunakan while, bukan for? 
#   ==> karena jumlah pergeseran tidak pasti dan akan terus berjalan selama kondisi terpenuhi
# 4. Operasi apa yang terjadi di dalam while? 
#   ==> operasi yang terjadi adalah pergeseran untuk memindahkan key ke posisi yang benar