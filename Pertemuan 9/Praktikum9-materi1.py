# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 1 : Membuat Node
# ===================================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai data
        self.left = None    #child kiri
        self.right = None   #child kanan

# Membuat sebuah node root
root = Node ("A")
        
# Menampilkan isi node
print("Data pada root : ", root.data)       #menampilkan nilai data pada root
print("Child kiri root : ", root.left)      #belum ada child kiri -> none
print("Child kanan root : ", root.right)    #belum ada child kiri -> none

# Pembahasan : Kode program dimulai dengan membuat class Node, dan membuat root dengan nilai "A". 
# Karena belum ada child kiri dan kanan, maka hasil pencetakan data root child kiri dan kanan : None 
# Kode hanya membuat satu node (root) sebagai awal dari tree, tanpa child.
