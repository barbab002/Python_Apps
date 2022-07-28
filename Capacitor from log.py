import os, fnmatch
import codecs

kondziory = ["0.4\n","0.7\n","1.2\n","1.5\n",'1.8\n','2.2\n','2.7\n','3.3\n','3.9\n','4.7\n','5.6\n','6.8\n','8.1\n']

SN_to_copy = '*Adjustment*fail*.html'
file_count = sum(len(files) for _, _, files in os.walk(r'./'))


def find(pattern, path):
    global result
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(name))
    return result

def count_cases():
    wynik = 0
    file = open("dane.txt",'r')
    linie = file.readlines()
    for x in range (0,len(kondziory)):
        for i in linie:
            if i == kondziory[x]:
                wynik +=1
        print ("wynik dla",kondziory[x], wynik)
        wynik =0
        print("\n")
    file.close()
    
def save_txt(cap1,cap2,cap3,cap4,cap5):
    file = open ("dane.txt", 'a')
    file.write(cap1)
    file.write("\n")
    file.write(cap2)
    file.write("\n")
    file.write(cap3)
    file.write("\n")
    file.write(cap4)
    file.write("\n")
    file.write(cap5)
    file.write("\n")
    file.close()

find(SN_to_copy,'./')


for i in range (0,10):
    global result
    f = codecs.open(result[i], 'r', 'ANSI')
    a = str(f.read())
    c205 = a.find("""Capacitor welded for 27MHz Adjustment C205 (pF)</FONT></TH><FONT size=2>""")
    c205_end = a.find("""<TH align=middle width="30%"><FONT size=2>Capacitor welded for 27MHz Adjustment C605 (pF)</FONT></TH><FONT size=2>""")
    c605 = a.find('''Capacitor welded for 27MHz Adjustment C605 (pF)</FONT></TH><FONT size=2>''')
    c605_end = a.find("""Coupling type for 27MHz Adjustment""")
    c207 = a.find('''Capacitor welded for Modulator Adjustment C207 (pF)</FONT></TH><FONT size=2>''')
    c207_end = c207+110
    c181 = a.find('''<TH align=middle width="30%"><FONT size=2>Capacitor welded for 27MHz Adjustment C181 (pF)</FONT></TH><FONT size=2>''')
    c181_end = a.find('''<TH align=middle width="30%"><FONT size=2>Capacitor welded for 27MHz Adjustment C919 (pF)</FONT></TH><FONT size=2>''')
    c919 = a.find('''<TH align=middle width="30%"><FONT size=2>Capacitor welded for 27MHz Adjustment C919 (pF)</FONT></TH><FONT size=2>''')
    c919_end = a.find('''Coupling type for 27MHz Adjustment''')
    d1 = (a[c205+103:c205_end-25])
    d2 = (a[c605+103:c605_end-55])
    d3 = (a[c207+107:c207_end])
    d4 = (a[c181+145:c181_end-25])
    d5 = (a[c919+145:c919_end-55])
    if (len(d1)>4):
        cap1=''
    elif(len(d1)<4):
        cap1 = d1
    if (len(d1)>4):
        cap2 = ''
    elif(len(d2)<4):
        cap2 = d2
    if (len(d3)>4):
        cap3=''
    elif(len(d3)<4):
        if d3 == """-</""":
            cap3 = "0.0"
        elif d3 !="""-</""":
            cap3 = d3
    if (len(d4)>4):
        cap4=''
    elif(len(d4)<4):
        cap4 = d4
    if (len(d5)>4):
        cap5=''
    elif(len(d5)<4):
        cap5 = d5
    print (cap1,cap2,cap3,cap4,cap5,'\n')
    save_txt(cap1,cap2,cap3,cap4,cap5)    

count_cases() 
