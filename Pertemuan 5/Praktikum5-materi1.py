# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
# =====================================================================================================

def faktorial(n):
    # base case (menghentikan proses rekursi agar tidak berjalan tanpa akhir)
    if n == 0:
        return 1
    
    # recursive case (fungsi memanggil fungsi sendiri)
    return n*faktorial(n-1) #n-1*n-2*n-3 ...n-?

print("===== Program Faktorial =====")
print("Hasil Faktorial : ", faktorial(3))
