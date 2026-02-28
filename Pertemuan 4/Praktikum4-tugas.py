# =====================================================================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# =====================================================================================================

# =====================================================================================================
# Tugas Hands-on : Sistem Antrian Pelanggan Bengkel Motor (queue berbasis linked list)
# =====================================================================================================

class node:
    def __init__(self, nomor, nama, servis):
        # menyimpan data pelanggan
        self.nomor = nomor      #nomor antrian
        self.nama = nama        #nama pelanggan
        self.servis = servis    #jenis servis

        # pointer ke node berikutnya
        self.next = None

class queueBengkel:
    def __init__(self):
        # pointer depan (pelanggan pertama)
        self.front = None #queue awalnya kosong
        # pointer belakang (pelanggan terakhir)
        self.rear  = None

    def is_empty(self):
        # ketika queue kosong maka front = rear = none
        return self.front is None
    
    def enqueue(self, nomor, nama, servis): #memindahkan pointer
        nodeBaru = node(nomor, nama, servis)

        # jika data baru masuk dari queue yang kosong maka data baru = front= rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru   

    # menghapus data paling depan (memberikan layanan antrian bengkel motor)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada Pelanggan yang dilayani")
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
        # jika antrian kosong, tampilan pesan muncul dan fungsi berhenti
        if self.is_empty():
            print("Antrian kosong")
            return
        
        print("Daftar antrian Pelanggan (Front -> Rear) : ")
        
        current = self.front    # pointer untuk traversal
        no = 1                  # variabel nomor urut tampilan

        # travesal dari front sampai rear
        while current is not None: 
            # menampilkan data pelanggan
            print(f'{no}. {current.nomor} - {current.nama} - {current.servis}')
            # pindah ke node berikutnya
            current = current.next
            # menambah nomor urut
            no += 1


# Program Utama
def main():
    # Instantiasi queue
    q = queueBengkel()

    while True:
        print("===== Sistem Antrian Bengkel =====")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4) : ").strip()

        if pilihan == "1":
            no = input("No Antrian : ") 
            nama = input("Nama : ") 
            servis = input("Servis : ") 
            q.enqueue(no, nama, servis) #menambah data ke queue
            print("Pelanggan berhasil ditambahkan ke antrian")
        
        elif pilihan == "2":
            dilayani = q.dequeue() #menghapus dan mengambil data paling depan
            print(f"Pelanggan dilayani : {dilayani.nomor} - {dilayani.nama} - {dilayani.servis}")

        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan == "4":
            print("Program selesai : Terima kasih ~")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi (1-4)")

# menjalankan program utama
if __name__ == "__main__":
    main() 