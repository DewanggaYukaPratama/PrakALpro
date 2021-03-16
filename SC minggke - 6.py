#7120581-Dewangga Yuka Pratama
#Universitas Duta Wacana

'''Deka adalah seorang mahasiswa Informatika.Dia memiliki kakak seorang guru TK, Esoknya Deka
diminta untuk menemani/membantu kakaknya mengajar.Rencananya kakaknya akan memperkenalkan 
bentuk-bentuk bangun datar kepada anak-anak.Keesokannya saat mulai mengajar ternyata kakanya
lupa membawa materi presentasinya sehingga Deka diminta membuatkan program yang 
merepresentasikan bentuk-bentuk bangun datar yaitu Segitiga,Kotak,Jajargenjang,Belah Ketupat.


Input:
1.pilihan menu
2.menentukan baris tiap bangun (4 bangun)

Proses:
1.memasukkan pilihan menu
2.memasukan baris segitiga
3.memasukan baris kotak
4.memasukan baris jajargenjang
5.memasukan baris belahketupat

output:
1.bentuk segitiga setelah ditentukan barisnya
2.bentuk kotak setelah ditentukan barisnya
3.bentuk jajargenjang setelah ditentukan barisnya
4.bentuk belahketupat setelah ditentukan barisnya

'''
print('Menu Bangun Datar')
print('='*20)
list = ['Segitiga','Jajargenjang','Kotak','Belah Ketupat']

for i in range (4):
    print('%d.'%(i+1),list[i])

print('='*20)

pil = int(input('Masukkan Pilihan Menu : '))

if pil == 1:
    a = int(input('Baris : '))
    for i in range (a):
        print(('*'*(1+2*i)).center(1+2*a))
elif pil == 2:
    p = int(input('Baris : '))
    i = 0
    l = p
    while(1<=p):
        print(' '*(p-1)+ '*' * (i+(l*2))+ '*' * (p-1))
        p= p-1
        i= i+1
elif pil == 3:
    s = int(input('Baris : '))
    for i in range (s):
        if i == 0 or i == s-1:
            print('* '*s)
        else:
            print('* '+'  '*(s-2)+'* ')
elif pil == 4:
    d = int(input('Baris'))
    for i in range (d):
        for j in range(d-i-1):
            print(' ',end='')
        for k in range(2*i+1):
            print('*',end='')
        print()
    d-=1
    for i in range (d):
        for j in range (i+1):
            print(' ',end='')
        for j in range(2*(d-i)-1):
            print('*',end='')
        print()
else :
    print('Invalid')











