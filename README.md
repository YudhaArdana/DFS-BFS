
**SOAL**
# <img src="WhatsApp%20Image%202021-09-29%20at%2022.35.47.jpeg">

# DFS
**Baris 1-12**: Grafik bergambar diwakili menggunakan daftar adjacency - cara mudah untuk melakukannya dengan Python adalah dengan menggunakan kamus struktur data. Setiap simpul memiliki daftar node yang berdekatan yang disimpan.

**Baris 14**: visited adalah set yang digunakan untuk melacak node yang dikunjungi.

**Baris 16-21**: dfs akan memeriksa apakah node saat ini belum dikunjungi - jika ya, itu ditambahkan dalam set yang dikunjungi. Kemudian untuk setiap tetangga dari node saat ini, fungsi dfs dipanggil lagi. Kasus dasar dipanggil ketika semua node dikunjungi.

**Baris 23**: fungsi dfs dipanggil dan melewati visited, dan 1, yang merupakan simpul awal. 
#

# BFS
**Baris 1-12**: Grafik bergambar diwakili menggunakan daftar adjacency - cara mudah untuk melakukannya dengan Python adalah dengan menggunakan kamus struktur data. Setiap simpul memiliki daftar node yang berdekatan yang disimpan.

**Baris 14**: visited adalah set yang digunakan untuk melacak node yang dikunjungi.

**Baris 15**: queue adalah daftar yang digunakan untuk melacak node saat dalam antrian.

**Baris 17-28**: bfs memeriksa dan menambahkan node awal ke daftar yang dikunjungi dan antrian. Kemudian, ketika antrian mengandung elemen, antrian terus mengeluarkan node dari antrian, menambahkan tetangga node tersebut ke antrian jika belum dikunjungi, dan menandainya sebagai dikunjungi.

**Baris 30**: Argumen dari fungsi bfs adalah daftar yang dikunjungi, grafik dalam bentuk kamus, dan node awal 1. 


source: github.com/kmayutrisna