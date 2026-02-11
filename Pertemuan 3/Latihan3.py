#==============================================================================
#Praktikum 2: Linked List
#Latihan 3 : Implementasikan Pencarian pada node tertentu Double Linked List
#==============================================================================

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublylinkedlist:
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
            new_node.prev = self.tail
            self.tail = new_node
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

dll = doublylinkedlist()
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)
key = 0 
if dll.search(key):
    print(f"elemen {key} ditemukan")
else:
    print(f"elemen {key} tidak ditemukan")