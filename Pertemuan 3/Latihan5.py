#==============================================================================================================
#Praktikum 2: Linked List
#Latihan 5 : Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru
#==============================================================================================================
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def insert_at_end(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail  = new_node

    def display(self):
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next    
            print("null")

    def reverve(self):
        prev = None
        temp = self.head 
        while temp:
            next_node = temp.next
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

r.reverve()
print('Linked list setelah dibalik : ')
r.display()
