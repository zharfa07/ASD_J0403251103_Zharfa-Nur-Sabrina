# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
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


'''
kondisi awal 10 - 20 - 30
diambil root lama x = 10
ambil anak kanan y = 20
ambil anak kiri dari y -> T2
melakukan rotasi 10 jadi anak kiri 20
karena T2 kosong, 20 tidak punya anak kanan
y = 20 menjadi root yang baru
'''
# Fungsi rotasi Kiri
def rotate_left (x):
    # x adalah root lama
    y = x.right     # y adalah child kanan x
    T2 = y.left     # subtree kiri milik y disimpan sementara

    # proses rotasi 
    y.left = x      # x menjadi child kiri dari y
    x.right = T2    # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)


# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri :  ")
tampil_struktur(root)

'''
hasil setelah rotasi
root = 20 
anak kiri = 10
anak kanan = 30
'''