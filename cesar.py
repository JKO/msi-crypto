#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
###################################################
#     IMPLEMENTANDO EL CIFRADO CESAR - MAESTRIA   #
###################################################
#                                                 #
# @version     0.001                              #
# @author      Jaime Andrés Restrepo (@DragonJAR) #
# @author      Juan Jacobo Tibaquirá(@jjtibaquira)#
#                                                 #
###################################################
#
#Importarmos las librerias necesarias, para uso de argumentos y la generacion del hash md5
import argparse
import hashlib
#Banner al Inicio
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Cifrado Cesar")
print(ascii_banner)
print("Por Jaime Restrepo y Jacobo Tibaquirá\n\n")

#Parseamos los parametros de entrada
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Archivo a cifrar/descifrar', dest='archivo')
parser.add_argument('-o', help='Archivo de Salida cifrado/descifrado', dest='salida')
parser.add_argument('-modo', help='modo a utilizar cifrar/descifrar', dest='modo')
parser.add_argument('-ll', help='llave de cifrar/descifrado', dest='llave', type=int)
args = parser.parse_args()

#Definimos las variables con base en los parametros ingresados
ARCHIVO = args.archivo
SALIDA = args.salida
LLAVE = args.llave
MODO = args.modo
CARACTERES = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
TRADUCIDO = ''

with file(ARCHIVO, 'r') as f:
   for line in f:
      for ch in line:
          if ch in CARACTERES:
              symbolIndex = CARACTERES.find(ch)
              if MODO == 'cifrar':
                TRADUCIDOIndex = symbolIndex + LLAVE
              elif MODO == "descifrar":
                TRADUCIDOIndex = symbolIndex - LLAVE
              if TRADUCIDOIndex >= len(CARACTERES):
                TRADUCIDOIndex = TRADUCIDOIndex - len(CARACTERES)
              elif TRADUCIDOIndex < 0:
                TRADUCIDOIndex = TRADUCIDOIndex + len(CARACTERES)
              TRADUCIDO = TRADUCIDO + CARACTERES[TRADUCIDOIndex]
          else:
            TRADUCIDO = TRADUCIDO + ch
f.close()

ArchivoResultado = open(SALIDA+".txt", "wx")

ArchivoResultado.write(TRADUCIDO)
ArchivoResultado.close()

def md5Checksum(rutaArchivo):
    with open(rutaArchivo, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print('EL checksum md5 de '+SALIDA+'.txt es:', md5Checksum(SALIDA+".txt"))