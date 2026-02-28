# =====================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================

# =====================================
# Latihan 1 : Rekursi Pangkat
# =====================================

def pangkat(a, n): 
    # Base case : kondisi berhenti jika pangkat n=0, hasilnya selalu 1
    if n == 0: 
        return 1 
    
    # Recursive case : memanggil nilai a dengan  hasil pemanggilan fungsi
    return a * pangkat(a, n - 1) 

print(pangkat(2, 4)) # Output: 16