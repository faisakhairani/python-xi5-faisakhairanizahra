class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

faisa = Siswa(16354, "Faisa Khairani Zahra", "XI MIPA 5")

print(faisa.getnis())
faisa.setnis(10000)
print(faisa.getnis())