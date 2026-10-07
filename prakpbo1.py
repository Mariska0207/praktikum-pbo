# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def show_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Price: {self.price}")

#     def change_price(self, new_price):
#         self.price = new_price
#         self.show_info()

class Jadwal:
    musim_liga = "MPL Indonesia Season 14"
    def __init__(self, tim_a, tim_b, tanggal):
        self.tim_a = tim_a
        self.tim_b = tim_b
        self.tanggal = tanggal

    @classmethod
    def dari_dict(cls, data):
        return cls(data["tim_a"], data["tim_b"], data["tanggal"])
    
    @classmethod
    def ganti_musim(cls, musim_baru):
        cls.musim_liga = musim_baru

    def info(self):
        print(f"{self.tim_a} vs {self.tim_b} - {self.tanggal}({Jadwal.musim_liga})\n")

data_laga = {"tim_a": "RRQ", "tim_b": "Evos Legends", "tanggal": "12 September 2026"}
data_laga2 = {"tim_a": "ONIC", "tim_b": "Alter Ego", "tanggal": "13 September 2026"}
laga1 = Jadwal.dari_dict(data_laga)
laga2 = Jadwal.dari_dict(data_laga2)
laga1.info() 
laga2.info() 
Jadwal.ganti_musim("MPL Indonesia Season 15")
laga1.info() 
laga2.info()