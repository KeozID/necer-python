import time
import socket
import webbrowser
from datetime import datetime
import platform
import py_compile
from tqdm import tqdm
from terminal_config import *

__useros__ = platform.system() + ' ' + platform.release() + ' ' +  platform.version()

print(terminal_start_message)
print("_________Terminal "+ config_build_version +"_________")

#___Parameter
secureboot = config_secure_boot

#___Author Settings
buildstatus = (config_build_status)
cmd_list = ("cmd-list: "+config_cmd_list)

#___Variable_and_Function
securelogintitle = ("#Secure // Boot Panel // login")
logintitle = ("Boot Panel // login")

def login():
    print(logintitle)
    print("#Secure boot is disabled")
    time.sleep(2)
    main()

def securelogin():
    print(securelogintitle)
    username = input("Username: ")
    password = input("Password: ")
    if username == config_username:
        print("username_right")
        if password == config_password:
            print("password_right")
            print("logging-in please wait...")
            time.sleep(2)
            main()

def main():
    run = True
    while run == True:
        command = input("terminal-main> ").lower()
        if command == "ls" or command == "list":
            print(config_cmd_list)
        if command == "quit":
            time.sleep(2)
            run = False
        if command == "about":
            print("Terminal " + config_build_version + " Created by Satria Bima")
            print("Build is", config_build_status)
            time.sleep(1)
        if command == "localip" or command == "ip":
            local_ip()
        if command == "browser" or command == "web":
            run = False
            browser()
        if command == "date" or command == "datetime":
            print(datetime.now())
        if command == "platform" or command == "os":
            print(__useros__)
        if command == "compile":
            filepath = str(input("pathfile: "))
            for i in tqdm(range(10)):
                time.sleep(0.1)
            py_compile.compile(filepath)

#___Feature
def local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)

def browser():
    webinput = str(input("Web: "))
    try:
        webbrowser.open("https://www."+webinput)
    except NameError:
        print("NO WEB")

#___Parameter_Check
if secureboot == True:
    securelogin()
if secureboot == False:
    login()

print(terminal_end_message)