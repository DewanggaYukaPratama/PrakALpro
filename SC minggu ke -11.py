#71200581 Dewangga Yuka Pratama
#Universitas Kristen Duta Wacana

''' Suatu hari Andi diminta ibunya untuk berbelanja kebutuhan sehari-hari.Dia diminta
untuk membeli beberapa jenis sembako seperti : Beras,Minyak Goreng,Telur,Gula,Mie instant,
Bumbu dapur,Garam, dan Snack.Andi diberi ibunya sejumlah uang , karena Andi kesusahan 
dalam perhitungan bantulah Andi dengan membuatkan program untuk memasukkan semua barang 
belanjaannya dan harganya,sehingga Andi mengetahui total harga belanja dan kembaliannya.

=====================
Input :
1.Uang Andi
2.Harga barang belanja

Proses:
1.Memasukkan uang andi dan harga barang belanja
2.penghitungan total belanja Andi dan Kembalian yang diterima Andi

Output:
1.Total Belanja Andi
2.Kembalian Andi
===================== '''

belanja = ('Beras','Minyak Goreng','Telur','Gula','Mie Instant','Bumbu Dapur','Garam','Snack')

uang = int(input('Uang Andi Sebanyak : '))
n = 0

for i in range(len(belanja)):
    print('Masukkan harga barang belanjaan dari ',belanja[i],end='')
    harga = int(input(' : Rp. '))
    n = n + harga

print('='*20)
print('Total Harga Barang Belanja Andi Sebesar ',n)
print('='*20)

if n > uang :
    print('Uang Andi tidak Cukup')
    print('Andi utang sebesar ',n - uang)
elif uang > n:
    print('Kembalian Andi sebesar',uang - n)

