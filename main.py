#Import
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Konstanta
m = 9.1094e-31     # Massa Elektron
hbar = 1.0546e-34  # Konstanta Planck Tereduksi
e = 1.6022e-19     # Muatan Elektron
L = 5.2918e-11     # Panjang dari Sumur Potensial, Diasumsikan Sebagai Radius Bohr Untuk Menggunakan Nilai yang Sesuai Asli
N = 1000           # Banyaknya Pengulangan yang Diinginkan
h = L/N            # Nilai h atau Step Size Ditentukan Berdasarkan Nilai L Dibagi Banyak Pengulangan yang Diinginkan

#data judul
judul1 = "Program Solusi Persamaan Schroedinger Tak Bergantung Waktu"
judul2 = 'Sumur Potensial Tak Berhingga Satu Dimensi'
print()
print('='*112)
print(judul1.center(111))
print(judul2.center(111))
print('='*112)

#data menu
pilihan_menu = {
    1: 'Menunjukan Grafik Persamaan Gelombang dan Rapat Probabilitas',
    2: 'Menunjukan Tingkat Energi',
    3: 'Keluar'
    }

#Pendefinisian Fungsi
def V(x):
    return 0.0

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    dpsi = phi
    ddpsi = (2*m/hbar**2)*(V(x)-E)*psi
    return np.array([float(dpsi),float(ddpsi)])

#Pendefinisian Runge-Kutta Orde 4 dalam Kasus Persamaan Schroedinger Tak Bergantung Waktu : Sumur Potensial Tak Hingga Satu Dimensi
def rungeKutta4Orde2(Epred):
    #Nilai psi atau panjang gelombang pada kondisi awal adalah 0
    psi = 0.0
    #Tebakan nilai dpsi
    phi = 1
    r = np.array([float(psi),float(phi)])
    psiPlot=[]
    for x in np.arange(0,L,h):
        psiPlot.append(r[0])
        k1 = h*f(r,x,Epred)
        k2 = h*f(r+0.5*k1,x+0.5*h,Epred)
        k3 = h*f(r+0.5*k2,x+0.5*h,Epred)
        k4 = h*f(r+k3,x+h,Epred)
        r += (k1+2*k2+2*k3+k4)/6
    return r[0],psiPlot

#Pendefinisian Metode Secant untuk Menentukan Energi
def secantEnergi(Epred):
    psiPlotBaru = []
    Ehasil = e
    psiPred,psiPlot = rungeKutta4Orde2((Epred))
    gal = e / 1000
    while abs(Epred - Ehasil) > gal:
        psiHasil = psiPred
        psiPred, psiPlotBaru = rungeKutta4Orde2(Ehasil)
        Epred, Ehasil = Ehasil, Ehasil - psiPred * (Ehasil - Epred) / (psiPred - psiHasil)
    return Ehasil,psiPlotBaru

#Menghitung Energi secara numerik untuk memudahkan pengolahan menu
Epred = 0
EhasilMain,psiPlotBaruMain = secantEnergi(Epred)

#Setting grafik
plt.style.use('seaborn')

#Definisi Fungsi Penampilan Menu
def printMenu():
    print()
    for i in pilihan_menu.keys():
        print (i, '-', pilihan_menu[i] )

#Fungsi Menu Pertama
def pilihan1(Ehasilmain):
    while(True):
        n = int(input('Masukan Bilangan Kuantum (Masukan Nilai 0 Untuk Melihat Kombinasi Grafik n = 1 Sampai n Tertentu: '))
        fig = plt.figure()
        gstinggi = gridspec.GridSpec(nrows=2, ncols=2, width_ratios=[3, 1], height_ratios=[3, 1])
        gs = gridspec.GridSpec(nrows=2, ncols=2, width_ratios=[3, 1])
        ax0 = fig.add_subplot(gs[0, 0])
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gstinggi[:, 1])
        if n == 0:
            N = int(input('Masukan n akhir: '))
            for n in range(0,N+1):
                Eplot, psiPlotGrafik = secantEnergi(Ehasilmain * (n ** 2))
                ax2.set_ylim(Ehasilmain-1e-16,Eplot+1e-16)
                ax2.axhline(y=Eplot, color='r', linestyle='-',label ='n = %d'%n )
                ax2.set_title('Tingkatan Energi')
                ax0.set_xlim(0,1000)
                ax0.set_title('Persamaan Gelombang (Ψ)')
                ax0.plot(psiPlotGrafik,label='n = %d'%n)
                psiPlotProb = (np.square(np.abs(psiPlotGrafik)))
                ax0.legend()
                ax1.set_xlim(0, 1000)
                ax1.set_title('Rapat Probabilitas (|Ψ|²)')
                ax1.plot(psiPlotProb,label='n = %d'%n)
                ax1.legend()
            plt.show()
            break
        else:
            Eplot, psiPlotGrafik = secantEnergi(Ehasilmain * (n ** 2))
            plt.subplot(211)
            plt.title('Persamaan Gelombang (Ψ)')
            plt.plot(psiPlotGrafik,'b')
            plt.xlim(0,1000)
            psiPlotProb = (np.square(np.abs(psiPlotGrafik)))
            plt.subplot(212)
            plt.title('Rapat Probabilitas (|Ψ|²)')
            plt.plot(psiPlotProb,'g')
            plt.xlim(0,1000)
            plt.show()
            status = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
            if (status == 'y'):
                return False
            else:
                continue

#Fungsi Menu Kedua
def pilihan2():
    while(True):
        n = int(input('Masukan Bilangan Kuantum yang ingin dilihat energinya: '))
        Enumerik = EhasilMain*(n**2)
        print("\nE =", Enumerik, "J")
        print("E =",  Enumerik / e, "eV")
        Eeksak = (((hbar ** 2) * (np.pi ** 2)) / (2 * m * L ** 2))*(n**2)
        print("\nE analitik=",Eeksak, "J")
        print("E analitik=", Eeksak/ e, "eV")
        print("\nGalat =", ((abs(Enumerik-Eeksak))/Eeksak), "%")
        status = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
        if (status == 'y'):
            return False
        else:
            continue

#Program Utama/Runner Program
if __name__=='__main__':
    while(True):
        printMenu()
        pilihan = ''
        try:
            pilihan = int(input('\nSelamat datang dalam sistem, silahkan pilih opsi menu: '))
        except:
            print('Tolong masukan data berupa angka, terima kasih.')
        if pilihan == 1:
           pilihan1(EhasilMain)
        elif pilihan == 2:
            pilihan2()
        elif pilihan == 3:
            print('Sampai jumpa kembali')
            exit()
        else:
            print('Tolong masukan angka yang tertera untuk mengakses menu yang terlampir, terima kasih.')
