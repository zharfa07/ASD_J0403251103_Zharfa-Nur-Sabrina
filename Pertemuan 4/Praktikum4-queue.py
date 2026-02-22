# ================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ================================================
# Implementasi Dasar : Queue Berbasis Linked List
# ================================================

# Membuat class node (merupakan unit dasar dari Linked List)
class Node: 
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke note berikutnya (awal=none)

# Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def  is_empty(self):
        return self.front is None 
        

    def enqueue(self, data): #tambah belakang
        # Menambah data di belakang (rear)
        nodeBaru = Node(data)

        # JIka queue kosong, front dan rear meunjuk ke node 
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # jika queue tidak kosong :
        # rear lama menunjuk ke node baru
        # self.rear.next = nodeBaru #rear saja menunjuk ke rear lama, next dari rear yang lama
        # rear pindah ke node baru
        self.rear = nodeBaru #menggeser rear, karena rear adalah node baru
        self.rear.next = nodeBaru
                 

    def dequeue(self): 
        # menghapus data dari depan

        # 1) ambil data yang paling depan
        data_terhapus = self.front.data

        # 2) geser front ke node berikutnya
        self.front = self.front.next 

        # 3) jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None: 
            self.rear = None
        return data_terhapus


    def tampilkan(self):
        current = self.front
        print("Front ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

# Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()
# sampai none
q.dequeue()
q.tampilkan()