import numpy as np
import matplotlib.pyplot as plt

file1 = np.loadtxt('cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#1(s)')
file2 = np.loadtxt('cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#2(p)')
file3 = np.loadtxt('cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#3(d)')
energy1, pdos1 = file1[:,0], file1[:,1]
energy2, pdos2 = file2[:,0], file2[:,1]
energy3, pdos3 = file3[:,0], file3[:,1]

plt.ylabel("PDOS")
plt.xlabel("Energy (eV)")
plt.plot(energy1,pdos1,color='red',label="cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#1(s)")
plt.plot(energy2,pdos2,color='blue',label="cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#2(p)")
plt.plot(energy3,pdos3,color='violet',label="cunipt-pdos.dat.pdos_atm#1(Cu)_wfc#3(d)")
plt.legend()

plt.savefig('pdos_spd.png')
plt.show()
