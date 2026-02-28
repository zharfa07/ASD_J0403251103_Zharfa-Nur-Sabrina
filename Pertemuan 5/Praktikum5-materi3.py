# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Materi Rekursif : Menjumlahkan Elemen List
# =====================================================================================================

def jumlah_list(data, index=0):
    # base case 
    if index == len(data): # jika index sama dengan panjang data, semua elemen dijumlahkan
        return 0 #tidak ada yang dijumlahkan lagi
    
    # recursive case
    # Mengambil nilai pada index, lalu menambahkan dengan hasil pemanggilan fungsi berikutnya
    return data[index] + jumlah_list(data, index+1)

print("====== Program Jumlah Data ======")
# memanggil fungsi dengan list
print(jumlah_list([2,4,5]))