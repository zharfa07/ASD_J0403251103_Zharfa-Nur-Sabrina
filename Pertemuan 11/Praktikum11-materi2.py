# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Materi 2 : Implementasi BFS (Queue)
# ===================================================

# struktur data unntuk membuat antrian, kita gunakan dari library collections bawaan phyton
from collections import deque

# representasi graph (identifikasi tiap tetangga, jika tidak ada tetangga tetap dituliskan menjadi kosong)
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def bfs(graph, start):
    # fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph 
    # start : node awal penelusuran

    # queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    # variabel yang digunakan node yang sudah diproses/dikunjungi/dibaca
    visited = set()

    # masukkan node awal ke queue
    queue.append(start)

    # tandai node awal yang sudah masuk ke queue sebagai node yang sudah dikunjungi
    visited.add(start)

# penelusuran ke node berikutnya dengan looping ambil node atau data yang di deque
    while queue: 
        # mengambil node paling depan dari queue
        node = queue.popleft()

        # tampilkan node yang sedang dikunjungi
        print(node, end=" ")

        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            if neighbor not in visited:
                # jika tetangga belum dikunjungi
                visited.add(neighbor) 
                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

# menjalankan BFS dari node A
bfs(graph, 'A')