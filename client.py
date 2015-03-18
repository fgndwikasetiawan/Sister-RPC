import xmlrpclib as xrl
import os
import threading
import time

def kirim_gambar(daftarFile, server, jumlah, nama):
    daftarGambar = []
    n = 0
    while (n + jumlah < len(daftarFile)):
        for i in range(n, n+jumlah):
            f = open(daftarFile[i], 'rb')
            daftarGambar.append(xrl.Binary(f.read()))
            f.close()
        i = n
        daftarGrayscale = server.rgb_to_grayscale(daftarGambar)
        for grayscale in daftarGrayscale:
            f = open(daftarFile[i][:-4] + '_grayscale.png', 'wb')
            f.write(grayscale.data)
            f.close()
            i += 1
        daftarGambar[:] = []
        n += jumlah
        print nama + ": " + str(n) + '/' + str(len(daftarFile))

    for i in range(n, len(daftarFile)):
        f = open(daftarFile[i], 'rb')
        daftarGambar.append(xrl.Binary(f.read()))
        f.close()
    i = n
    daftarGrayscale = server.rgb_to_grayscale(daftarGambar)
    for grayscale in daftarGrayscale:
        f = open(daftarFile[i][:-4] + '_grayscale.png', 'wb')
        f.write(grayscale.data)
        f.close()
        i += 1
    print nama + ' selesai'


dir = raw_input("Direktori gambar: ")
alamat1 = raw_input("Alamat server #1: ")
alamat2 = raw_input("Alamat server #2: ")
os.chdir(dir)
server1 = xrl.ServerProxy(alamat1)
server2 = xrl.ServerProxy(alamat2)
jumlahBatch = int(raw_input("Jumlah gambar per request: "))
files = os.listdir(os.getcwd())
jumlahFile = len(files)

thread1 = threading.Thread(target=kirim_gambar, args=(files[0:jumlahFile/2], server1, jumlahBatch, 'Thread 1'))
thread2 = threading.Thread(target=kirim_gambar, args=(files[jumlahFile/2:jumlahFile], server2, jumlahBatch, 'Thread 2'))
start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print 'SELESAI yeee, waktu: ' + str(time.time() - start)


