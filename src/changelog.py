import tkinter as tk
from main_config import *

config_window_size = '400x300'

root = tk.Tk()
root.title(config_window_title)
root.geometry(config_window_size)
root.configure(background=config_window_background)
root.resizable(0, 0)

header = tk.Label(text='ChangeLog', fg='black')
header.config(font=(config_window_font, 15))
header.configure(background=config_window_background)
header.pack()

version_info = tk.Label(text=config_about_build, fg='black')
version_info.config(font=(config_window_font, 15))
version_info.configure(background=config_window_background)
version_info.pack()

ch1 = tk.Label(root, text='-new feature >> terminal new feature').pack()
ch2 = tk.Label(root, text='-compiler >> pyc compiler').pack()
ch3 = tk.Label(root, text='-interpreter >> added python interpreter (python required)').pack()
ch4 = tk.Label(root, text='-datetime >> display time and date').pack()
ch5 = tk.Label(root, text='-ui >> ui revamped').pack()
ch6 = tk.Label(root, text='-launcher >> added event logger for debugging').pack()
ch7 = tk.Label(root, text='-code >> simplified onclick function blocks').pack()

def back_button_function():
    quit()
back_button = tk.Button(root, text='Back', bg='black', fg='white', command=back_button_function)
back_button.place(relx=0.8, rely=0.8)
back_button.config(font=(config_window_font, 12))


root.mainloop()