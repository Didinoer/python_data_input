# data input calon pegawai 
#nama
nama_pegawai = input("masukan nama anda  : ")
if nama_pegawai == nama_pegawai : print("nama telah disimpan") 
## nik 
nik_pegawai = input("masukan NIK anda : ")
if nik_pegawai == nik_pegawai : print(" nik anda telah disimpan")
## tempat tanggal lahir 
tempat_tanggal_lahir = input("masukan tempat dan tanggal lahir anda :")
if tempat_tanggal_lahir == tempat_tanggal_lahir :
    print(" tempat dan tanggal lahirmu telah tersimpan ")

#alamat 
alamat = input("masukan Alamat tempat tinggal  anda  : ")
if alamat == alamat : print("Alamat telah disimpan") 

#jenis kelamin
jenis_kelamin = input(""" masukan jenis gender : laki-laki (L)
                                                 perempuan (P)""")
if jenis_kelamin == "L" : print("laki-laki (ok)")
if jenis_kelamin == "P" : print("perempuan  (ok)")
   
print(""" posisi yang tersedia untuk ditempati 
         - Administrasi (S1)
         - IT staff (S1)
         - Manager operasional(S1) 
         - Operator produksi(SMA)
         - Cleaning service(SMA)
         - Maintenance gedung(SMA) """)


#pendidikan 
pendidikan = input("masukan jenjang pendidikan terakhir anda (SMA / S1) : ")  
if pendidikan == "SMA" : posisi = input(""" masukan posisi yang ingin dilamar : 
     - [OP] Operator produksi(SMA)
     - [CS] Cleaning service(SMA)
     - [MNT] Maintenance gedung(SMA)    :""") 
elif pendidikan == "S1" : posisi = input(""" masukan posisi yang ingin dilamar  :
      - [ADM] Administrasi (S1)
      - [IT]  IT staff (S1)
      - [MGR] Manager operasional(S1) """) 
if posisi == "OP" : print("anda melamar sebagai Operator produksi")
elif posisi == "CS": print("anda melamar sebagai Cleaning service")
elif posisi == "MNT"  : print("anda melamar sebagai Maintenance gedung")
elif posisi == "ADM" : print("anda melamar sebagai Administrasi ")
elif posisi == "IT" : print("anda melamar sebgaai IT staff")
elif posisi == "MGR" : print("anda melamar sebgai Manager operasional")
else : print(" posisi tidak tersedia")
#notel
notel = input("masukan Nomor telephone  anda  : ")
if alamat == alamat : print("Nomor telephone telah disimpan") 

#email  
email = input("masukan email anda  : ")
if alamat == alamat : print("email telah disimpan") 


print("""


















""")

#output
print("                                      DATA CALON PEGAWAI                                                              ")

print("nama :" , nama_pegawai)
print("Nik pegawai :", nik_pegawai)
print("tempat tanggal lahir : "  , tempat_tanggal_lahir)
print(" alamat :"  , alamat)
print(" jenis kelamin" , jenis_kelamin)
print("pendidikan terakhir :", pendidikan)
print("posisi yang dilamar :", posisi)
print("nomor telephone :" ,notel)
print("email calon pegawai", email)




