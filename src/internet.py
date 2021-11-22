import tkinter as tk
from main_config import *
from kzmodules import *

kzm = kzmodules()

class onclick():
    def bchost():
        kzm.open_current_directory(config_location_bchost)
    def bcclient():
        kzm.open_current_directory(config_location_bcclient)


config_window_size = "300x150"


root = tk.Tk()
root.title(config_window_title)
root.geometry(config_window_size)
root.configure(background=config_window_background)
root.resizable(0, 0)

header = tk.Label(root, text='INTERNET', fg='black')
header.config(font=(config_window_font, 15))
header.configure(background=config_window_background)
header.pack()

bchost_button = tk.Button(root, text='Broadcast-Host', bg='gray', fg='black', command=onclick.bchost)
bchost_button.place(relx=0.1, rely=0.3)
bchost_button.config(font=(config_window_font, 12))

bcclient_button = tk.Button(root, text='Broadcast-Client', bg='gray', fg='black', command=onclick.bcclient)
bcclient_button.place(relx=0.1, rely=0.6)
bcclient_button.config(font=(config_window_font, 12))

root.mainloop()