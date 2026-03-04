# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 2 : Melengkapi Potongan Kode
# ===================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key: #ascending 
            data[j + 1] = data[j]
            j -= 1

        data[j+1] = key
    return data

# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending. 
# ==> data[j] > key
# ==> data[j+1] = key

# 2. Ubah agar menjadi descending.
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key: #descending 
            data[j + 1] = data[j]
            j -= 1

        data[j+1] = key
    return data