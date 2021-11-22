#!usr/bin/python

from misc_config import *

print(terminal_start_message)

print("Pengubah Satuan Suhu @Satria Bima")
print("---------------------------------")
print("1.Celcius, 2.Fahrenheit, 3.Kelvin, 4.Reamur")
pilihopsi = input("Dari(1/2/3/4)? ")

if pilihopsi == "1":
        inpt = input("celsius: ")
        print("Fahrenheit:", float(inpt)*(9/5)+32)
        print("Kelvin:", float(inpt)+273.15)
        print("Reamur:", 4/5*float(inpt))

if pilihopsi == "2":
        inpt = input("fahrenheit: ")
        print("Celcius:", (float(inpt)-32)*5/9)
        print("Kelvin:", (float(inpt)-32)*5/9+273.15)
        print("Reamur:", (float(inpt)-32)*4/9)

if pilihopsi == "3":
        inpt = input("kelvin: ")
        print("Celcius:", float(inpt)-273.15)
        print("fahrenheit:", (float(inpt)-273.15)*9/5+32)
        print("Reamur:",(float(inpt)-273.15)*(4/5))

if pilihopsi == "4":
        inpt = input("reamur: ")
        print("Celcius:", 5/4*float(inpt))
        print("Fahrenheit:", 9/4*float(inpt)+32)
        print("Kelvin:", 5/4*float(inpt)+273.15)

print(terminal_end_message)