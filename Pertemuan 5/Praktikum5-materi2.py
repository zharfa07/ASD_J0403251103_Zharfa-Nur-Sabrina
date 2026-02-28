# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk keluar)
# input 3
# Masuk 1- 2 - 3
# Keluar 
# =====================================================================================================

def hitung(n):
    # base case
    # jika n mencapai 0, rekursi diberhentikan 
    if n == 0:
        print("Selesai")
        return #hentikan fungsi agar tidak lanjut rekursi

    print("Masuk :", n)
    hitung(n-1)         #recursive case (nilai n dikurangi 1 tiap pemanggilan)
    print("Keluar", n)

print("===== Program Tracing =====")
hitung(6)