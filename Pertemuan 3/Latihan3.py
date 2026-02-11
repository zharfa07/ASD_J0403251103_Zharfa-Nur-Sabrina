#==============================================================================
#Praktikum 2: Linked List
#Latihan 3 : Implementasikan Pencarian pada node tertentu Double Linked List
#==============================================================================

class node:
    def __init__(self, data):
        self.data = data #menyimpan nilai data pada node
        self.next = None #pointer ke node berikutnya
        self.prev = None #pointer ke node sebelumnya

class doublylinkedlist:
    def __init__(self):
        self.head = None #node pertama
        self.tail = None # node terakhir 
    
    def insert_at_end(self, data):
        new_node = node(data) #membuat node baru
        if not self.head:         #jika list masih kosong
            self.head = new_node 
            self.tail = new_node
        else:
            self.tail.next = new_node #sambung node terakhir ke node baru
            new_node.prev = self.tail
            self.tail = new_node #update
    
    def display(self):
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next    
            print("null")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key: #jika ditemukan
                return True
            temp = temp.next #ke node berikutnya 
        return False #jika tidak ditemukan

dll = doublylinkedlist()

#menambahkan data
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)
dll.display() #menampilkan data 

key = 9 #nilai yang dicari

if dll.search(key): #hasil pencarian
    print(f"elemen {key} ditemukan")
else:
    print(f"elemen {key} tidak ditemukan")

key = 0 #nilai yang dicari
if dll.search(key):
    print(f"elemen {key} ditemukan")
else:
    print(f"elemen {key} tidak ditemukan")
