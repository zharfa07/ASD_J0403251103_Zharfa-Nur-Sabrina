# ================================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ================================================================================================================

# ================================================================================================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi  Queue => 
# Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
# Dequeue : memindahkan pointer front (menghapus data dari head/depan)
# Stack ==> Front -> C -> B -> A -> None (dari depan)
# Queue ==> Front -> A -> B -> C -> Rear (dari belakang, yang baru datang di belakang, yang akan dilayani yang awal)
# ================================================================================================================


# 1) Mendefinisikan Node (Unit dasar linked list)
class node:
    def __init__(self, nim, nama):  #kontruktor, instantiasi
        self.nim  = nim             #Menyimpan NIM Mahasiswa
        self.nama = nama            #Menyimpan Nama Mahasiswa
        self.next = None            #Pointer ke node berikutnya 

# 2) Mendefinisikan Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None #queue awalnya kosong
        self.rear  = None

    def is_empty(self):
        # ketika queue kosong maka front = rear = none
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama): #memindahkan pointer
        nodeBaru = node(nim, nama)

        # jika data baru masuk dari queue yang kosong maka data baru = front= rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru        
        

    # menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang dilayani")
            return None
        
        # lihat data bagian front, simpan ke variabel data yang akan dihapus (yang akan dilayani)
        node_dilayani = self.front

        # geser pointer front ke next front
        self.front = self.front.next

        # jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        print("Daftar antrian mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f'{no}. {current.nim} - {current.nama} ')
            current = current.next
            no += 1

# Program Utama
def main():
    # Instantiasi queue
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4) : ").strip()
        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")
        
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan == "4":
            print("Program selesai : Terima kasih ~")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi (1-4)")

if __name__ == "__main__":
    main()