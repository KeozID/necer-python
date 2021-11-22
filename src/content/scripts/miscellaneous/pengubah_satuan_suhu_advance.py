#!usr/bin/python

from misc_config import *

print(terminal_start_message)

print("Pengubah Satuan Suhu @Satria Bima")
print("---------------------------------")
print("1.Dari Celsius, 2.Dari Fahrenheit, 3.Dari Kelvin, 4.Dari Reamur")
pilihopsi = input("Dari(1/2/3/4)? ")

if pilihopsi == "1":
    print("1.Fahrenheit, 2.Kelvin, 3.Reamur")
    pilihc = input("Operasi(1/2/3)? ")
    print("-----------")

    if pilihc == "1":
        print("Celsius ke Fahrenheit")
        fahrenheit = input("celsius: ")
        print(float(fahrenheit)*(9/5)+32)
        input()
    if pilihc == "2":
        print("Celsius ke Kelvin")
        kelvin = input("celsius: ")
        print(float(kelvin)+273.15)
        input()
    if pilihc == "3":
        print("Celsius ke Reamur")
        reamur = input("celsius: ")
        print(4/5*float(reamur))
        input()

if pilihopsi == "2":
    print("1.Celsius, 2.Kelvin, 3.Reamur")
    pilihf = input("Operasi(1/2/3)? ")
    print("-----------")
    
    if pilihf == "1":
        print("Fahrenheit ke Celsius")
        celsius = input("fahrenheit: ")
        print((float(celsius)-32)*5/9)
        input()
    if pilihf == "2":
        print("Fahrenheit ke Kelvin")
        kelvin = input("fahrenheit: ")
        print((float(kelvin)-32)*5/9+273.15)
        input()
    if pilihf == "3":
        print("Fahrenheit ke Reamur")
        reamur = input("fahrenheit: ")
        print((float(reamur)-32)*4/9)
        input()

if pilihopsi == "3":
    print("1.Celsius, 2.Fahrenheit, 3.Reamur")
    pilihk = input("Operasi(1/2/3)? ")
    print("-----------")

    if pilihk == "1":
        print("Kelvin ke Celsius")
        celsius = input("kelvin: ")
        print(float(celsius)-273.15)
        input()
    if pilihk == "2":
        print("Kelvin ke Fahrenheit")
        fahrenheit = input("kelvin: ")
        print((float(fahrenheit)-273.15)*9/5+32)
        input()
    if pilihk == "3":
        print("Kelvin ke Reamur")
        reamur = input("kelvin: ")
        print((float(reamur)-273.15)*(4/5))
        input()

if pilihopsi == "4":
    print("1.Celsius, 2.Fahrenheit, 3.Kelvin")
    pilihr = input("Operasi(1/2/3)? ")
    print("-----------")

    if pilihr == "1":
        print("Reamur ke Celsius ")
        celsius = input("reamur: ")
        print(5/4*float(celsius))
        input()
    if pilihr == "2":
        print("Reamur ke Fahrenheit")
        fahrenheit = input("reamur: ")
        print(9/4*float(fahrenheit)+32)
        input()
    if pilihr == "3":
        print("Reamur ke Kelvin")
        kelvin = input("reamur: ")
        print(5/4*float(kelvin)+273.15)
        input()

print(terminal_end_message)