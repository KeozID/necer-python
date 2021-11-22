#!usr/bin/python

from misc_config import *

print(terminal_start_message)

def penghitung_bunga():
    uang = float(input('uang/modal: '))
    bunga = float(input('bunga: '))
    waktu = float(input('waktu(12=1th): '))
    print(((waktu/12)*(bunga/100)*uang)+uang)
    selectmt_loop()

def penghitung_pajak():
    uang = float(input('uang: '))
    tidak_pajak = float(input('tidak kena pajak: '))
    pajak = float(input('pajak: '))
    print(uang-((uang-tidak_pajak)*(pajak/100)))
    selectmt_loop()

def penghitung_no_pajak():
    uang = float(input('uang: '))
    pajak = float(input('pajak: '))
    print(uang+((pajak/100)*uang))
    selectmt_loop()

def selectmt_loop():
    run = True
    while run == True:
        selectmt = input('1(bunga), 2(pajak), 3(pajak only): ')
        if selectmt == '1':
            penghitung_bunga()
        if selectmt == '2':
            penghitung_pajak()
        if selectmt == '3':
            penghitung_no_pajak()
        if selectmt == 'exit':
            run = False
            exit

selectmt_loop()
print(terminal_end_message)