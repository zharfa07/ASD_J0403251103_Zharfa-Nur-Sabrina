# =====================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================

# =====================================
# Latihan 5 : Generator PIN
# =====================================

def buat_pin(panjang, hasil=""): 
    # base case : jika sudah hasil str sudah sama dengan panjang PIN, bisa dicetak
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    
    # recursive case : setiap angka ditambahkan ke hasil lalu panggil fungsi
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
        
buat_pin(3)