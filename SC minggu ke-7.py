#71200581 Dewangga Yuka Pratama 
#Universitas Kristen Duta Wacana

''' Terdapat 3 sahabat bernama Andi,Budi,Dedi.Karena mereka bosan mereka memutuskan 
untuk melakukan permainan susan kata.Mereka membuat 3 kata acak tiap orangnya setelah itu
mereka mengacaknya dan membagikannya terhadap lainnya sama rata yaitu sebanyak 3 per orang.
Setelah mendapatkan acakan tersebut mereka menyusun kembali kata acak tersebut menggunakan 
1 kata dari tiap orangnya,sehingga tiap orang dapat menyusun kata sebanyak 3 kata
Kita diminta membantu mereka dengan program untuk menyusun kata
acak tersebut.
===============================
andi = 'Aku Bola Makan'
budi = 'Mau Kami Sedang'
dedi = 'Menonton Dia Belajar'
===============================

Input:
1.User/Anggota
2.Menentukan pengambilan kata tiap orang

Proses:
1.Memasukan nama anggota
2.Memasukan perpotongan kata/menentukan kata tiap orang

Output:
1.Berhasil masuk pada program
2.hasil gabungan kata

'''
andi = 'Aku Makan Bola'
budi = 'Sedang Kami Mau'
dedi = 'Dia Belajar Menonton'

print('='*20)
print('Program Permainan Penyusun Kata')
print('='*20)
anggota = str(input('Nama Anggota : '))
print('='*20)

if anggota == 'Andi' or anggota == 'Budi' or anggota == 'Dedi':
    print('Selamat Datang di Permainan ', anggota)

    dpnandi = int(input('Kamus Andi pertama : '))
    blkandi = int(input('Kamus Andi kedua : '))
    dpnbudi = int(input('Kamus Budi pertama : '))
    blkbudi = int(input('Kamus Budi kedua : '))
    dpndedi = int(input('Kamus Dedi pertama : '))
    blkdedi = int(input('Kamus Dedi kedua : '))
    
    if anggota == 'Andi':
        print(andi[dpnandi:blkandi]+' '+budi[dpnbudi:blkbudi]+' '+dedi[dpndedi:blkdedi]) 
    elif anggota == 'Budi':
        print(budi[dpnbudi:blkbudi]+' '+dedi[dpndedi:blkdedi]+' '+andi[dpnandi:blkandi])
    elif anggota == 'Dedi':
        print(dedi[dpndedi:blkdedi]+' '+budi[dpnbudi:blkbudi]+' '+andi[dpnandi:blkandi])
    
else:
    print('Bukan Anggota!!!')