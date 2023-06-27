# Asep permadi Nim F55121049
 
# TSP Djiktra
Fungsi Bubble Sort (bubble_sort):
Pada baris 5, panjang array n diinisialisasi dengan panjang array input.
Waktu Komputasi: Program mencatat waktu mulai pengurutan menggunakan start_time = time.time().
Loop pertama (baris 7-9) digunakan untuk mengiterasi melalui array dari indeks 0 hingga n-2.
Loop kedua (baris 8-9) digunakan untuk membandingkan dan menukar elemen jika elemen sebelumnya lebih besar dari elemen saat ini.
Pada baris 13-18, program mencetak iterasi pertama dan terakhir jika iterasi tersebut berada di dalam 5 iterasi pertama atau 5 iterasi terakhir.
Setelah selesai melakukan pengurutan, program mencetak array yang telah diurutkan, waktu yang diperlukan, dan pesan akhir.

Fungsi Insertion Sort (insertion_sort):
Pada baris 24, panjang array n diinisialisasi dengan panjang array input.
Waktu Komputasi: Program mencatat waktu mulai pengurutan menggunakan start_time = time.time().
Loop pertama (baris 26-31) digunakan untuk mengiterasi melalui array dari indeks 1 hingga n-1.
Loop kedua (baris 28-30) digunakan untuk memindahkan elemen-elemen yang lebih besar dari elemen saat ini ke posisi yang benar di sebelah kanan.
Pada baris 35-40, program mencetak iterasi pertama dan terakhir jika iterasi tersebut berada di dalam 5 iterasi pertama atau 5 iterasi terakhir.
Setelah selesai melakukan pengurutan, program mencetak array yang telah diurutkan, waktu yang diperlukan, dan pesan akhir.

Main Program:
Pada baris 46, array data awal dicetak.
Pada baris 48, user diminta untuk memasukkan pilihan algoritma pengurutan (bubble/insertion).
Jika pilihan adalah "bubble" (baris 50-51), fungsi bubble_sort dipanggil dengan salinan data array.
Jika pilihan adalah "insertion" (baris 52-53), fungsi insertion_sort dipanggil dengan salinan data array.
Jika pilihan tidak valid, pesan kesalahan dicetak.

# Bubble sort dan insertion sort
Fungsi bubble_sort(arr) digunakan untuk mengurutkan array menggunakan algoritma bubble sort. Dalam setiap iterasi, elemen tetangga/sebelah dibandingkan dan ditukar jika urutannya tidak benar. Jika tidak ada swap dalam iterasi, proses pengurutan berhenti karena array sudah terurut. Waktu eksekusi pengurutan dihitung oleh modul time.Fungsi  insertion_sort(arr) digunakan untuk mengurutkan array menggunakan algoritma insertion sort. Dengan setiap iterasi, elemen yang akan ditambahkan ditempatkan pada posisi yang benar di bagian terurut dari baris sebelumnya. Waktu eksekusi pengurutan juga dihitung menggunakan mesin waktu. Fungsi print_iteration_results(arr, algorithm_name) digunakan untuk mencetak hasil iterasi penyortiran pertama dan terakhir. Iterasi pertama mencetak 5 elemen pertama dari array yang diurutkan sedangkan iterasi terakhir mencetak 5 elemen terakhir dari array yang diurutkan.Fungsi print_execution_time(execution_time) digunakan untuk mencetak waktu eksekusi dari urutan. Fungsi print_before_after(arr, algorithm_name) digunakan untuk mencetak array sebelum dan sesudah pengurutan. Pertama matriks asli dicetak, kemudian matriks yang diurutkan setelah disortir oleh algoritma yang dipilih.Array yang akan diurutkan ditentukan langsung dalam kode program.Pengguna akan diminta untuk memilih algoritma pengurutan antara bubble sort (opsi 1) dan insertion sort (opsi 2).
Setelah memilih algoritme, program memanggil fungsi print_before_after(arr, algorithm_name) untuk mencetak tabel sebelum dan sesudah penyortiran, dan memanggil fungsi print_iteration_results(sorted_queue, algorithm_name) untuk mencetak iterasi pertama dan terakhir dari antrian. Terakhir, program mencetak waktu eksekusi dari jenis dengan memanggil fungsi print_execution_time(execution_time). 
