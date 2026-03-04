# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 3 : Tracing Insertion Sort
# ===================================================

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]
# Soal:
# 1. Tuliskan isi list setelah iterasi i = 1.
#      ==> i = [2,5,4,6,1,3]
# 2. Tuliskan isi list setelah iterasi i = 3.
#      ==> i = [2,5,4,6,1,3]
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
#      ==> 4 kali

def insertion_sort(data):
    # loop mulai dari data kedua (index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] # simpan nilai yang disisipkan 
        j = i-1 # index elemen terakhir di bagian kiri

        # geser 
        while j>=0 and data[j] > key: #selama lebih besar
            data[j+1] = data[j]
            j -= 1 #menggeser
        # sisipkan key ke posisi yang benar
        data[j+1] = key
    return data 

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))