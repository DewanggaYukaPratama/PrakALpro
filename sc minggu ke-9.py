#71200581 Dewangga Yuka Pratama
#Universitas Kristen Duta Wacana

'''Di sebuah sekolah seorang guru ingin memasukkan nilai beberapa muridnya dengan cara
melistnya.Dia mengajar di 2 kelas A dan B nantinya 3 siswa dari kelas A 
dan 4 siswa dari kelas B dari akan diambil acak untuk melihat nilainya.
Kelas A ada Fadli,Dodi,Galih sedangkan kelas B ada Riki,Joko,Paul,Tono
Kita diminta untuk membuatkan program untuk membuat daftar siswa dan nilainya dari tiap kelas

Kelas A :
Fadli = 80
Dodi = 79
Galih = ?

Kelas B :
Riki = 88
Joko = ?
Paul = 82
Tono = 90
===================
Input:
1.Memasukkan nilai kosong
2.Memilih kelas a atau kelas b

Proses:
1.Masuk kedalam tiap kelas yang dipilih

Output:
1.masuk ke kelas a dan juga ke kelas b
2.daftar nama dan nilai dari tiap kelasnya

=================
'''

glh = int(input('Nilai Kosong A : '))
jk = int(input('Nilai Kosong B : '))

namaA = ['Fadli','Dodi','Galih']
nilaiA = ['80','79',glh]
namaB = ['Riki','Joko','Paul','Tono']
nilaiB = ['88',jk,'82','90']

listmenu = ['Daftar Kelas A','Daftar Kelas B','Tutup']

while True:
    print('='*15+'Daftar Siswa'+15*'=')
    for i in range(3):
        print('%d.'%(i+1),listmenu[i])
    
    menu = int(input("Pilihan Kelas : "))

    x = len(namaA)
    y = len(namaB)

    if menu == 1:
        print('====Data Siswa Kelas A====')
        for klsA in range(x):
            print('Nama :'+namaA[klsA]+'|'+' '+'Nilai : '+str(nilaiA[klsA]))
    elif menu == 2:
        print('====Data Siswa Kelas B====')
        for klsB in range(y):
            print('Nama : '+namaB[klsB]+'|'+' '+'Nilai : '+str(nilaiB[klsB]))
    elif menu == 3:
        print('Terima Kasih')
        break


