
#71200581 Dewangga Yuka Pratama
#Universitas Kristen Duta Wacana

'''Joni adalah seorang pemilik tempat bermain atau rental Playstation/PS.Pada tempatnya
dia memiliki atau menyediakan PS3 dan PS4 untuk disewakan/rental.Namun karena sering 
kehilangan catatan sang peminjam dia susah saat ada yang mau pinjam atau mengembalikan.
Sebagai teman Joni kita ingin membantunya membuatkan catatan digital supaya Joni yang teledor
tidak kesusahan dalam mengelola data-data pinjaman PS-nya.Disini kita akan membuatkan program
yang nantinya akan dapat melist siapa saja peminjam PS3 dan PS4 nya.

==================
Input:
1.User/Pemilik
2.Pilihan menu 
3.peminjam ps3 & ps4

Proses:
1.Memasukkan user sang pemilik
2.Memasukkan menu
3.Menuliskan nama peminjam
4.Melihat seluruh peminjam

Output:
1.Greeting terhadap sang pemilik
2.masuk kedalam pilihan menu
3.Data peminjam akan tersimpan pada list 
================== 
'''
fileku = open('data-pinjaman.txt','w')

print('='*20)
print('Data Peminjam PS Joni')
print('='*20)
list=['Peminjam PS4','Peminjam PS3','Seluruh Data Peminjam','Exit']
data_user=str(input('Masukkan nama Pemilik : '))
data_ps4=[]
data_ps3=[]

if data_user == 'Joni':
    print('==== Selamat Datang' + data_user + '====')

    while True:
        for i in range(4):
            print('%d.'%(i+1),list[i])
        
        pilihmenu = int(input('Masukkan pilihan menu : '))

        if pilihmenu == 1:
            ps4 = input('Masukkan Peminjam PS4 : ')
            data_ps4.append(ps4)
            print('Data'+' '+ps4+' '+ 'berhasil dimasukkan')
        elif pilihmenu == 2:
            ps3 = input('Masukkan Peminjam PS3 : ')
            data_ps3.append(ps3)
            print('Data'+' '+ps3+' '+ 'berhasil dimasukkan')
        elif pilihmenu == 3:
            print('Data Seluruh Peminjam : ')
            x = len(data_ps4)
            w = len(data_ps3)
            for y in range(x):
                print('|'+'Peminjam PS4 : '+''+data_ps4[y]+'|')
            for z in range(w):
                print('|'+'Peminjam PS3 : '+''+data_ps3[z]+'|')
            print('')
        elif pilihmenu == 4:
            print('Goodbye....'+data_user)
            break
        else:
            print('Invalid')
            break
else:
    print('User tidak diketahui!!')

fileku.write('Peminjam PS4 '+' '+str(data_ps4)+'\n')
fileku.write('Peminjam PS3 '+' '+str(data_ps3))
fileku.close()






            

