import fnmatch
from ftplib import FTP
import glob
import os

ftp = FTP()
ftp.connect('SERVER IP', 8821)
ftp.login("username", "password")
ftp.cwd("51.195.242.50_7040/")
print(ftp.dir())
files = ftp.nlst()

for i in files:
    if fnmatch.fnmatch(i, "login*"):
        print("Downloading " + i)
        try:
            ftp.retrbinary("RETR " + i, open("./" + i, 'wb').write)
        except EOFError:
            pass

ftp.close()

local_files = glob.glob("*.log")
final_log = open("logs.txt", 'a')

for f in local_files:
    try:
        content = open("./" + f, 'r')
        final_log.write(str(content.read()))
        content.close()
    except UnicodeDecodeError:
        pass

for i in local_files:
    os.remove(i)
    
    
