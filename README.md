# Mini project 1 ( DDP )
PRAKTIKUM MINI PROJECT 1 DDP - Sistem Manajemen Stok Cemilan 

Nama : Qonitah Khansa' Ayu Madani Alamsyah  
NIM  : 2509116113  
Kelas: Sistem Informasi C'25

# Flowchart Sistem Manajemen Stok Cemilan
![Flowchart_Mini_Project_1_Qonitah_Khansa'_Ayu_Madani_Alamsyah](https://github.com/user-attachments/assets/4beda366-16b9-4ad0-aaa5-fdf01f0c2ccf)  

# Output Menu  
Program ini menggunakan struktur while True untuk menjalankan menu secara berulang hingga pengguna memilih keluar. Setiap pilihan menu memiliki fungsi spesifik  

![Output_Mini_Project_1](https://github.com/user-attachments/assets/399d9535-79c8-4669-92ed-4f57c2131d43)  

Program ini merupakan mini project 1 berbasis Python yang dirancang untuk membantu pengguna mencatat dan mengelola stok cemilan secara praktis. Ketika dijalankan, program akan langsung menampilkan menu utama yang terdiri dari empat pilihan. Berikut penjelasan dari 4 pilihan menu utama dari program saya yang berjudul "Sistem Manajemen Stok Cemilan"  

Program ini menerapkan tiga dari empat proses dasar CRUD (Create, Read, Delete)

  1. Tambah Cemilan (Create)

     Menu ini digunakkan untuk menambahkan data cemilan baru ke dalam sistem. Pengguna akan diminta untuk memasukkan/ input:
     - Nama Cemilan (bebas):
     - Rasa Cemilan (manis/asin/pedas):
     - Jumlah Stok (bebas):
     - Status stok (ada/habis/expired):

Setelah data diinput, program akan menyimpannya dalam bentuk tuple dan menambahkannya ke list stok_cemilan. Output yang muncul adalah pesan konfirmasi bahwa cemilan berhasil ditambahkan.

  2. Lihat Daftar Cemilan (Read)

  Pilihan ini digunakan untuk menampilkan semua data cemilan yang telah dicatat. Informasi yang ditampilkan meliputi:
      - Nomor urut
      - Nama cemilan
      - Rasa
      - Jumlah stok
      - Status
Jika belum ada data yang tercatat, maka akan muncul pesan:
"Belum ada cemilan yang dicatat nih."  

  3. Hapus Cemilan (Delete)

     Menu ini memungkinkan pengguna untuk menghapus cemilan dari daftar berdasarkan nomor urut. Program akan menampilkan daftar cemilan terlebih dahulu, lalu meminta input nomor cemilan yang ingin dihapus.

Jika nomor valid, data akan dihapus dan muncul pesan:
"Oke, cemilan sudah dihapus."

Jika nomor tidak valid, akan muncul pesan:
"Nomor tidak valid."  

  4. Keluar (Exit)

     Pilihan ini digunakan untuk keluar dari program. Setelah dipilih, program akan berhenti dan menampilkan pesan penutup yang ramah:
"Program ditutup. Jangan lupa beli cemilan kalau sudah habis ya!"

# Bagaimana jika saya menginput Menu selain dari (1/2/3/4) ?  
![Output_Mini_Project_1_tidak_valid](https://github.com/user-attachments/assets/9cffb83a-f225-4559-a294-aeb6ae2d6729)


Dalam program berbasis menu, penting untuk memastikan bahwa pengguna hanya dapat memilih opsi yang tersedia yaitu (1/2/3/4).  
-  Tujuan : Mencegah program error karena input yang tidak dikenali. <br> Menjaga alur program tetap berjalan tanpa gangguan.

Jika pengguna memasukkan angka selain 1, 2, 3, atau 4, program akan menampilkan pesan seperti: <br> "Pilihan tidak dikenal, coba lagi." 🚫  

# Pilihan Menu Pertama (Tambah Cemilan)  
Jika masuk ke pilihan pertama, maka pengguna akan diminta untuk menginput data cemilan yang ingin dicatat. Data yang dimasukkan meliputi:
- Nama cemilan
- Rasa cemilan (manis/asin/pedas)
- Jumlah stok
- Status stok (ada/habis/expired)
Setelah semua data diisi, program akan menyimpan informasi tersebut dalam bentuk tuple dan menambahkannya ke dalam list stok_cemilan. Jika proses berhasil, akan muncul output berupa pesan:
"Yey! Cemilan berhasil ditambahkan!" 

<img width="757" height="185" alt="image" src="https://github.com/user-attachments/assets/4f0dace0-9b5b-4c9b-9f17-cc09da13549e" />
  
# Pilihan Menu Kedua (Lihat Daftar Cemilan)   
Jika masuk ke pilihan kedua, maka program akan menampilkan seluruh data cemilan yang sudah dicatat sebelumnya. Data yang ditampilkan akan seperti:
- Nomor urut
- Nama cemilan (nama cemilan yang di input)
- Rasa (manis/asin/pedas)
- Jumlah stok (berapa)
- Status (ada/habis/expired)
Namun, jika belum ada data yang dicatat atau list stok_cemilan masih kosong, maka akan muncul output dengan pesan:
"Belum ada cemilan yang dicatat nih."

![Output_Mini_Project_1_lihat_daftar_cemilan_belum_ada_daftar](https://github.com/user-attachments/assets/54fccd74-6128-4801-bde0-7aa7d668f9e2)

![Output_Mini_Project_1_lihat_daftar_cemilan](https://github.com/user-attachments/assets/ed93e450-7eae-46ed-b8cd-7ccd422c76c2)
  

# Pilihan Menu Ketiga (Hapus Daftar Cemilan)  
Jika pengguna memilih pilihan ketiga, maka program akan menampilkan daftar cemilan yang tersedia beserta nomor urutnya. Pengguna diminta untuk memilih nomor cemilan yang ingin dihapus. Program akan menampilkan daftar cemilan terlebih dahulu, lalu meminta input nomor yang ingin dihapus. Setelah penghapusan, akan muncul pesan konfirmasi.

Jika nomor yang dimasukkan valid, maka data cemilan akan dihapus dan muncul pesan:
"Oke, cemilan sudah dihapus."  

Namun jika nomor tidak sesuai atau di luar jangkauan, maka akan muncul output:
"Nomor tidak valid."  

![Output_Mini_Project_1_hapus_daftar_cemilan](https://github.com/user-attachments/assets/187999a9-98fd-47ba-a9f7-55bd004fb3ad)  

# Pilihan Menu Keempat (Keluar)  
Jika pengguna memilih pilihan keempat, maka program akan berhenti dan menampilkan pesan penutup:
"Program ditutup. Jangan lupa beli cemilan kalau sudah habis ya!"  

![Output_Mini_Project_1_input_keluar](https://github.com/user-attachments/assets/11a4715c-490a-4cac-9f38-4c8a7ca70998)  

# Tujuan Project  
Alasan saya membuat program python ini "Sistem Manajemen Stok Cemilan" karena : <br> Program ini dibuat sebagai solusi sederhana untuk mencatat stok cemilan agar tidak ada yang lupa, terutama bagi pengguna yang suka nyemil tapi sering lupa status stoknya.









