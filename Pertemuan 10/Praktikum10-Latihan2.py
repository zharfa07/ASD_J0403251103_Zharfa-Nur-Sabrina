# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 4 : Membuat BST yang Tidak Seimbang
# ===================================================

# Class node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data        #nilai pada node
        self.left = None        #child kiri 
        self.right = None       #child kanan

# alur fungsi inserti pada bst 
'''
fungsi Insert digunakan untuk memasukkan data ke BST
pertama, jika root masih kosong (none), data langsung menjadi node baru (root)
jika tree sudah ada data, bandingkan dengan nilai root, 
jika lebih kecil, proses ke anak kiri | jika lebih besar, proses ke anak kanan
dilakukan secara rekursif
'''

# fungsi insert untuk BST
def insert(root, data):
    if root is None :                           #jika root kosong, buat node baru
        return Node(data)

    if data < root.data :                       #jika data lebih kecil, masuk ke subtree kiri
        root.left = insert(root.left, data)
    elif data > root.data :                     #jika data lebih besar, masuk ke subtree kanan
        root.right = insert(root.right, data)

    return root

'''
Preorder : root -> kiri -> kanan
dimulai dari root dahulu, ke anak kiri, dan ke anak kanan
'''
# fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")   #root
        preorder(root.left)         #kiri
        preorder(root.right)        #kanan

'''
menampilkan sesuai struktur 
kiri dengan label L
kanan dengan label R
'''
# fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")   #posisi node dengan spasi sesuai level
        tampil_struktur(root.left, level + 1, "L")      #ke child kiri
        tampil_struktur(root.right, level + 1, "R")     #ke child kanan

# -----------------------------
# Program utama
# -----------------------------
root = None #awal tree kosong

# data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)  #menampilkan isi tree dengan preorder

print("\n\nStruktur BST:")
tampil_struktur(root) #bentuk tree