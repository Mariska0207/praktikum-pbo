from abc import ABC, abstractmethod

class AlatCamping(ABC):
    nama_toko = "Camping Yuk"
    Total_alat = 0

    def __init__(self, id_alat,nama, harga, stok):
        self.__id_alat = id_alat
        self.nama = nama
        self.harga = harga
        self._stok = stok

        AlatCamping.Total_alat += 1

    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, stok_baru):
        if type(stok_baru) == int:
            if stok_baru < 0:
                print("Stok tidak boleh negatif")
            else:
                self._stok = stok_baru
        else:
            print("stok harus angka")

    @abstractmethod
    def tampilkan_info(self):
        print(f"ID Alat Camping: {self.__id_alat}")
        print(f"Nama Alat Camping: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Stok: {self.stok}")

    @abstractmethod
    def hitung_diskon(self, jumlah):
        pass

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self._stok += jumlah
            print(f"Stok {self.nama} berhasil ditambahkan. Stok sekarang: {self._stok}")
        else:
            print("Jumlah yang ditambahkan harus lebih dari 0")

class tenda(AlatCamping):
    def __init__(self, id_alat, nama, harga, stok, kapasitas):
        super().__init__(id_alat, nama, harga, stok)
        self.kapasitas = kapasitas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas: {self.kapasitas} orang")
        print()

    def hitung_diskon(self, jumlah):
        return self.harga * jumlah * 0.10 if jumlah >= 2 else 0
    
class jaket(AlatCamping):
    def __init__(self, id_alat, nama, harga, stok, ukuran):
        super().__init__(id_alat, nama, harga, stok)
        self.ukuran = ukuran

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Ukuran: {self.ukuran}")
        print()

    def hitung_diskon(self, jumlah):
        return self.harga * jumlah * 0.05 if jumlah >= 3 else 0

class Kategori_Alat:
    def __init__(self, nama_kategori):
        self.nama_kategori = nama_kategori
        self.daftar_alat = []

    def tambah_alat(self, alat):
        if isinstance(alat, AlatCamping):
            self.daftar_alat.append(alat)
        else:
            print("Hanya objek AlatCamping yang dapat ditambahkan")

    def tampilkan_alat(self):
        print(f"Kategori: {self.nama_kategori}")
        for alat in self.daftar_alat:
            alat.tampilkan_info()

    def __len__(self):
        return len(self.daftar_alat)

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

    def beli_alat(self, alat, jumlah):
        if jumlah <= alat.stok:
            alat.stok -= jumlah
            print(f"{self.nama} berhasil membeli {jumlah} {alat.nama}. Stok sekarang: {alat.stok}")
        else:
            print(f"Stok {alat.nama} tidak cukup. Stok sekarang: {alat.stok}")

    def info_pelanggan(self):
        print(f"ID Pelanggan: {self.id_pelanggan}")
        print(f"Nama Pelanggan: {self.nama}")
        print(f"No. HP: {self.__no_hp}")
        print()

class DetailTransaksi:
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

class Transaksi:
    pajak = 0.1 

    def __init__(self, id_transaksi, produk, jumlah, total_harga):
        self.id_transaksi = id_transaksi
        self.produk = produk
        self.jumlah = jumlah

        self.detail_transaksi = DetailTransaksi(id_transaksi, produk, jumlah, total_harga)
        self.total_harga = self.hitung_total_harga(produk.harga, jumlah)

    def bukti_transaksi(self):
        self.detail_transaksi.bukti_transaksi()

    @classmethod
    def ubah_pajak(cls, pajak_baru):
        cls.pajak = pajak_baru

    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah

class PembayaranTunai:
    def __init__(self, uang_diberikan):
        self.uang_diberikan = uang_diberikan

    def proses(self, total):
        if self.uang_diberikan >= total:
            kembalian = self.uang_diberikan - total
            print(f"Pembayaran tunai berhasil. Kembalian: {kembalian}")
        else:
            print("Uang tidak cukup")

class PembayaranTransfer:
    def __init__(self, nama_bank, no_rekening):
        self.nama_bank = nama_bank
        self.no_rekening =  None

        if type(no_rekening) == str:
            if 10 <= len(no_rekening) <= 12:
                self.no_rekening = no_rekening
            else:
                print("Nomor rekening harus 10 sampai 12 digit")
        else:
            print("Nomor rekening harus berupa string")

    def proses(self, total):
        if self.no_rekening is None:
            print("Pembayaran Gagal: nomor rekening tidak valid")
        else:
            print(f"Silakan transfer {total} ke {self.nama_bank} {self.no_rekening}")

def proses_pembayaran(metode, total):
    metode.proses(total)

produk1 = tenda("AL001", "Tenda 2 orang", 500000, 10, 10)
produk2 = jaket("AL002", "Jaket Gunung", 150000, 15, "M")

try:
    alat = AlatCamping("AL001", "Tenda 2 orang", 500000, 10)
except TypeError as e:
    print("Abstract class tidak bisa diinstansiasi:", e)

print()
produk1.tampilkan_info()
produk2.tampilkan_info()

produk1.tambah_stok(5)
produk2.tambah_stok(-3)
print()

kategori1 = Kategori_Alat("Tenda")
kategori2 = Kategori_Alat("Jaket")

kategori1.tambah_alat(produk1)
kategori2.tambah_alat(produk2)

kategori1.tampilkan_alat()
kategori2.tampilkan_alat()

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

pelanggan1.beli_alat(produk1, 3)
pelanggan2.beli_alat(produk2, 5)
print()

Trans1 = Transaksi("TR01", produk1, 2, 1000000)
Trans2 = Transaksi("TR02", produk2, 1, 150000)

Trans1.bukti_transaksi()
Trans2.bukti_transaksi()

print("pajak awal:", Transaksi.pajak)
Transaksi.ubah_pajak(0.15)
print("pajak baru:", Transaksi.pajak)

hitung_total = Transaksi.hitung_total_harga(produk1.harga, 3)
print(f"Total harga untuk 3 {produk1.nama}: {hitung_total}\n")

daftar_produk = {produk1, produk2}
for alat in daftar_produk:
    alat.tampilkan_info()

proses_pembayaran(PembayaranTunai(1200000), Trans1.total_harga)
proses_pembayaran(PembayaranTransfer("BCA", "1234567890"), Trans2.total_harga)
print()

print(f"Jumlah alat di kategori {kategori1.nama_kategori}: {len(kategori1)}\n")

print(f"Diskon 2 tenda : Rp{produk1.hitung_diskon(2):,.0f}")
print(f"Diskon 4 jaket : Rp{produk2.hitung_diskon(4):,.0f}") 