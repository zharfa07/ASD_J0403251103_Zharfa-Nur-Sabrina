# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 1 : Node dan Insert pada BST
# ===================================================

# membuat class node
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan  nilai/data
        self.left = None    #pointer ke anak kiri
        self.right = None   #pointer ke anak kanan

# Alur fungsi insert pada bst 
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

    return root #mengambil root yang sudah diperbarui

# Mengisi data BST
root = None         #root awal kosong
data_list = [50,30,70,20,40,50,80]

for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat\n")


# ===================================================
# Latihan 2 : Traversal Inorder (menampilkan hasil penelusuran)
# ===================================================

# alur fungsi inorder
'''
mulai child kiri, lanjut menampilkan nilai root, lalu ke child kanan
dilakukan berulang (rekursif)
'''
def inorder(root):
    if root is  not None:
        inorder(root.left)          #kiri
        print(root.data, end=" ")   #root
        inorder(root.right)         #kanan

print("Hasil Inorder : ")
inorder(root)


# ===================================================
# Latihan 3 : Search di BST (menelusuri, membandingkan)
# ===================================================

'''
jika node kosong, data tidak ditemukan
jika nilai node sama dengan data yang dicari, data ditemukan
jika data yang dicari lebih kecil, maka pencarian dilanjutkan ke anak kiri
jika data yang dicari lebih besar, maka pencarian dilanjutkan ke anak kanan
'''

# fungsi mencari data pada BST 
def search(root, key):
    # jika kosong, data tidak ditemukan (salah)
    if root is None:
        return False
    
    # jika data ditemukan (benar)
    if root.data == key:
        return True
    # jika key lebih kecil, cari ke kiri
    elif key < root.data : 
        return search(root.left, key)
    # jika key lebih besar, cari ke kanan
    else:
        return search(root.right, key)
    
# Uji pencarian
key = 100

if search(root, key):
    print("\nData Ditemukan")
else :
    print("\nData Tidak Ditemukan")
