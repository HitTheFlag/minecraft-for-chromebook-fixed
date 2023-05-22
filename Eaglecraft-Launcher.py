import shutil
import subprocess

source_file = '/downloads/Eaglecraft-Launcher.py'
startup_folder = '/home/chronos/user/Startup/'

shutil.move(source_file, startup_folder)

def turn_off_chrome_os():
    subprocess.run(['sudo', 'poweroff'])
    
turn_off_chrome_os()
