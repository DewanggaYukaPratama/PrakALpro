#71200581 Dewangga Yuka Pratama
#Universitas Kristen Duta Wacana

'''Suatu hari Mei sedang mengerjakan atau menyelesaikan sebuah teka-teki,karena 
Mei orangnya suka dengan teka-teki maka Mei mampu hampir semua teka-teki.Tetapi pada akhir 
teka-teki Mei kesusahan saat mencari teka-teki berupa beberapa angka dan untuk menyelesaikannya
Mei butuh mengurutkan angka terkecil dan terbesarnya.Bantulah Mei dalam menentukan angka 
terkecil dan terbesar pada urutan beberapa angka yang ditemukan..

Input:
1.beberapa uratan angka

Proses:
1.mencari angka terkecil dan terbesar

Output:
1.hasil dari angka terkecil dan angka terbesar

'''
def nilai_max(list):
    nilai_terbesar=list[0]

    if len(list)>1:
        nilai_terbesar2 = nilai_max(list[1:])

        if nilai_terbesar2 > nilai_terbesar:
            nilai_terbesar = nilai_terbesar2
    
    return nilai_terbesar

def nilai_min(list):
    nilai_terkecil=list[0]

    if len(list)>1:
        nilai_terkecil2 = nilai_min(list[1:])

        if nilai_terkecil2 < nilai_terkecil:
            nilai_terkecil = nilai_terkecil2

    return nilai_terkecil

x = [15,3,26,88,34]
print(x)
print('Nilai Terbesar : ',nilai_max(x))
print('Nilai Terkecil : ',nilai_min(x))

