# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 6 : Stuktur Organisasi Perusahaan
# ===================================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data        #menyimpan nilai data
        self.left = None        #child kiri
        self.right = None       #child kanan

# Fungsi preorder : Root ==> Left ==> Right
def preorder(node) :
    if node is not None:
        print(node.data, end=" ==> ")   #root
        preorder(node.left)             #left
        preorder(node.right)            #rights

# Membuat tree struktur organisasi
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

# Menjalankan
print("Struktur Oragnisasi (Preorder) : ")
preorder(root)



# Penjelasan : program struktur organisasi inni menggunakan traversal preorder
# yang dimulai dari root paling atas, yaitu Direktur, lalu ke manajer sebagai child level 1, 
# kemudian ke staf sebagai child level 2, urutan dari kiri ke kanan secara berurutan