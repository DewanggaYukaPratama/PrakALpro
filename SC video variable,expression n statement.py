#Dewangga Yuka Pratama - 71200581
#Universitas Kristen Duta Wacana

'''Abi adalah salah satu siswa desain grafis.Gurunya meminta Abi untuk membuatkannya sebuah program penghitungan.
Dia diminta untuk membuat sebuah program untuk menghitung nilai rata-rata dari siswa desain grafis lainnya 
yang berjumlah 5 orang termasuk dirinya.Daftar nilai sebagai berikut: 
Abi = 81 ; Siswa1 = 78 ; Siswa2 = 83 ; Siswa3 = 86 ; Siswa4 = 77

Input: 
NilaiAbi = 81
NilaiS1  = 78
NilaiS2  = 83
NilaiS3  = 86
NilaiS4  = 77


Proses: 
Rumus = NilaiAbi + NilaiS1 + NilaiS2 + NilaiS3 + NilaiS4 dibagi 5

Output:
Hasil rata-rata dari kelima siswa desain grafis

'''

print ('='*10,'Program Penghitungan Nilai Rata-Rata Siswa Desain Grafis',10*'=')

NilaiAbi = int(input('Masukkan Nilai Abi:'))
NilaiS1  = int(input('Masukkan Nilai Siswa1:'))
NilaiS2  = int(input('Masukkan Nilai Siswa2:'))
NilaiS3  = int(input('Masukkan Nilai Siswa3:'))
NilaiS4  = int(input('Masukkan Nilai Siswa4:'))

Rata_rata = (NilaiAbi + NilaiS1 + NilaiS2 + NilaiS3 + NilaiS4) / 5

print("Hasil Rata-Rata Siswa Desain Grafis adalah %d "%Rata_rata)











'''Hitunglah sebuah nilai dari fungsi f(x) = 3(x+2)**2+4x/ x/4 , namun x adalah bilangan atau angka kelipatan 2 

Input :

x = 4

Proses:

Memasukan nilai X ke dalam fungsi f(x) = 3(x+2)**2+4x/ x/4

Output:

Hasil dari fungsi f(x) = 3(x+2)**2+4x/ x/4


'''


print ('Program Penghitungan Fungsi Nilai')

NilaiX = int(input("Masukkan bilangan kelipatan dua : "))

rumus = 3 * (NilaiX+2)**2 + 4 * NilaiX / (NilaiX/4)

print ('Hasil dari fungsi F(x) : %d'% rumus)
