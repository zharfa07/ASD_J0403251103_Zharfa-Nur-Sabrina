# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 5 : Melengkapi Fungsi Merge
# ===================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): #ascending
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # result.extend digunakan untuk menambahkan sisa elemen jika ada setelah perulangan selesai
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().
#   ==> result.extend digunakan untuk menambahkan sisa elemen jika ada setelah perulangan selesai
