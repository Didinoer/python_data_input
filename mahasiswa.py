

data1 = []

print('===================menu==================')
print('1 . menambah data mahasiswa')
print('2 . menampilkan data mahasiswa')
print('3 . keluar')
i = int(input("masukan pilihan 1/2/3 ?   :  "))
while i == 1 :
    nama = input("input nama mahasiswa  : ")
    nim = input("input nim mahasiswa  :   ")
    data1.append([nama,nim])
    j = input("""ingin melanjutkan program ? (y) 
                tampilkan data ? (p)  
                masukan perintah :   """)
    if j == "y" : i = 1
    elif j == "p" : i = 2
while  i == 2 :
    print(data1)
    j = input('a . masukan data lagi  b. keluar')
    if j == "a"  :
        nama = input("input nama mahasiswa  : ")
        nim = input("input nim mahasiswa  :   ")
        data1.append([nama,nim])
    elif j == "b" : break
    











    
 
  