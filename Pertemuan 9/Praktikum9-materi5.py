# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 5 : Membuat Traversal Postorder
# Dimulai dari bawah => Left -> Right -> Root
# ===================================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai data
        self.left = None    #child kiri
        self.right = None   #child kanan

# Membuat Traversal Postorder : left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
    

# Membuat tree
# Membuat sebuah node root
root = Node ("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")


# Menjalankan Traversal Postorder
print("Hasil Traversal Postorder : ")
postorder(root)

# Penjelasan : traversal postorder, penelusuran tree dari urutan kiri, kanan, dan root
# hasil data menampilkan dari sisi bawah ke atas secara terstuktur