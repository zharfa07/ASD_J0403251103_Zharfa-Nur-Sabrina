# =====================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================

# =====================================
# Latihan 4 : Kombinasi Huruf
# =====================================

def kombinasi(n, hasil=""): 
    # base case : jika hasil sama dengan n, kombinasi sudah lengkap dan bisa dicetak
    if len(hasil) == n: 
        print(hasil) 
        return 

    # recursive case : (Choose + Explore)
    kombinasi(n, hasil + "A") #pilihan 1
    kombinasi(n, hasil + "B") #pilihan 2

# memanggil fungsi dengan panjang kombinasi
kombinasi(2)