class Classes:
    def __init__(self,nama,nim,jurusan,fakultas,b):
        self.nama = nama
        self.jurusan = jurusan
        self.nim = nim
        self.fakultas = fakultas
        self.b = b
        
    def display(self,nim,jurusan,fakultas):
        print("Nama     : ", nama)
        print("Nim      : ", nim) 
        print("Jurusan  : ", jurusan)
        print("Fakultas : ", fakultas) 
          
    def jaraktempuh(self,b):
        return self * b
        
    def harga_satuan(self,b,diskon):
        return self * b * diskon
    
    def biaya_percakapan(self):
        return self * 1000
    
    def biaya_sms(self):
        return self * 300
    
    def gaji_bersih(self,b):
        return (self + (self * 0.2) + (self * (0.1 * b)))
    
#main 
print("1. Nomor 1\n2. Nomor 2\n3. Nomor 3\n4. Nomor 4\n5. Nomor 5\n6. Nomor 6\n7. Nomor 7")
pilihan = int(input("Masukan Pilihan    :"))

if pilihan == 1:
    print("Input Identitas")
    nama    = input("nama       :")
    nim     = input("nim        :")
    jurusan = input("Jurusan    :")
    fakultas= input("fakultas   :")

    print("\nOutput ")        
    Classes.display(nama,nim,jurusan,fakultas)

elif pilihan == 2:
    kecepatan = int(input("Kecepatan rata-rata  :"))
    waktu     = int(input("Waktu tempuh (jam)   :"))
    hasil = Classes.jaraktempuh(kecepatan,waktu)
    print("Jara tempuh      : ", hasil, " km")
    
elif pilihan == 3:
    diskon = 0.1
    harga_satuan = int(input("Harga Satuan :"))
    Jumlah = int(input("Jumlah Pembelian :"))
    hasil = Classes.harga_satuan(harga_satuan,Jumlah,diskon)
    print("Harga Total :Rp. ", int(hasil))

elif pilihan == 4:
    harga_satuan = int(input("Harga satuan :"))
    Jumlah = int(input("Jumlah  :"))
    Diskon = int(input("Diskon (%) :"))
    Diskon = Diskon / 100
    hasil = Classes.harga_satuan(harga_satuan,Jumlah,Diskon)
    print("Harga Total :Rp. ", hasil)
    
elif pilihan == 5:
    abnomen = 20000
    nama = input("Nama  : ")
    percakapan = int(input("Percakapan  :"))
    sms = int(input("SMS    : "))
    b_percakapan = Classes.biaya_percakapan(percakapan)
    b_sms = Classes.biaya_sms(sms)
    total = b_percakapan + b_sms
    print("\nTagihan\n          :")
    print("Abnomen          : ", abnomen,"(Optional biaya bulanan)")
    print("Biaya percakapan : ", b_percakapan)
    print("Biaya SMS        : ", b_sms)
    print("Total Tagihan    : ", total)

elif pilihan == 6:
    T_kesejahteraan = 20 / 100
    T_Keluarga = 10 / 100
    pajak = 10 / 100
    nama = input("Nama Karyawan : ")
    g_pokok = float(input("Gaji Pokok :"))
    j_anak = int(input("Jumlah anak :"))
    g_kotor = Classes.gaji_bersih(g_pokok,j_anak)
    g_bersih = g_kotor - (g_kotor * 0.1)
    
    print("Gajo Pokok        T. Kesejahteraan           T.Keluarga      Pajak")
    print(g_pokok,"                20%                     10%           10% " )
    
    print("Gaji Kotor   : ",g_kotor)
    print("Gaji Bersih  : ",g_bersih)    
    