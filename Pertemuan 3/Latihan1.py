#==============================================================================
#Praktikum 2: Linked List
#Latihan 1 : Implementasikan fungsi untuk menghapus node dengan nilai tertentu
#==============================================================================

class node:
    def __init__(self, data):
        self.data = data #menyimpan nilai data yang akan disimpan
        self.next = None #pointer ke node berikutnya

class linkedlist:
    def __init__(self):
        self.head = None #node pertama dalam linked list
        self.tail = None #node terakhir 
    
    def insert_at_end(self, data):
        new_node = node(data) #membuat node baru
        
        if not self.head: #jika linked list kosong
            self.head = new_node 
            self.tail = new_node #tail menunjuk ke node pertama
        else:
            self.tail.next = new_node #sambung tail dengan node baru
            self.tail  = new_node #update tail ke node baru

    def display(self):
            temp = self.head
            while temp: 
                print(temp.data, end="->")
                temp = temp.next    #pindah ke node berikutnya
            print("null") #tanda akhir linked list

    def delete_node(self, key):
        temp = self.head 
        if temp and temp.data == key:
            self.head = temp.next
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None: #jika data tidak ditemukan 
            return
        prev.next = temp.next

    
#menambah data ke linked list
p = linkedlist()
p.insert_at_end(3)
p.insert_at_end(5)
p.insert_at_end(13)
p.insert_at_end(2)

print("Sebelum dihapus : ")
p.display()

p.delete_node(5) #menghapus node dengan nilai tertentu

print("Setelah dihapus : ")
p.display()


