# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 3 : Membuat Traversal Preorder
# Root -> Left -> Right
# ===================================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai data
        self.left = None    #child kiri
        self.right = None   #child kanan

# Fungsi preorder : Root ==> Left ==> Right
def preorder(node) :
    if node is not None:            #mengecek apakah node ada 
        print(node.data, end=" ")   #root
        preorder(node.left)         #left
        preorder(node.right)        #rights

# Membuat tree
# Membuat sebuah node root
root = Node ("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D") 
root.left.right = Node("E")


# Menjalankan Traversal Preorder
print("Hasil Traversal Preorder : ")
preorder(root)

# Penjelasan : menggunakan struktur data tree untuk menyimpan data secara hirarki
# dalam kode ini traversal yang digunakan adalah preorder dengan pengurutan dari root, left, right
# preorder mencetak hasil dimulai dari node utama yaitu root(paling atas), 
# kemudian dilanjutkan ke bagian kiri dan kanan dengan membuat child level 1, yaitu B dan C
# kemudian membuat lagi child level 2 dari B dan C, yaitu D E dan F G
# urutan penelusuran hasil travesal preorder dari atas ke bawah sesuai struktur