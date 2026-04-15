# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 2 : Membuat Binary Search Tree Sederhana
# ===================================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai data
        self.left = None    #child kiri
        self.right = None   #child kanan

# Membuat sebuah node root
root = Node ("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")

# Menampilkan isi node
print("Data pada root : ", root.data)
print("Child kiri root : ", root.left.data)
print("Child kanan root : ", root.right.data)
print("Child kiri dari B : ", root.left.left.data)
print("Child kanan dari B : ", root.left.right.data)
print("Child kiri dari C : ", root.right.left.data)
print("Child kanan dari C : ", root.right.right.data)

# Pembahasan : di dalam class node, membuat root dengan nilai "A". Setelah itu, 
# menambahkan child level 1 dengan nilai "B" di kiri dan "C" di kanan root, 
# kemudian menambahkan child level 2 pada node "B" memiliki anak D dan E, node "C" memiliki anak F dan G
# hasil akhir menampilkan seluruh isi tree setiap node melalui atribut kiri dan kanan