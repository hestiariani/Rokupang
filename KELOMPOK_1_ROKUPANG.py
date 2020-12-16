print("============================================")
print("KELOMPOK 1 ROKUPANG")
print("PYANDI PRADIPTA SETIAWAN 19200126")
print("ADE RIZKY ANWAR 19200247")
print("SIDIK DWI NUGRAHA 19200061")
print("DHEA AYU PERTIWI 19200602")
print("HESTI ARIANINGTYAS 19200085")
print("============================================")


print("              ROKUPANG           ")
print("=================================")
print("Kode       Varian Rasa      harga")
print("=================================")
print("1           Cokelat          10000")
print("2           Strawberry       10000")
print("3           Keju             10000")
print("4           Bluberry         10000")
print("5           Kacang           10000")

print("=============================================")
nama_mhs = str(input("CUSTUMER = "))
print("=============================================")

banyak_jenis = int(input("Banyak Jenis : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []
i = 0

while i<banyak_jenis:
    print("Jenis ke = ", i+1)
    kode_potong.append(input("kode Varian Rasa [1/2/3/4/5] : "))
    banyak_potong.append(int(input("Banyak Varian Rasa : ")))

    if kode_potong[i] == "1":
        jenis_potong.append("Cokelat")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode_potong[i] == "2":
        jenis_potong.append("Strawberry")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode_potong[i] == "3":
        jenis_potong.append("keju")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode_potong[i] == "4":
        jenis_potong.append("Bluberry")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode_potong[i] == "5":
        jenis_potong.append("kacang")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    else:
        jenis_potong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i = i + 1

print("                      ROKUPANG                ")
print("=========================================================")
print("No       Jenis           Harga       Banyak       Jumlah")
print("         Potong          Satuan      Potong       Harga")
print("=========================================================")

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i       %s        %s          %i          %i" % (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1

pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("                         Jumlah Bayar        Rp. ", jumlah_bayar)
print("                         Pajak 10%           Rp. ", pajak)
print("                         Total Bayar         Rp. ", total_bayar)

uang_tunai = int(input("UANG TUNAI : "))
kembalian = uang_tunai - total_bayar
print("KEMBALIAN = ", kembalian)