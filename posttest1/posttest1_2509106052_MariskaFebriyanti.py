class AlatCamping:
    nama_toko = "Camping Yuk"
    Total_alat = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.__stok = stok

        AlatCamping.Total_alat += 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if type(stok_baru) == int:
            if stok_baru < 0:
                print("Stok tidak boleh negatif")
            else:
                self.__stok = stok_baru
        else:
            print("stok harus angka")

    def tampilkan_info(self):
        print(f"Nama Alat Camping: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Stok: {self.stok}")
        print()

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print(f"Stok {self.nama} berhasil ditambahkan. Stok sekarang: {self.__stok}")
        else:
            print("Jumlah yang ditambahkan harus lebih dari 0")

class pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.__no_hp = no_hp

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, no_hp_baru):
        if type(no_hp_baru) == str:
            if len(no_hp_baru) < 11:
                print("Nomor HP harus memiliki minimal 11 digit")
            else:
                self.__no_hp = no_hp_baru
        else:
            print("Nomor HP harus berupa string")

    def info_pelanggan(self):
        print(f"ID Pelanggan: {self.id_pelanggan}")
        print(f"Nama Pelanggan: {self.nama}")
        print(f"No. HP: {self.__no_hp}")
        print()

class Transaksi:
    pajak = 0.1 

    def __init__(self, id_transaksi, produk, jumlah, total_harga):
        self.id_transaksi = id_transaksi
        self.produk = produk
        self.jumlah = jumlah
        self.total_harga = total_harga

    def bukti_transaksi(self):
        print(f"ID Transaksi: {self.id_transaksi}")
        print(f"Produk: {self.produk.nama}")
        print(f"Jumlah: {self.jumlah}")
        print(f"Total Harga: {self.total_harga}")
        print()

    @classmethod
    def ubah_pajak(cls, pajak_baru):
        cls.pajak = pajak_baru

    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah

produk1 = AlatCamping("Tenda 2 orang", 500000, 10)
produk2 = AlatCamping("Sleeping Bag", 150000, 15)

produk1.tampilkan_info()
produk2.tampilkan_info()

produk1.tambah_stok(5)
produk2.tambah_stok(-3)
print()

produk1.stok = 12
produk1.tampilkan_info()
produk1.stok = -5
produk1.stok = "lima"
print()

pelanggan1 = pelanggan("PL001", "Febri", "082251567811")
pelanggan2 = pelanggan("PL002", "Yanti", "08224153753")

pelanggan1.info_pelanggan()
pelanggan2.info_pelanggan()
pelanggan1.no_hp = "081365478"
pelanggan2.no_hp = 124442790081
print()
Trans1 = Transaksi("TR01", produk1, 2, 1000000)
Trans2 = Transaksi("TR02", produk2, 1, 150000)

Trans1.bukti_transaksi()
Trans2.bukti_transaksi()

print("pajak awal:", Transaksi.pajak)
Transaksi.ubah_pajak(0.15)
print("pajak baru:", Transaksi.pajak)

hitung_total = Transaksi.hitung_total_harga(produk1.harga, 3)
print(f"Total harga untuk 3 {produk1.nama}: {hitung_total}")