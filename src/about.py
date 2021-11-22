import tkinter as tk
from main_config import *
from kzmodules import *

kzm = kzmodules()

class onclick:
    def youtube_link():
        kzm.open_website(config_link_about_youtube)
    def instagram_link():
        kzm.open_website(config_link_about_instagram)
    def facebook_link():
        kzm.open_website(config_link_about_facebook)
    def github_link():
        kzm.open_website(config_link_about_github)


config_window_size = '300x100'


root = tk.Tk()
root.title(config_window_title)
root.geometry(config_window_size)
root.configure(background=config_window_background)
root.resizable(0, 0)


header = tk.Label(text='About', fg='blue')
header.config(font=(config_window_font, 12))
header.configure(background=config_window_background)
header.pack()

creator = tk.Label(root, text='Creator: ' + config_about_creator)
creator.configure(background=config_window_background)
creator.place(relx=0.1, rely=0.2)

version = tk.Label(root, text='Version: ' + config_about_build)
version.configure(background=config_window_background)
version.place(relx=0.1, rely=0.4)


youtube_link_button = tk.Button(root, text='Youtube', bg='red', fg='white', command=onclick.youtube_link)
youtube_link_button.place(relx=0.1, rely=0.6)

instagram_link_button = tk.Button(root, text='instagram', bg='orange', fg='white', command=onclick.instagram_link)
instagram_link_button.place(relx=0.3, rely=0.6)

facebook_link_button = tk.Button(root, text='Facebook', bg='blue', fg='white', command=onclick.facebook_link)
facebook_link_button.place(relx=0.53, rely=0.6)

github_link_button = tk.Button(root, text='github', bg='purple', fg='white', command=onclick.github_link)
github_link_button.place(relx=0.75, rely=0.6)


def back_button_function():
    quit()
back_button = tk.Button(root, text='Back', bg='black', fg='white', command=back_button_function)
back_button.place(relx=0.80, rely=0.1)
back_button.config(font=(config_window_font, 8))

root.mainloop()