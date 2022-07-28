import fnmatch
import os
import shutil

extensions = ['*.exe','*.xlxs','*.jpg','*.doc','*docx','*.pdf','*.zip','*.rar']
folders = ['EXE','XLXS','RAR','ZDJECIA','PDF']
dir = os.listdir('.')


#shutil.move(dir[0],folders[0])
for file in dir:
    if fnmatch.fnmatch(file,extensions[0]):
        print(file)
        shutil.move(file,folders[0])
