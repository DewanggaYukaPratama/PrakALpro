#DewanggaYukaPratama_71200581
#Universitas Kristen Duta Wacana

'''Di sebuah daerah terdapat sebuah gamenet sedang mengadakan acara grand opening.Sang pemilik yang bernama Dewa meminta
temannya yang bernama Aldo dan Omega untuk datang ke warnetnya yang sedang dibukanya.Dengan begitu dia membuatkan 
teman-temanya akun terlebih dahulu.
Sehingga saat teman-temannya datang mereka tinggal langsung masuk ke dalam akun billing mereka.
Nantinya teman-temannya pun hanya tinggal mengisi billing untuk mulai bermain sesuai dengan paket waktu yang tertera.
Daftar paket:
1.paket1 = 1 jam
2.paket2 = 3 jam
3.paket3 = 5 jam

Input:
1.Nama akun : Dewa,Aldo,dan Omega
2.Daftar dari paket yang akan dipilih


Proses:
1.Memasukan nama akun untuk melakukan login
2.Memasukan/memilih paket dari daftar paket yang tersedia


Output:
1.Dapat masuk ke dalam akun tersebut
Anda telah login ke akun Dewa/Aldo/Omega
2.Mendapat billing atau waktu yang sudah dipilih/dibeli
paket1 = billing anda telah bertambah 1 jam
paket2 = billing anda telah bertambah 3 jam
paket3 = billing anda telah bertambah 5 jam

'''

print('~'*6,'Selamat Datang di Gamenet DX',6*'~')

login_user=str(input('Masukkan Username Anda :'))
if login_user == 'Dewa' or login_user == 'Aldo' or login_user == 'Omega':
    print('Anda telah login ke Akun ' + login_user)

    billing=str(input('Tambah Billing Anda '))
    if billing == 'paket1':
        print('Billing anda telah bertambah 1 jam')
    elif billing == 'paket2':
        print('Billing anda telah bertambah 3 jam')
    elif billing == 'paket3':
        print('Billing anda telah bertambah 5 jam')
    else:
        print('Paket tersebut tidak tersedia')

else:
    print('Silahkan membuat akun terlebih dahulu')




