# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
# ===================================================

# struktur data unntuk membuat antrian, kita gunakan dari library collections bawaan phyton
from collections import deque

# representasi graph (identifikasi tiap tetangga, jika tidak ada tetangga tetap dituliskan menjadi kosong)
graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
} 

def bfs(graph, start): 
# fungsi untuk melakukan penelusuran graph dengan BFS
# graph : dictionary yang menyimpan struktur dari graph 
# start : node awal penelusuran

    visited = set()         #variabel yang digunakan node yang sudah diproses/dikunjungi/dibaca
    queue = deque([start])  #queue digunakan untuk menyimpan node yang akan diproses / dibaca
    visited.add(start)      #tandai node awal yang sudah masuk ke queue sebagai node yang sudah dikunjungi
        
# penelusuran ke node berikutnya dengan looping ambil node atau data yang di deque
    while queue: 
        node = queue.popleft()              #mengambil node paling depan dari queue
        print(node, end=" ")                #tampilkan node yang sedang dikunjungi
        
        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:        
            if neighbor not in visited:    
                visited.add(neighbor)       #jika tetangga belum dikunjungi
                queue.append(neighbor)      #masukkan tetangga ke queue untuk diproses nanti

# menjalankan BFS dari node Rumah
print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 


# Pertanyaan Analisis 
# 1. Node mana yang dikunjungi pertama?  
#     -> node yang dikunjungi pertama BFS dimulai dari node awal (start) yaitu 'Rumah'
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?  
#     -> Karena penelusuran BFS node dilakukan per level, jadi jalur pertama yang ditemukan adalah jalur terdekat
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#     -> Urutan BFS akan berubah tergantung hubungan antar node dan urutan tetangga pada graph
#        Jika urutan list tetangga diubah, maka hasil BFS ikut berubah
#        Jika ada cabang baru, urutan juga berubah