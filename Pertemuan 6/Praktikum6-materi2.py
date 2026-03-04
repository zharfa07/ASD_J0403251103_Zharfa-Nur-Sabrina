# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Insertion Sort (Ascending)
# ===================================================
def insertion_sort(data):
    # melihat data awal
    print("Data Awal : ", data)
    print("="*50)

    # loop mulai dari data kedua (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # simpan nilai yang disisipkan 
        j = i-1 # index elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai ke = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i:])

        # geser 
        while j>=0 and data[j] > key: #selama lebih besar
            data[j+1] = data[j]
            j -= 1 #menggeser
        # sisipkan key ke posisi yang benar
        data[j+1] = key
        
        print("Setelah disisipkan : ", data)
        print("-"*50)

    return data 

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))
print("="*50)