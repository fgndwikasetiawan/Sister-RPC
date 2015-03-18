import xmlrpclib as xrl
import os
import threading


def kirim_gambar(daftarFile, server, jumlah):
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
        print str(n) + '/' + str(len(daftarFile))

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
    print('selesai')

dir = raw_input("Direktori gambar: ")
alamatServer = raw_input("Alamat server: ")
os.chdir(dir)
server = xrl.ServerProxy(alamatServer)
print "Berhasil konek"
jumlahBatch = int(raw_input("Jumlah gambar per request: "))
files = os.listdir(os.getcwd())
jumlahFile = len(files)

thread1 = threading.Thread(target=kirim_gambar, args=(files[:], server, jumlahBatch))
thread1.start()


