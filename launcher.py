import socket
import os
import time
import platform
import getpass
import logging
from datetime import datetime
from pathlib import Path

LOG_INFO_MESSAGE =  '[INFO] '
LOG_ERROR_MESSAGE = '[ERROR] '
LOG_DEBUG_MESSAGE = '[DEBUG] '
LOG_DATE = datetime.now()

logging.basicConfig(filename="launcher.log", level=logging.INFO)
logging.info(LOG_DATE)
logging.info(LOG_INFO_MESSAGE + 'Boot')

config_location_main = 'src/main.py'
FileExists = Path(config_location_main)

class boolean():
    checkstart = True

def start():
    if FileExists.is_file() == True:
        logging.info(LOG_INFO_MESSAGE + 'File Found')
        logging.info(LOG_INFO_MESSAGE + 'Opening File')
        print("[CONSOLE] New Session")
        os.system(os.path.join(__location__, config_location_main))
        print("[CONSOLE] Terminating..")
        logging.info(LOG_INFO_MESSAGE + 'Shutdown')
        time.sleep(1)
        exit()

    elif FileExists.is_file() == False:
        logging.error(LOG_ERROR_MESSAGE + 'File Not Found')
        print("[CONSOLE] File Not Found: Terminating..")
        time.sleep(1)
        exit()

__user__ = os.path.join(getpass.getuser())
__useros__ = platform.system() + ' ' + platform.release() + ' ' +  platform.version()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

__hostname__ = socket.gethostname()
__localip__ = socket.gethostbyname(__hostname__)

def check():
    if boolean.checkstart == True:
        print("OS: " + __useros__ + "            LOCAL_IP: " + __localip__)
        print("USER: " + __user__)
        print("───────────────────────────────────────────────────────────────────<")
        start()
    elif boolean.checkstart == False:
        start()
check()