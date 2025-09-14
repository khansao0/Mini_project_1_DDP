# Mini project 1 ( DDP )
PRAKTIKUM MINI PROJECT DDP - Sistem Manajemen Stok Cemilan 

Nama : Qonitah Khansa' Ayu Madani Alamsyah  
NIM  : 2509116113  
Kelas: Sistem Informasi C'25

# Flowchart Sistem Manajemen Stok Cemilan
![Flowchart_Mini_Project_1_Qonitah_Khansa'_Ayu_Madani_Alamsyah](https://github.com/user-attachments/assets/4beda366-16b9-4ad0-aaa5-fdf01f0c2ccf)  

# Output Menu  
![Output_Mini_Project_1](https://github.com/user-attachments/assets/399d9535-79c8-4669-92ed-4f57c2131d43)  

Program ini merupakan mini project 1 berbasis Python yang dirancang untuk membantu pengguna mencatat dan mengelola stok cemilan secara praktis. Ketika dijalankan, program akan langsung menampilkan menu utama yang terdiri dari empat pilihan. Berikut penjelasan dari 4 pilihan menu utama dari program saya yang berjudul "Sistem Manajemen Stok Cemilan"  

  1. Tambah Cemilan

     Menu ini digunakkan untuk menambahkan data cemilan baru ke dalam sistem. Pengguna akan diminta untuk memasukkan/ input:
     - Nama Cemilan (bebas):
     - Rasa Cemilan (manis/asin/pedas):
     - Jumlah Stok (bebas):
     - Status stok (ada/habis/expired):

Setelah data diinput, program akan menyimpannya dalam bentuk tuple dan menambahkannya ke list stok_cemilan. Output yang muncul adalah pesan konfirmasi bahwa cemilan berhasil ditambahkan.

  2. Lihat Daftar Cemilan

  Pilihan ini digunakan untuk menampilkan semua data cemilan yang telah dicatat. Informasi yang ditampilkan meliputi:
      - Nomor urut
      - Nama cemilan
      - Rasa
      - Jumlah stok
      - Status
Jika belum ada data yang tercatat, maka akan muncul pesan:
"Belum ada cemilan yang dicatat nih."

  3. Hapus Cemilan

     Menu ini memungkinkan pengguna untuk menghapus cemilan dari daftar berdasarkan nomor urut. Program akan menampilkan daftar cemilan terlebih dahulu, lalu meminta input nomor cemilan yang ingin dihapus.

Jika nomor valid, data akan dihapus dan muncul pesan:
"Oke, cemilan sudah dihapus."

Jika nomor tidak valid, akan muncul pesan:
"Nomor tidak valid."  

  4. Keluar

     Pilihan ini digunakan untuk keluar dari program. Setelah dipilih, program akan berhenti dan menampilkan pesan penutup yang ramah:
"Program ditutup. Jangan lupa beli cemilan kalau sudah habis ya!"

# Bagaimana jika saya menginput Menu selain dari (1/2/3/4) ?  
![Output_Mini_Project_1_tidak_valid](https://github.com/user-attachments/assets/ccfb6d73-17da-4f86-ab2e-24d8e3b881ba)  

Dalam program berbasis menu, penting untuk memastikan bahwa pengguna hanya dapat memilih opsi yang tersedia yaitu (1/2/3/4).  
-  Tujuan : Mencegah program error karena input yang tidak dikenali. <br> Menjaga alur program tetap berjalan tanpa gangguan.

Jika pengguna memasukkan angka selain 1, 2, 3, atau 4, program akan menampilkan pesan berikut: <br> 






