# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Materi Rekursif : Backtracking Kombinasi Biner
# =====================================================================================================

def biner(n, hasil=""):
    # Base case : jika panjang string sudah n, cetak hasil
    if len(hasil) == n: 
        print(hasil)    #cetak hasil kombinasi
        return          #hentikan rekursi
    
    # Recursive case
    # Choose + Explore: tambah '0'  (memanggil fungsi dengan hasil + "0")
    biner(n, hasil + "0") 
    
    # Choose + Explore: tambah '1' (memanggil fungsi dengan hasil + "1")
    biner(n, hasil + "1") 

biner(3) #memanggil fugsi untuk menghasilkan semua kombinasi biner