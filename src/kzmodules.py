from tqdm import tqdm
import time
import os
import platform
import getpass
import socket
import webbrowser


class kzmodules:

    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()

    user_info = os.path.join(getpass.getuser())

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    def open_directory(self, file_location):
        """Open file with the full path writed in parameter"""
        os.system(file_location)
    
    def open_executable(self, file_location):
        """Open executable with the full path writed in parameter"""
        os.popen(file_location)

    def open_current_directory(self, file_location):
        """Open file in the current directory"""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        __dirfile__ = os.system(os.path.join(__location__, file_location))
        
    def open_current_executable(self, file_location):
        """Open executable in the current directory"""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        __dirfile__ = os.popen(os.path.join(__location__, file_location))

    def open_website(self, url):
        """Open a website based on the url entered in parameter"""
        webbrowser.open_new(url)

    def loading_bar(self, loading_range, loading_time):
        """Visualize loading bar with the value based on parameter"""
        for i in tqdm(range(loading_range)):
            time.sleep(loading_time)

    def merge_arrays(self, array1, array2):
        """Merge 2 arrays in one line"""
        result = array1 + array2
        return result