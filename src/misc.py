import tkinter as tk
from main_config import *
from kzmodules import *

kzm = kzmodules()

class onclick:
    def penghitung_bunga():
        kzm.open_current_directory(config_location_misc_penghitung_bunga)
    def pengubah_satuan_suhu():
        kzm.open_current_directory(config_location_misc_pengubah_satuan_suhu)
    def pengubah_satuan_suhu_advance():
        kzm.open_current_directory(config_location_misc_pengubah_satuan_suhu_advance)
    def kertas_batu_gunting():
        kzm.open_current_directory(config_location_misc_kertas_batu_gunting)
    def log():
        kzm.open_current_directory(config_location_log)


root = tk.Tk()
root.title(config_window_title)
root.geometry(config_window_size)
root.configure(background=config_window_background)
root.resizable(0, 0)


header = tk.Label(text='Miscellaneous', fg='blue')
header.config(font=(config_window_font, 15))
header.configure(background=config_window_background)
header.pack()

surheader = tk.Label(text='────────────Menu────────────')
surheader.config(font=(config_window_font, 10))
surheader.configure(background=config_window_background)
surheader.pack()


penghitung_bunga_button = tk.Button(root, text='Penghitung Bunga', bg='grey', command=onclick.penghitung_bunga)
penghitung_bunga_button.place(relx=0.1, rely=0.1)
penghitung_bunga_button.config(font=(config_window_font, 12))

pengubah_satuan_suhu_button = tk.Button(root, text='Pengubah Satuan Suhu', bg='grey', command=onclick.pengubah_satuan_suhu)
pengubah_satuan_suhu_button.place(relx=0.1, rely=0.2)
pengubah_satuan_suhu_button.config(font=(config_window_font, 12))

pengubah_satuan_suhu_advance_button = tk.Button(root, text='Pengubah Satuan Suhu(Advance)', bg='grey', command=onclick.pengubah_satuan_suhu_advance)
pengubah_satuan_suhu_advance_button.place(relx=0.1, rely=0.3)
pengubah_satuan_suhu_advance_button.config(font=(config_window_font, 12))

kertas_batu_gunting_button = tk.Button(root, text='Kertas Batu Gunting', bg='grey', command=onclick.kertas_batu_gunting)
kertas_batu_gunting_button.place(relx=0.1, rely=0.4)
kertas_batu_gunting_button.config(font=(config_window_font, 12))

log_button = tk.Button(root, text='ChangeLog', bg='black', fg='white', command=onclick.log)
log_button.place(relx=0.45, rely=0.9)
log_button.config(font=(config_window_font, 12))

def back_button_function():
    quit()
back_button = tk.Button(root, text='Back', bg='black', fg='white', command=back_button_function)
back_button.place(relx=0.8, rely=0.9)
back_button.config(font=(config_window_font, 12))


root.mainloop()