# =====================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================

# =====================================
# Latihan 3 : Mencari Nilai Maksimum
# =====================================

def cari_maks(data, index=0): 
    # Base case : jika index berada di elemen terakhir, langsung kembalikan nilai tersebut
    if index == len(data) - 1: 
        return data[index] 
    
    # Recursive case : mencari nilai maks dari sisa elemen 
    maks_sisa = cari_maks(data, index + 1) 
    
    # membandingkan elemen dengan maks dari sisa elemen
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 

angka = [3, 7, 2, 9, 5]  #data list angka

print("Nilai maksimum:", cari_maks(angka)) #menampilkan hasil maks