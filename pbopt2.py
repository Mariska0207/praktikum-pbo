class AlatCamping:
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            print("Harga tidak boleh negatif.")
        else:
            self.__harga = harga_baru

    def tampilkan_info(self):
        print(f"Nama Alat Camping: {self.nama}")
        print(f"Harga: {self.__harga}")

    @staticmethod
    def cek_nama(nama):
        if nama == "":
            print("Nama alat tidak boleh kosong.")
        else:
            print(f"Nama alat camping adalah: {nama}")

class TokoAlatCamping:
    def __init__(self, nama):
        self.nama = nama
        self.__daftar_alat = []

    def tambah_alat(self, alat):
        self.__daftar_alat.append(alat)
        print(f"Alat camping {alat.nama} telah ditambahkan ke daftar.")

    @property
    def daftar_alat(self):
        return self.__daftar_alat

    @daftar_alat.setter
    def __daftar_alat(self, alat_baru):
        self.__daftar_alat = alat_baru

class Transaksi:
    def __init__(self, id_transaksi, produk, jumlah):
        self.__id_transaksi = id_transaksi
        self.produk = produk
        self.__jumlah = jumlah

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru < 0:
            print("Jumlah tidak boleh negatif.")
        else:
            self.__jumlah = jumlah_baru

    def hitung_total(self):
        return self.produk.harga() * self.__jumlah

    @classmethod
    def buat_transaksi(cls, id_transaksi, produk, jumlah):
        return cls(id_transaksi, produk, jumlah)

alat1 = AlatCamping("Tenda", 500000)
alat2 = AlatCamping("Sleeping Bag", 300000)

alat1.tampilkan_info()
print()
alat2.tampilkan_info()

print(AlatCamping.cek_nama("Tenda"))
print(AlatCamping.cek_nama(""))

alat1.harga = 600000
alat1.tampilkan_info()

alat1.harga = -200000 
alat1.tampilkan_info()

transaksi1 = Transaksi.buat_transaksi("TRX001", alat1, 2)
print(f"ID Transaksi: {transaksi1._Transaksi__id_transaksi}") ,ncn