# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 4 : Memahami KOde Program (Merge Sort)
# ===================================================

def merge_sort(data):
    # kondisi rekursi berhenti
    # jika data sudah 0 atau 1, maka dianggap sudah terurut jadi tidak perlu dieksekusi lagi
    if len(data) <= 1:
        return data 

    # membagi data menjadi lebih kecil sampai menjadi base case
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # menggabungkan 2 list yang sudah diuturtkan menjadi satu list baru yang sudah terurut
    return merge(left_sorted, right_sorted) 
    

# Soal:
# 1. Apa yang dimaksud dengan base case? 
#   ==> kondisi rekursi berhenti
# 2. Mengapa fungsi memanggil dirinya sendiri? 
#   ==> rekursif, untuk mengubah/membagi data menjadi bagian sampai paling kecil (base case), 
#       lalu dipanggil untuk menggabungkan kembali dalam keadaan terurut.
# 3. Apa tujuan fungsi merge()? 
#   ==> untuk menggabungkan 2 list yang sudah diuturtkan menjadi satu list baru yang sudah terurut
