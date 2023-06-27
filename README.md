# Asep permadi Nim F55121049
 
# TSP Djiktra
BUBBLE SORT:
Waktu Komputasi: Algoritma Bubble Sort memiliki kompleksitas waktu rata-rata dan terburuk O(n^2), di mana n adalah jumlah elemen dalam data. Pada setiap iterasi, dua elemen dibandingkan dan ditukar jika urutannya salah. Ini dilakukan secara berulang hingga seluruh data diurutkan dengan benar.
Iterasi Pertama dan Terakhir: Program mencetak hasil iterasi pertama dan terakhir dari Bubble Sort.
Before and After: Program mencetak data sebelum dan setelah diurutkan menggunakan Bubble Sort.
Waktu Komputasi: Program juga mencetak waktu komputasi yang diperlukan untuk menjalankan Bubble Sort.

INSERTTION SORT:
Waktu Komputasi: Algoritma Insertion Sort memiliki kompleksitas waktu rata-rata dan terburuk O(n^2), di mana n adalah jumlah elemen dalam data. Pada setiap iterasi, elemen yang sedang diproses disisipkan ke posisi yang benar di antara elemen yang sudah terurut sebelumnya.
Iterasi Pertama dan Terakhir: Program mencetak hasil iterasi pertama dan terakhir dari Insertion Sort.
Before and After: Program mencetak data sebelum dan setelah diurutkan menggunakan Insertion Sort.
Waktu Komputasi: Program juga mencetak waktu komputasi yang diperlukan untuk menjalankan Insertion Sort.

MAIN PROGRAM:
Data Input: Program menginisialisasi data yang akan diurutkan menggunakan Bubble Sort atau Insertion Sort.
User Input: Program meminta pilihan pengguna untuk memilih algoritma pengurutan (bubble/insertion).
Pemanggilan Fungsi: Berdasarkan pilihan pengguna, program memanggil fungsi yang sesuai untuk menjalankan pengurutan menggunakan algoritma yang dipilih.
Analisis: Program tidak memberikan analisis langsung, tetapi memberikan output yang memungkinkan pengguna melihat hasil iterasi, waktu komputasi, dan perbandingan sebelum dan sesudah pengurutan.

# Bubble sort dan insertion sort
Fungsi bubble_sort(arr) digunakan untuk mengurutkan array menggunakan algoritma bubble sort. Dalam setiap iterasi, elemen tetangga/sebelah dibandingkan dan ditukar jika urutannya tidak benar. Jika tidak ada swap dalam iterasi, proses pengurutan berhenti karena array sudah terurut. Waktu eksekusi pengurutan dihitung oleh modul time.Fungsi  insertion_sort(arr) digunakan untuk mengurutkan array menggunakan algoritma insertion sort. Dengan setiap iterasi, elemen yang akan ditambahkan ditempatkan pada posisi yang benar di bagian terurut dari baris sebelumnya. Waktu eksekusi pengurutan juga dihitung menggunakan mesin waktu. Fungsi print_iteration_results(arr, algorithm_name) digunakan untuk mencetak hasil iterasi penyortiran pertama dan terakhir. Iterasi pertama mencetak 5 elemen pertama dari array yang diurutkan sedangkan iterasi terakhir mencetak 5 elemen terakhir dari array yang diurutkan.Fungsi print_execution_time(execution_time) digunakan untuk mencetak waktu eksekusi dari urutan. Fungsi print_before_after(arr, algorithm_name) digunakan untuk mencetak array sebelum dan sesudah pengurutan. Pertama matriks asli dicetak, kemudian matriks yang diurutkan setelah disortir oleh algoritma yang dipilih.Array yang akan diurutkan ditentukan langsung dalam kode program.Pengguna akan diminta untuk memilih algoritma pengurutan antara bubble sort (opsi 1) dan insertion sort (opsi 2).
Setelah memilih algoritme, program memanggil fungsi print_before_after(arr, algorithm_name) untuk mencetak tabel sebelum dan sesudah penyortiran, dan memanggil fungsi print_iteration_results(sorted_queue, algorithm_name) untuk mencetak iterasi pertama dan terakhir dari antrian. Terakhir, program mencetak waktu eksekusi dari jenis dengan memanggil fungsi print_execution_time(execution_time). 
