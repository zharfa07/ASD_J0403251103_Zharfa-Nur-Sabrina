# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang
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
kondisi awal 30 - 20 - 10
ambil root yang lama y = 30
ambil anak kiri x = 20
ambil anak kanan dari x -> T2
melakukan rotasi 30 jadi anak kanan 20
T2 kosong, 30 tidak punya anak kiri
x = 20 menjadi root baru
'''
# Fungsi rotasi kanan
def rotate_right(y):
    # y adalah root lama
    x = y.left      # x adalah child kiri y
    T2 = x.right    # subtree kanan milik x disimpan sementara

    # proses rotasi
    x.right = y     # y menjadi child kanan dari x
    y.left = T2     # child kiri y diganti dengan T2

    # x menjadi root baru
    return x

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Rotasi kanan
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)

'''
hasil setelah rotasi
root = 20 
anak kiri = 10
anak kanan = 30
'''