"""
Archivo principal práctica 1 CRIP.
Autores: Alberto Armijo Ruiz. Juan Alberto Martínez López.
"""

from logaritmo import medirTiempos
import csv
import sys


if __name__ == "__main__":

    # Comprobamos que le hemos pasado el nombre del archivo de la batería de pruebas.
    if(len(sys.argv) < 2):
        print("Introduzca el nombre del archivo de entrada")
        exit

    out_file = open("output.csv",'w')
    out_file.write("A,B,Primo,Tiempo (seg) \n")
    tiempos_miller_rabin = open("time_rabin.csv",'w')
    tiempos_miller_rabin.write("Primo,Tiempo (seg)\n")
    print("Leyendo el archivo de entrada.")
    file_name = sys.argv[1]
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            a = int(row[0])
            b = int(row[1])
            p = int(row[2])
            print("Calculando ejemplo: {0:d},{1:d},{2:d}".format(a,b,p))
            time = medirTiempos(args=list([a,b,p]))
            out_file.write("{0:d},{1:d},{2:d},{3:f} \n".format(a,b,p,time) )
            time = medirTiempos(args=list([p,2000]),miller_rabin=True)
            tiempos_miller_rabin.write("{0:d}, {1: f} \n".format(p,time))


    out_file.close()
    tiempos_miller_rabin.close()
