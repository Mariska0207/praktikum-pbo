# Sistem Manajemen Penjualan Alat Camping

## Deskripsi Program
Program ini merupakan penerapan Pemrograman Berorientasi Objek (PBO) menggunakan Python dengan studi kasus penjualan alat camping, pelanggan, dan transaksi.

Program terdiri dari tiga class utama, yaitu AlatCamping, pelanggan, dan Transaksi.

Program menerapkan beberapa konsep PBO seperti class, object, atribut class, atribut instance, encapsulation, property, setter, class method, dan static method.

## Struktur Class
### 1. Class AlatCamping
Class ini memiliki atribut kelas, yaitu:
1. nama_toko untuk menyimpan nama toko, yaitu "Camping Yuk".
2. Total_alat atribut class yang digunakan untuk menghitung jumlah alat camping

Class ini juga memiliki atribut instance, yaitu:
1. nama untuk menyimpan nama produk (bersifat publik)
2. harga untuk menyimpan harga produk (bersifat publik)
3. __stok untuk menyimpan banyaknya stok produk (bersifat private)

Method pada Class ini, yaitu:
1. tampilkan_info() digunakan untuk menampilkan informasi alat camping
2. tambah_stok() digunakan untuk menambahkan jumlah stok

pada class ini juga terdapat stok yang diberi decorator(@property) digunakan untuk mengakses nilai stok dan juga ada stok.setter digunakan untuk mengubah nilai stok sekaligus melakukan validasi agar stok tidak bernilai negatif.
Setiap kali objek AlatCamping dibuat, nilai Total_alat akan bertambah satu.

### 2. Class Pelanggan
Class ini memiliki atribut instance, yaitu:
1. id_pelanggan untuk menyimpan Id pelanggan (bersifat publik)
2. nama untuk menyimpan nama pelanggan (bersifat publik)
3. __no_hp untuk menyimpan nomor HP pelanggan (bersiifat private)

Method pada Class ini, yaitu:
1. info_pelanggan() digunakan untuk menampilkan informasi pelanggan

Pada class ini juga terdapat no_hp yang diberi decorator(@property) digunakan untuk mengakses no_hp dan juga ada no_hp.setter digunakan untuk mengubah no_hp sekaligus melakukan validasi agar panjang no_hp tidak boleh kurang atau sama dengan 10

### 3. Class Transaksi
Class ini memiliki atribut kelas, yaitu:
1. pajak yang menyimpan nilai pajak transaksi, memiliki nilai awal 10%

Class ini juga memiliki atribut instance, yaitu:
1. id_transaksi untuk menyimpan Id transaksi (berifat publik)
2. produk untuk menyimpan produk yang digunakan dalam transaksi (berifat publik)
3. jumlah menyimpan jumlah produk yang di beli (berifat publik)
4. total_harga untuk menyimpan total harga transaksi (berifat publik)

Method pada Class ini, yaitu:
1. bukti_transaksi() digunakan untuk menampilkan informasi transaksi
2. ubah_pajak() ini merupakan class method yang digunakan untuk mengubah nilai pajak(atribut kelas)
3. hitung_total_harga ini merupakah static method yang digunakan untuk menghitung total harga berdasarkan harga dan jumlah produk

## Pengujian Program
### pengujian pada Class AlatCamping
``` python
produk1 = AlatCamping("Tenda 2 orang", 500000, 10)
produk2 = AlatCamping("Sleeping Bag", 150000, 15) 
```
pertama-tama saya membuat 2 objek yaitu tenda 2 orang dan sleeping bag.
```python
produk1.tampilkan_info()
produk2.tampilkan_info()
```
disini saya memanggil method tampilkan_info() untuk menampilkan informasi produk sesuai objek yang telah kita buat sebelumnya.
```python
produk1.tambah_stok(5)
```
melakukan penambahan stok sebanyak 5 kepada produk1.
```python
produk2.tambah_stok(-3)
```
melakukan pengujian penambahan stok bernilai negatif, disini akan menampilkan pesan error "Jumlah yang ditambahkan harus lebih dari 0" karena tidak boleh memasukkan stok kurang dari 0.
```python
produk1.stok = 12
```
melakukan pengubahan stok menjadi 12 kepada produk1.
```pyhon
produk1.stok = -5
```
melakukan pengubahan stok menjadi -5, disini akan ditampilkan pesan error "Stok tidak boleh negatif" karena tidak boleh memasukkan stok kurang dari 0. 
```python
produk1.stok = "lima"
```
melakukan perubahan stok, disini akan ditampilkan pesan error "stok harus angka" karena disini kita memasukkan string("lima") sedangkan stok bertipe integer
### pengujian pada Class Pelanggan
```python
pelanggan1 = pelanggan("PL001", "Febri", "082251567811")
pelanggan2 = pelanggan("PL002", "Yanti", "08224153753")
```
membuat 2 objek pada class pelanggan. 
```python
pelanggan1.info_pelanggan()
pelanggan2.info_pelanggan()
```
disini saya memanggil method info_pelanggan() untuk menampilkan informasi pelanggan sesuai objek yang telah kita buat sebelumnya.
```python
pelanggan1.no_hp = "081365478"
```
melakukan pengubahan no_hp menjadi "081365478", disini akan di tampilkan pesan error "Nomor HP harus memiliki minimal 11 digit" karena nomor_hp yang di masukkan kurang dari 10.
```python
pelanggan2.no_hp = 124442790081
```
melakukan pengubahan no_hp menjadi 124442790081, disini akan di tampilkan pesan error "Nomor HP harus berupa string", karena tipe data no_hp harus string sedangkan kita memasukkan angka yg bertipe data integer
### pengujian pada Class Transaksi
```python
Trans1 = Transaksi("TR01", produk1, 2, 1000000)
Trans2 = Transaksi("TR02", produk2, 1, 150000)
```
membuat 2 objek pada class pelanggan.
```python
Trans1.bukti_transaksi()
Trans2.bukti_transaksi()
```
disini saya memanggil method bukti_transaksi() untuk menampilkan bukti transaksi sesuai objek yang telah kita buat sebelumnya.
```python
print("pajak awal:", Transaksi.pajak)
Transaksi.ubah_pajak(0.15)
print("pajak baru:", Transaksi.pajak)
```
outpul awal akan menampilkan pajak awal 0.1 , pada perintah ubah_pajak berfungsi untuk mengubah pajak dalam class transaksi disini saya mengubah pajak menjadi 0.15, dan pada baris akhir berfungsi untuk menampilkan pajak setelah diubah.
```python
hitung_total = Transaksi.hitung_total_harga(produk1.harga, 3)
print(f"Total harga untuk 3 {produk1.nama}: {hitung_total}")
```
disini akan menampilkan total harga sesuai perhitungan yaitu harga * jumlah