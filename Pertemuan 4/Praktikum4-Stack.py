# =============================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =============================================
# Implementasi Dasar : Node pada Linked List
# =============================================

# Membuat class node (merupakan unit dasar dari Linked List)
class Node: 
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai data
        self.next = None #untuk menginisialisasi pointer ketika dijalankan ke note berikutnya (awal=none)

# 1) Memanggil konstruktor dalam class
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4)Traversal : menelusuri dari head sampai none
current = head 
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

# ================================================
# Implementasi Dasar : Linked List + Insert Awal
# ================================================

class Linkedlist: #class implementasi Stack
    def __init__(self): #konstruktor
        self.head = None #awalnya kosong

    def insert_awal(self, data): #konsep push dalam stack
        # 1) buat node baru
        nodeBaru = Node(data) #panggil class node

        # 2) node buat menunjuk ke head lama, karena penambahan data baru
        nodeBaru.next = self.head 

        # 3) head pindah ke node 
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        # menghapus = menggeser head ke node berikutnya (setelah head, akhirnya head lama hilang)
        self.head = self.head.next
        print("Node yang dihapus adalah :", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next 
        

print("=== List Baru ===") 
ll = Linkedlist() #instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan() #stack, LIFO(last in first out)
ll.hapus_awal()
ll.tampilkan()




'''
instantiasi 
kostruktor : otomatis
object 
metode
properti : variabel
'''
