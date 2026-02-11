#==============================================================================
#Praktikum 2: Linked List
#Latihan 1 : Implementasikan fungsi untuk menghapus node dengan nilai tertentu
#==============================================================================

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

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next

    

p = linkedlist()
p.insert_at_end(3)
p.insert_at_end(5)
p.insert_at_end(13)
p.insert_at_end(2)

print("Sebelum dihapus : ")
p.display()

p.delete_node(5)

print("Setelah dihapus : ")
p.display()
