#71200581-Dewangga Yuka Pratama
#Universitas Kristen Duta Wacana

'''Reki adalah anak yang sedang merantau .Orang tuannya selalu memberikan uang kiriman 
setiap bulan untuk mencukupi kebutuhannya.Karena dia tidak bersama keluarganya Reki merasa 
kesusahan dalam memanage uang kiriman orang tuanya dalam mencukupi kebutuhannya.
Buatlah program untuk membantu Reki dalam mengecek saldo miliknya,sisa saldonya setelah 
melakukan pengeluaran dan meminta menambah saldo miliknya.


Input:
1.Uang awal Reki = 50000
2.Cek saldo
3.Sisa saldo
4.Menambah saldo
5.menutup atau menyudahi program tersebut

Proses:
1.Memasukan username Reki
2.Masuk ke menu cek saldo
3.Masuk menu sisa saldo
4.Masuk menu menambah saldo
5.masuk menu exit


Output:
1.Selamatan datang kepada user
2.Saldo Reki sekarang
3.Hasil sisa saldo Reki setelah melakukan pengeluaran
4.Hasil dari menambah saldo baru ke saldo awal


'''
print('Program Pengecek Saldo')
list = ['Cek Saldo','Sisa Saldo','Tambah Saldo','Exit']

Reki = 50000

user = str(input('Masukkan Username : '))
if user == 'Reki':
      print('Selamat Datang ', user)
      while True:
            for i in range (4):
                  print('%d.'%(i+1),list[i])
            
            inp=int(input('Masukkan Pilihan Anda : '))

            if inp == 1:
                  saldo = Reki
                  print('Saldo anda sebanyak ', saldo)
            elif inp == 2:
                  pengeluaran = int(input('Masukkan Pengeluaran Anda : '))
                  Sisa = saldo - pengeluaran
                  print('Sisa Saldo anda sebesar ' , Sisa )
            elif inp == 3:
                  tambah = int(input('Masukkan jumlah yang ingin anda tambahkan : '))
                  saldobaru = tambah + saldo
                  print('Saldo anda sekarang sebesar ', saldobaru)
            elif inp == 4:
                  print('Terima Kasih ')
                  break
            else:
                  print('Invalid')
                  break
else:
      print('Username anda belum terdaftar pada Program ')          
      

      
      
      