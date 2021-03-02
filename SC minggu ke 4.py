#71200581_DewanggaYukaPratama
#Universitas Kristen Duta Wacana


'''Rian memiliki seorang adik yang masih SD.Adiknya mendapat sebuah PR
oleh guru matematikanya.Adiknya diminta untuk menghitung luas bangun datar.
Karena melihat adiknya yang merasa kesusahan dalam mengerjakan PR, Sehinga 
Rian mempunyai Ide untuk membuatkan adiknya sebuah program untuk menghitung 
luas bangun datar supaya dia dapat membantu dan mengajari adiknya.
Sehingga kita diminta untuk membuat program untuk menghitung luas bangun 
datar persegi, persegi panjang, segitiga, dan lingkaran 
menggunakan program modular.

Input:
persegi = sisi
persegi panjang = panjang lebar
segitiga = alas tinggi
lingkaran = jari-jari


Proses:
1.membuat fungsi modular persegi
2.fungsi modular persegi panjang
3.fungsi modular segitiga
4.fungsi modular lingkaran

Output:
1.hasil luas persegi
2.hasil luas persegi panjang
3.hasil luas segitiga
4.hasil luas lingkaran


'''
print('=== Program Penghitung Luas Bangun Datar ===')
list = ['Persegi','Persegi Panjang','Segitiga','Lingkaran']
for i in range(4):
    print('%d.'%(i+1), list [i])


def luaspersegi(s):
    hasil = s*s
    return hasil

def luasperspanjang(p,l):
    hasil = p*l
    return hasil

def luassegitiga(a,t):
    hasil = (a*t)/2
    return hasil

def luaslingkaran(r):
    phi = 22/7
    hasil = phi*(r*r)
    return hasil

inp = input('Masukkan Pilihan Anda : ')
if inp == '1':
    sisi = int(input('Masukkan sisi :'))
    print('Luas persegi tersebut adalah ', luaspersegi(sisi))
elif inp == '2':
    panjang = int(input('Masukkan panjang : '))
    lebar = int(input('Masukkan lebar : '))
    print('Luas persegi panjang tersebut adalah ', luasperspanjang(panjang,lebar))
elif inp == '3':
    alas = int(input('Masukkan alas : '))
    tinggi = int(input('Masukkan tinggi : '))
    print('Luas segitiga tersebut adalah ', luassegitiga(alas,tinggi))
elif inp == '4':
    jari = int(input('Masukkan jari-jari : '))
    print('Luas lingkaran tersebut adalah ', luaslingkaran(jari))
else :
    print('Rumus belum tersedia!!!')

    