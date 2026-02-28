# =====================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================

# =====================================
# Latihan 2 : Tracing Rekursi
# =====================================

def countdown(n): 
    # base case : jika n sudah 0, maka rekursi dihentikan
    if n == 0: 
        print("Selesai") 
        return 
    
    print("Masuk:", n) 
    
    # recursive case : memanggil fungsi dengan nilai n dikurangi 1
    countdown(n - 1) 
    # Proses setelah rekursi (unwinding)
    # Akan dieksekusi setelah semua pemanggilan di bawahnya selesai
    print("Keluar:", n) 

countdown(3)