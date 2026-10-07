# Sistem Manajemen Penjualan Alat Camping
## Deskripsi Program
Program ini merupakan penerapan Pemrograman Berorientasi Objek (PBO) menggunakan Python dengan menerapkan beberapa konsep PBO seperti class, object, atribut class, atribut instance, encapsulation, property, setter, class method, dan static method 

Program ini juga menerapkan inheritance(pewarisan) dan Relasi UML.

## Penerapan Relasi UML
1. Asosiasi: Pada program ini, class `pelanggan` menggunakan class `AlatCamping` lewat method `beli_alat()`. Objek alat diterima sebagai parameter method dan tidak disimpan sebagai atribut, sehingga kedua objek tetap berdiri sendiri.

2. Agregasi: Pada program ini, class `Kategori_Alat` menampung objek `AlatCamping` yang dibuat di luar class, lalu dimasukkan ke dalam list `daftar_alat`. Jika kategori dihapus, objek alat tetap ada.

3. Komposisi: Pada program ini, class `Transaksi` terdiri dari `DetailTransaksi`. Objek `DetailTransaksi` dibuat langsung di dalam `__init__` milik `Transaksi`, sehingga tidak berdiri sendiri dan ikut hilang jika transaksinya dihapus.

## Penerapan Inheritance (Pewarisan)
Superclass : `AlatCamping` memiliki Subclass : `Tenda` dan `Jaket`

Penerapan super().init yaitu pada subclass yaitu `tenda` 
```python
def __init__(self, id_alat, nama, harga, stok, kapasitas):
    super().__init__(id_alat, nama, harga, stok)
    self.kapasitas = kapasitas
``` 
dan `jaket`
```python
def __init__(self, id_alat, nama, harga, stok, ukuran):
    super().__init__(id_alat, nama, harga, stok)
    self.ukuran = ukuran
```

Subclass `tenda` memiliki atribut spesifik yaitu atribut kapasitas, Subclass `jaket` memiliki atribut spesifik yaitu atribut ukuran.

Method Overriding di terapkan pada subclass `tenda` 
```python
def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas: {self.kapasitas} orang")
        print()
```

Atribut protected di terapkan pada atribut `_stok` di class `AlatCamping`
```python
class AlatCamping:
    nama_toko = "Camping Yuk"
    Total_alat = 0

    def __init__(self, id_alat,nama, harga, stok):
        self.__id_alat = id_alat
        self.nama = nama
        self.harga = harga
        self._stok = stok
```

Atribut Private di terapkan pada atribut `__id_alat` di class `AlatCamping`
```python
class AlatCamping:
    nama_toko = "Camping Yuk"
    Total_alat = 0

    def __init__(self, id_alat,nama, harga, stok):
        self.__id_alat = id_alat
        self.nama = nama
        self.harga = harga
        self._stok = stok
```

## Pengujian Program
### Pengujian Pada Class AlatCamping, Subclass(Tenda, jaket), Kategori_Alat
``` python
produk1 = tenda("AL001", "Tenda 2 orang", 500000, 10, 10)
produk2 = jaket("AL002", "Jaket Gunung", 150000, 15, "M")
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
kategori1 = Kategori_Alat("Tenda")
kategori2 = Kategori_Alat("Jaket")
```
membuat kategori yang terdiri kategori1 = Tenda dan kategori2 = Jaket
```python
kategori1.tambah_alat(produk1)
kategori2.tambah_alat(produk2)
```
menambahkan produk1(tenda) ke dalam kategori1 dan menambahkan produk2(jaket) ke dalam kategori2
```python
kategori1.tampilkan_alat()
kategori2.tampilkan_alat()
```
disini saya memanggil method tampilkan_alat() untuk menampilkan informasi kategori dan informasi produk yang telah kita buat sebelumnya.
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
### Pengujian Pada Class Pelanggan
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
```python
pelanggan1.beli_alat(produk1, 3)
pelanggan2.beli_alat(produk2, 5)
```
memanggil method beli_alat() pada objek pelanggan1 dan pelanggan2 untuk membeli produk. pelanggan1 membeli 3 produk1 (tenda) dan pelanggan2 membeli 5 produk2 (jaket). Ini adalah penerapan asosiasi, karena objek alat dikirim lewat parameter method dan tidak disimpan di dalam class pelanggan. Stok alat otomatis berkurang, sehingga stok produk1 menjadi 9 (12 - 3) dan stok produk2 menjadi 10 (15 - 5).
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