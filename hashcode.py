#!/usr/bin/env python3.5
#coding: utf-8

'''
HashCode
'''

import hashlib
from base64 import b64encode, b64decode
from time import sleep
from sys import exit
import os

Limpar = "reset"

def Apresentacao():
	os.system(Limpar)
	print('''\033[31m

 ▄  █ ██      ▄▄▄▄▄    ▄  █     ▄█▄    ████▄ ██▄   ▄███▄   
█   █ █ █    █     ▀▄ █   █     █▀ ▀▄  █   █ █  █  █▀   ▀  
██▀▀█ █▄▄█ ▄  ▀▀▀▀▄   ██▀▀█     █   ▀  █   █ █   █ ██▄▄    
█   █ █  █  ▀▄▄▄▄▀    █   █     █▄  ▄▀ ▀████ █  █  █▄   ▄▀ 
   █     █               █      ▀███▀        ███▀  ▀███▀   
  ▀     █               ▀                               
       ▀                             By: Magno-Tutor   \033[1;m
''')


def Escolha():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar.

\033[31m1\033[1;m) Encode - MD5
\033[31m2\033[1;m) Encode - Sha1
\033[31m3\033[1;m) Encode - Sha224
\033[31m4\033[1;m) Encode - Sha256
\033[31m5\033[1;m) Encode - Sha384
\033[31m6\033[1;m) Encode - Sha512
\033[31m7\033[1;m) Encode - Base64
\033[31m8\033[1;m) Cifra de César

\033[31mq\033[1;m) Sair
""")
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		Md5()
	elif opcao1 == "2":
		Sha1()
	elif opcao1 == "3":
		Sha224()
	elif opcao1 == "4":
		Sha256()
	elif opcao1 == "5":
		Sha384()
	elif opcao1 == "6":
		Sha512()
	elif opcao1 == "7":
		Base64()
	elif opcao1 == "8":
		CifraDeCesar()
	elif opcao1 == "q":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Md5():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em MD5\033[1;m: ")
		hash_object = hashlib.md5(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode MD5 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Md5()
		elif opcao1 == "n":
			Escolha()

def Sha1():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em Sha1\033[1;m: ")
		hash_object = hashlib.sha1(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode SHA1 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Sha1()
		elif opcao1 == "n":
			Escolha()

def Sha224():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em Sha224\033[1;m: ")
		hash_object = hashlib.sha224(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode SHA224 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Sha224()
		elif opcao1 == "n":
			Escolha()

def Sha256():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em Sha256\033[1;m: ")
		hash_object = hashlib.sha256(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode SHA256 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Sha256()
		elif opcao1 == "n":
			Escolha()

def Sha384():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em Sha384\033[1;m: ")
		hash_object = hashlib.sha384(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode SHA384 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Sha384()
		elif opcao1 == "n":
			Escolha()

def Sha512():
		Apresentacao()
		mystring = input("\033[32mColoque o texto que queira encriptar em Sha512\033[1;m: ")
		hash_object = hashlib.sha512(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode SHA512 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Sha512()
		elif opcao1 == "n":
			Escolha()

def Base64():
		Apresentacao()
		mystring = str(input("\033[32mColoque o texto que queira encriptar em base64\033[1;m: ")) 
		print("")
		encode = b64encode(mystring.encode('utf-8')) 
		decode = encode.decode('utf-8')
		print(decode)
		print("") 
		opcao1 = input("\n\033[1;36mDeseja fazer outro encode BASE64 (s/n) ?:\033[1;m ")
		if opcao1 == "s":
			Base64()
		elif opcao1 == "n":
			Escolha()

def CifraDeCesar():
		Apresentacao()
		print("""
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar.

\033[31m1\033[1;m) Encode - Cifra de César
\033[31m2\033[1;m) Decode - Cifra de César
""")
		opcao1 = input("\033[1;36mOpção:\033[1;m ")
		if opcao1 == "1":
			ChamarBloco1()
		elif opcao1 == "2":
			ChamarBloco2()

def cifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado


def decifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def ChamarBloco1():
	Apresentacao()
	c = str(input('\n\033[32mTexo a ser cifrado\033[1;m: ')).lower()
	n = int(input('\033[32mChave numérica\033[1;m: '))
	print("\033[32mResultado\033[1;m:", cifrar(c, n))
	opcao1 = input("\n\033[1;36mDeseja fazer outro encode da CIFRA DE CÉSAR (s/n) ?:\033[1;m ")
	if opcao1 == "s":
		ChamarBloco1()
	elif opcao1 == "n":
		Escolha()

def ChamarBloco2():
	Apresentacao()
	cc = str(input('\n\033[32mTexto para ser decifrado\033[1;m: ')).lower()
	cn = int(input('\033[32mChave numérica\033[1;m: '))
	print("\033[32mResultado\033[1;m:", decifrar(cc, cn))
	opcao1 = input("\n\033[1;36mDeseja fazer outro decode da CIFRA DE CÉSAR (s/n) ?:\033[1;m ")
	if opcao1 == "s":
		ChamarBloco2()
	elif opcao1 == "n":
		Escolha()


def ComandoNaoEncontrado():
	print("""
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado.
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor.

""")

Escolha()
