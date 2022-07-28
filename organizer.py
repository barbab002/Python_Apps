import fnmatch
import os
import shutil

extensions = ['*.exe','*.xlsx','*.jpg','*.doc','*docx','*.pdf','*.zip','*.rar','*.zip','*.csv','*.html']
folders = ['EXE','XLXS','RAR','ZDJECIA','PDF','DOC','html']
dir = os.listdir('.')
for i in range(0,len(folders)):
    try:
        os.makedirs(folders[i])
    except:
        print("elo")

#shutil.move(dir[0],folders[0])
for i in range (0,len(extensions)):
    for file in dir:
        if fnmatch.fnmatch(file,extensions[i]):
            print(file)
            if extensions[i] == extensions[0]:
                shutil.move(file,folders[0])
            if extensions[i] ==  extensions[1]:
                shutil.move(file,folders[1])
            if extensions[i] ==  extensions[2]:
                shutil.move(file,folders[3])
            if extensions[i] ==  extensions[3]:
                print("siema")
                shutil.move(file,folders[4])
            if extensions[i] ==  extensions[4]:
                shutil.move(file,folders[4])
            if  extensions[i] == extensions[5]:
                shutil.move(file,folders[5])
            if  extensions[i] == extensions[7]:
                shutil.move(file,folders[2])
            if  extensions[i] == extensions[8]:
                try:
                    shutil.move(file,folders[2])
                except: print('')   
            if  extensions[i] == extensions[9]:
                try:
                    shutil.move(file,folders[1])
                except: print('')    
            if  extensions[i] == extensions[10]:
                try:
                    shutil.move(file,folders[6])       
                except: print('') 
# 
# extensions = ['*.exe','*.xlxs','*.jpg','*.doc','*docx','*.pdf','*.zip','*.rar',']
# folders = ['EXE','XLXS','RAR','ZDJECIA','PDF','DOC']