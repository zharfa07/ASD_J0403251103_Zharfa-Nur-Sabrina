# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Materi Rekursif : Backtracking Kombinasi Biner dengan Batas '1' (Pruning)
# =====================================================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0): 
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti agar tidak melanjutkan percabangan yang tidak valid
    if jumlah_1 > batas: 
        return 
    
    # Base case : jika panjang str sudah sama dengan n, kombinasi lengkap dan dapat dicetak
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    # Recursive case 
    # Pilih '0', tidak berubah karena tidak menambah angka 1
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1', bertambah 1 karena menambah angka 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) 
    
biner_batas(4, 2)