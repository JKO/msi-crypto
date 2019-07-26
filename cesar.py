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
import argparse

#Parseamos los parametros de entrada
parser = argparse.ArgumentParser()
parser.add_argument('-m', help='mensaje a cifrar/descifrar', dest='mensaje')
parser.add_argument('-modo', help='modo a utilizar cifrar/descifrar', dest='modo')
parser.add_argument('-ll', help='llave de cifrar/descifrado', dest='llave', type=int)
args = parser.parse_args()

#Definimos las variables con base en los parametros ingresados
MENSAJE =  args.mensaje
LLAVE = args.llave
MODO = args.modo
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
TRADUCIDO = ''

#Iniciamos el ciclo de cifrado/decifrado
for symbol in MENSAJE:
    if symbol in CARACTERES:
        symbolIndex = CARACTERES.find(symbol)
        if MODO == 'cifrar':
            TRADUCIDOIndex = symbolIndex + LLAVE
        elif MODO == 'descifrar':
            TRADUCIDOIndex = symbolIndex - LLAVE
        if TRADUCIDOIndex >= len(CARACTERES):
            TRADUCIDOIndex = TRADUCIDOIndex - len(CARACTERES)
        elif TRADUCIDOIndex < 0:
            TRADUCIDOIndex = TRADUCIDOIndex + len(CARACTERES)
        TRADUCIDO = TRADUCIDO + CARACTERES[TRADUCIDOIndex]
    else:
        TRADUCIDO = TRADUCIDO + symbol
print(TRADUCIDO)
