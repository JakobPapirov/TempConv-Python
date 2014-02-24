#!/usr/bin/python
# -*- coding: utf-8 -*-

# Program file-name: TempKonv
# Author: Jakob Papirov
# Date created | last updated: 2014-01-16 | 2014-01-17

print('Detta program låter dig konvertera mellan Fahrenheit, Celcius och Kelvin')

iterera = 'True'

while iterera == 'True':
	print(' ')
	print('Du kan välja mellan:')
	print('1. Konvertera från Fahrenheit till Celcius. ')
	print('2. Konvertera från Celcius till Fahrenheit. ')
	print('3. Konvertera från Celcius till Kelvin. ')
	print('4. Konvertera från Kelvin till Celcius. ')
	print('5. Konvertera från kelvin till Fahrenheit. ')
	print('6. Konvertera från Fahrenheit till Kelvin. ')
	print('0. Avsluta programmet.')
	
	print(' ')
	Choice_main = int(input('Vad vill du göra? '))

	if Choice_main == 1:
		F2C = float(input('Vilken är temperaturen i Fahrenheit? '))
		C = (F2C - 32) * float(5./9)
		print('Temperaturen i Celcius är ' + str(C) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 2:
		C2F = float(input('Vilken är temperaturen i Celcius? '))
		F = (C2F * float(9./5)) + 32
		print('Temperaturen i Fahrenheit är ' + str(F) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 3:
		C2K = float(input('Vilken är temperaturen i Celcius? '))
		K = C2K + 273.15
		print('Temperaturen i Kelvin är ' + str(K) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 4:
		K2C = float(input('Vilken är temperaturen i Kelvin? '))
		C = K2C - 273.15
		print('Temperaturen i Celcius är ' + str(C) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 5:
		K2F = float(input('Vilken är temperaturen i Kelvin? '))
		C = K2F - 273.15
		F = (C * float(9./5)) + 32
		print('Temperaturen i Fahrenheit är ' + str(F) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 6:
		F2K = float(input('Vilken är temperaturen i Fahrenheit? '))
		C = (F2K - 32) * float(5./9)
		K = C + 273.15
		print('Temperaturen i Kelvin är ' + str(K) + ' grader.')
		print('Du går nu tillbaka till startmenyn.')
	elif Choice_main == 0:
		print('Du har avslutat programmet.')
		iterera = 'False'
	else:
		print('Du har gett fel input, var god och försök på nytt.')
	

# Comments
# I python 3.x raw_input() byts ut mot input()
# Fungerar!
# Översätt till Engelska!
