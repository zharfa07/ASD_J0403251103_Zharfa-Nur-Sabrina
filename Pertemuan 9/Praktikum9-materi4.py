# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 4 : Membuat Traversal Inorder
# Inorder dimulai dari bawah => Left -> Root -> Right
# ===================================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai data
        self.left = None    #child kiri
        self.right = None   #child kanan

# Membuat fungsi inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Membuat tree
# Membuat sebuah node root
root = Node ("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan Traversal Inorder
print("Hasil Traversal Inorder : ")
inorder(root)

# Penjelasan : traversal inorder, penelusuran tree dari urutan kiri, root, dan kanan
# hasil data menampilkan dari sisi kiri ke kanan (bagian bawah) secara terstuktur