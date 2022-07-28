from tkinter import *
from datetime import datetime
from time import *
import vlc
import threading
import RPi.GPIO as GPIO          

player = vlc.MediaPlayer('szum.mp3')

signal_en1 = 27
signal_en2 = 22
spin_speed = 17
micro = 12
toy = 5
mata = 13
move_detector = 16


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(signal_en1, GPIO.OUT)
GPIO.setup(signal_en2, GPIO.OUT)
GPIO.setup(spin_speed, GPIO.OUT)
GPIO.setup(toy, GPIO.OUT)
GPIO.setup(micro, GPIO.IN)
GPIO.setup(mata, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(move_detector, GPIO.IN)
global a
a = GPIO.PWM(spin_speed,50)
GPIO.output(signal_en1, GPIO.LOW)
GPIO.output(signal_en2, GPIO.LOW)

window = Tk()
window.title('Aplikacja do bujania dzieci')
window.geometry("880x560")

spin_counter=True

def spin():
    global spin_counter
    if spin_counter == True:
        global a
        a.start(100)
        GPIO.output(signal_en1, GPIO.LOW)
        GPIO.output(signal_en2, GPIO.HIGH)
        spin_button.config(bg ='red', text ="Wylacz bujanie")
        spin_counter = 0
    elif spin_counter == False:
        GPIO.output(signal_en2, GPIO.LOW)
        spin_button.config(text='Intensywne bujanie',font=('Arial',40), bg='#30acf8')
        spin_counter = True
        
def spin_slow():
    global spin_counter
    if spin_counter == True:
        global a
        a.start(30)
        GPIO.output(signal_en1, GPIO.LOW)
        GPIO.output(signal_en2, GPIO.HIGH)
        spin_slow_button.config(bg ='red', text ="Wylacz zabawke")
        spin_counter = 0
    elif spin_counter == False:
        GPIO.output(signal_en2, GPIO.LOW)
        spin_slow_button.config(text='Delikatne bujanie',font=('Arial',40), bg='#30acf8')
        spin_counter = True

    

play_sound= True      
def noise():
    global play_sound
    global player
    if play_sound == True :
        player.play()
        print('melodia ruszyla')
        play_sound = False
        noise_button.config(bg ='red', text ="zatrzymaj szum")
    else:
        print('nie działa')
        play_sound = True
        noise_button.config(bg ='#b1b3bc', text = "Łagodny szum")
        player.stop()
    
def stop():
    global spin_counter
    global play_sound
    global toy_counter
    global move_log
    global mata_log
    global crying_log
    spin_counter = 0
    play_sound = 0
    toy_counter = 0
    move_log = 0
    mata_log = 0
          
    noise()
    toy()
    spin()
    breath()
    movement()
    
    
toy_counter = True
spin_counter = True

def toy():
    global toy_counter
    if toy_counter == 1:
        print("Swieci")
        GPIO.output(5, GPIO.HIGH)
        toy_button.config(bg ='red', text ="Wylacz zabawke")
        toy_counter = 0
    elif toy_counter == 0:
        GPIO.output(5, GPIO.LOW)
        toy_button.config(bg ='#b1b3bc', text ="kolorowy mis")
        toy_counter = 1
    
#waiting functions

def spin_countdown():
    global spin_counter
    global toy
    while True:
        if spin_counter == 0:
            for i in range(0, 5):
                if spin_counter == 0:
                    sleep(1)
                    print("czas leci")
            spin_counter = True
            GPIO.output(signal_en2, GPIO.LOW)
            spin_button.config(text='Intensywne bujanie',font=('Arial',40), bg='#30acf8')
            spin_slow_button.config(text='Delikatne bujanie',font=('Arial',40), bg='#30acf8')
# 
def toy_countdown():
    global toy_counter
    while True:
        if toy_counter == 0:
#             toy_button.config(bg='green', text='Kreci sie')
            for i in range(0, 20):
                if toy_counter== 0:
                    sleep(1)
                    print("czas leci")
            toy_counter = True
            GPIO.output(5, GPIO.LOW)
            toy_button.config(bg ='#b1b3bc', text ="kolorowy mis")
        
    
        
#data from sensors to TXT files
crying_log = True
move_log = True
mata_log = True

def breath():
    global mata_log
    if mata_log == 1:
        mata_button.config(bg ='red', text ="Wylacz zapis") 
        mata_log = 0
    elif mata_log == 0:
        mata_button.config(text='Zapis z maty',font=('Arial',20), bg='#e2b3bc')   
        mata_log = 1


def data_from_mata():
    if GPIO.input(mata) == GPIO.LOW:
        with open('mata_log.txt', 'a') as file:
            current_time = datetime.now()
            date = str (current_time)
            file.write(date)
            file.write('\n')
            sleep(1)
            print("mata")
            
def movement():
    global move_log
    global crying_log
    if move_log == 1:
        move_button.config(bg ='red', text ="Wylacz zapis")    
        move_log = 0
        crying_log = 0
    elif move_log == 0:
        move_button.config(text='Aktywacja czujnika ruchu',font=('Arial',20), bg='#e2b3bc')   
        move_log = 1
        crying_log = 1

def data_from_move_sensor():
    if GPIO.input(move_detector) == GPIO.HIGH:
        with open('movement_log.txt', 'a') as file:
            current_time = datetime.now()
            date = str (current_time)
            file.write(date)
            file.write('\n')
            sleep(1)
        print('ruch')

    
def crying_data():
    if GPIO.input(micro) == GPIO.HIGH:
        with open('crying_log.txt', 'a') as file:
            current_time = datetime.now()
            data = str (current_time)
            file.write(data)
            file.write('\n')
            sleep(1)
        print("cry")


def data_saving():
    global crying_log
    global move_log
    global mata_log
    
    while True:
        if crying_log == 0:
            crying_data()
        if move_log == 0:
            data_from_move_sensor()
        if mata_log == 0:
            data_from_mata()

        
spin_button=Button(window, text='Intensywne bujanie',font=('Arial',40), bg='#30acf8',command=spin, width ='20', height = '2')
spin_button.place(x=1,y=10,width=500,height=130)
        
spin_slow_button=Button(window, text='Delikatne bujanie',font=('Arial',40), bg='#30acf8',command=spin_slow, width ='20', height = '2')
spin_slow_button.place(x=500,y=10,width=500,height=130)
        
noise_button = Button(window, text='Łagodny szum',font=('Arial',40), bg='#b1b3bc',command=noise, width ='20', height = '2')
noise_button.place(x=1,y=140,width=500,height=130)
        
toy_button=Button(window, text='Kolorowy mis',font=('Arial',40), bg='#b1b3bc',command=toy, width ='20', height = '2')
toy_button.place(x=501,y=140,width=500,height=130)
        
        
mata_button=Button(window, text='Zapis danych z maty',font=('Arial',40), bg='#e2b3bc',command=breath, width ='20', height = '2')
mata_button.place(x=1,y=270,width=500,height=130)
        
move_button=Button(window, text='Aktywacja czujnika ruchu',font=('Arial',20), bg='#e2b3bc',command=movement, width ='20', height = '2')
move_button.place(x=501,y=270,width=500,height=130)


stop_button=Button(window,text='STOP!',font=('Arial',45), bg='red',command=stop, width ='20', height = '2')
stop_button.place(x=1,y=400,width=1000,height=150)

spin_countdown_thread = threading.Thread(target = spin_countdown)
spin_countdown_thread.start()
toy_countdown_thread = threading.Thread(target = toy_countdown)
toy_countdown_thread.start()
data_save=threading.Thread(target=data_saving)
data_save.start()

window.mainloop()
if (data_save.is_alive()==True):
    data_save.join()
del data_save


print('koniec')


