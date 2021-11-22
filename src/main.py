import tkinter as tk
from main_config import *
from kzmodules import *

kzm = kzmodules()

__user__ = kzm.user_info
__useros__ = kzm.os_name + ' ' + kzm.os_release + ' | ' +  kzm.os_version

class onclick:
    def terminal():
        kzm.open_current_directory(config_location_terminal)
    def internet():
        kzm.open_current_directory(config_location_internet)
    def external_executor():
        kzm.open_current_directory(config_location_misc_external_executor)
    def games_warship_arcade():
        kzm.open_current_executable(config_location_games_warship_arcade)
    def games_3d_voxel():
        kzm.open_current_executable(config_location_games_3d_voxel)
    def games_aim_trainer():
        kzm.open_current_executable(config_location_games_aim_trainer)
    def interpreter():
        kzm.open_current_directory(config_location_interpreter)
    def misc():
        kzm.open_current_directory(config_location_misc)
    def about():
        kzm.open_current_directory(config_location_about)


root = tk.Tk()
root.title(config_window_title)
root.geometry(config_window_size)
root.configure(background=config_window_background)
root.resizable(0, 0)

header = tk.Label(text='NECER', fg='blue')
header.config(font=(config_window_font, 15))
header.configure(background=config_window_background)
header.pack()

surheader = tk.Label(text='────────────Menu────────────')
surheader.config(font=(config_window_font, 10))
surheader.configure(background=config_window_background)
surheader.pack()


terminal_button = tk.Button(root, text='Terminal', bg='black', fg='red', command=onclick.terminal)
terminal_button.place(relx=0.1, rely=0.1)
terminal_button.config(font=(config_window_font, 12))

internet_button = tk.Button(root, text='internet', bg='black', fg='yellow', command=onclick.internet)
internet_button.place(relx=0.1, rely=0.2)
internet_button.config(font=(config_window_font, 12))

external_executor_button = tk.Button(root, text='External Script Executor', bg='grey', command=onclick.external_executor)
external_executor_button.place(relx=0.1, rely=0.4)
external_executor_button.config(font=(config_window_font, 12))


gamezonelabel = tk.Label(text='───────────Games───────────')
gamezonelabel.place(relx=0.1, rely=0.56)
gamezonelabel.config(font=(config_window_font, 10))
gamezonelabel.configure(background=config_window_background)


games_warship_arcade_button = tk.Button(root, text='Warship-Arcade', bg='white', fg='black', command=onclick.games_warship_arcade)
games_warship_arcade_button.place(relx=0.1, rely=0.6)
games_warship_arcade_button.config(font=(config_window_font, 12))

games_3d_voxel_button = tk.Button(root, text='3D-Voxel', bg='white', fg='black', command=onclick.games_3d_voxel)
games_3d_voxel_button.place(relx=0.1, rely=0.7)
games_3d_voxel_button.config(font=(config_window_font, 12))

games_aim_trainer_button = tk.Button(root, text='Aim-Trainer', bg='white', fg='black', command=onclick.games_aim_trainer)
games_aim_trainer_button.place(relx=0.1, rely=0.8)
games_aim_trainer_button.config(font=(config_window_font, 12))

interpreter_button = tk.Button(root, text='Python Interpreter', bg='black', fg='lime', command=onclick.interpreter)
interpreter_button.place(relx=0.1, rely=0.3)
interpreter_button.config(font=(config_window_font, 12))

misc_button = tk.Button(root, text='Misc', bg='black', fg='white', command=onclick.misc)
misc_button.place(relx=0.8, rely=0.9)
misc_button.config(font=(config_window_font, 12))

about_button = tk.Button(root, text='!', bg='cyan', command=onclick.about)
about_button.place(relx=0.7, rely=0.9, width=25)
about_button.config(font=(config_window_font, 12))


userinfo =  tk.Label(root, text=__user__)
userinfo.place(relx=0.1, rely=0.89)
userinfo.config(font=(config_window_font, 10))
userinfo.configure(background=config_window_background)

osinfo =  tk.Label(root, text=__useros__)
osinfo.place(relx=0.1, rely=0.93)
osinfo.config(font=(config_window_font, 10))
osinfo.configure(background=config_window_background)


root.mainloop()