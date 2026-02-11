#==============================================================================================================
#Praktikum 2: Linked List
#Latihan 5 : Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru
#==============================================================================================================
class node:
    def __init__(self, data):
        self.data = data #menyimpan nilai data yang akan disimpan
        self.next = None #pointer ke node berikutnya

class linkedlist:
    def __init__(self):
        self.head = None #node pertama 
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
            temp = self.head #mulai dari head
            while temp: 
                print(temp.data, end="->")
                temp = temp.next    #pindah ke node berikutnya
            print("null") #tanda akhir linked list

    def reverse(self):
        prev = None #node sebelumnya
        temp = self.head 
        while temp:
            next_node = temp.next #simpan ke node berikutnya
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

r = linkedlist()
r.insert_at_end(1)
r.insert_at_end(2)
r.insert_at_end(3)
r.insert_at_end(4)
r.insert_at_end(5)
print('Linked list sebelum dibalik : ')
r.display()

print("\n")

r.reverse()
print('Linked list setelah dibalik : ')
r.display()

