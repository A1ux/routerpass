#!/usr/bin/python
#stdONUi0i
##Guardar la ip,nombre,pass en un csv

from ftplib import FTP
from xml.dom import minidom
import csv
import sys
from os import remove

##Datos conexion
host = sys.argv[1]
user = "user"
password = "user"

#Archivos a Descargar
archivo1 = 'lastgood.xml'
archivo2 = 'lastgood_hs.xml'

def descargarArchivos():
    try:
        tp = FTP(host,user,password)
        tp.cwd('/var/config')
        with open( archivo1, 'w' ) as file :
            tp.retrbinary('RETR %s' % archivo1, file.write)
        with open( archivo2, 'w' ) as file :
            tp.retrbinary('RETR %s' % archivo2, file.write)    
        tp.close()
    except:
        print ("Eror al conectarse, consulte el log")
        try:
            f = open("errores.log",'a')
            f.write("Error en ip ")
            f.write(host)
            f.write("\n")
        except:
            print ("Error al abrir archivo de log")

def sacarSSID():
    doc = minidom.parse('lastgood.xml')
    valor = doc.getElementsByTagName("Value")
    for skill in valor:
        if skill.getAttribute("Name") == 'ssid':
            ssid = skill.getAttribute("Value")
            break
    return ssid

def sacarPass():
    doc = minidom.parse('lastgood.xml')
    valor = doc.getElementsByTagName("Value")
    for skill in valor:
        if skill.getAttribute("Name") == 'WLAN_WPA_PSK':
            passwifi = skill.getAttribute("Value")
            break
    return passwifi

def sacarMac():
    doc2 = minidom.parse('lastgood_hs.xml')
    valor2 = doc2.getElementsByTagName("Value")
    for skill in valor2:
        if skill.getAttribute("Name") == 'ELAN_MAC_ADDR':
            macwifi = skill.getAttribute("Value")
            break
    return macwifi

def agregarCSV():
    datosWifi = [[host,sacarMac(),sacarSSID(),sacarPass()]]
    try:
        with open('datos.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerows(datosWifi)
        print "Contrasenas guardadas"
    except:
        print ("Error al escribir csv")

def eliminarArchivos():
    remove(archivo1)
    remove(archivo2)

def main():
    host = sys.argv[1]
    descargarArchivos()
    agregarCSV()
    eliminarArchivos()

if __name__ == "__main__":
    main()
