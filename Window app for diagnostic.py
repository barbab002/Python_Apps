import serial
import time
import tkinter as tk
global serialPort


window = tk.Tk()
window.title("DIAGNOSTYKA FACTORY SECRET")
frame = tk.Frame(master=window, width=450, height=500)
frame.pack()

#initialization

init_start = [0x01,0xAA,0xBB,0x07,0x00,0x00,0x00,0x03]
voter_start = [0x01,0xAA,0xBB,0x0b,0x00,0x00,0x00,0x03]
relay_start = [0x01,0xAA,0xBB,0x0b,0x00,0x02,0x00,0xfd,0x02,0x03]
relay_set = [0x01,0xAA,0xBB,0x0C,0x00,0x00,0x00,0x03]
mezzazine_enable = [0x01,0xAA,0xBB,0x0C,0x00,0x07,0x00,0x03]
open_all = [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x00,0x00,0x00,0x00,0x03]
close_all = [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x0f,0x00,0x0f,0x00,0x03]
read_status = [0x01,0xAA,0xBB,0x0C,0x00,0x10,0x81,0x00,0x03]

#relay closing commands
k1_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x10,0x81,0x00,0x00,0x00,0x03]
k2_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x00,0x00,0x10,0x81,0x00,0x03]
k3_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x02,0x00,0x02,0x00,0x03]
k4_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x04,0x00,0x00,0x00,0x03]
k5_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x00,0x00,0x04,0x00,0x03]
k6_close =  [0x01,0xAA,0xBB,0x0C,0x00,0x02,0x00,0x08,0x00,0x08,0x00,0x03]

#good relay response
closed_value =  "01aa0007000000f6ff030100bb07000000f6ff0301aa000b0000000000030100bb0b00000000000301aa000b0002000000030100bb0b00020000000301aa000c0000000000030100bb0c00000000000301aa000c0007000000030100bb0c00070000000301aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c001081000000003f030100bb0c001081000000003f03"
opened_value = "01aa000c0002000000030100bb0c00020000000301aa000c0010810000000000030100bb0c001081000000000003"
k1_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c001081000000001081030100bb0c00108100000000108103"
k2_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c0010810000000002030100bb0c001081000000000203"
k3_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c0010810000000004030100bb0c001081000000000403"
k4_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c0010810000000008030100bb0c001081000000000803"
k5_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c001081000000001090030100bb0c00108100000000109003"
k6_value = "01aa000c0002000000030100bb0c00020000000301aa000c0002000000030100bb0c00020000000301aa000c0010810000000020030100bb0c001081000000002003"

tablica1=[k1_close,k2_close,k3_close,k4_close,k5_close,k6_close]
tablica2=[k1_value,k2_value,k3_value,k4_value,k5_value,k6_value]


#code for initialization

def initialization():
    serialPort.write(serial.to_bytes(init_start))
    #print("inicjalizacja")
    time.sleep(0.25)
    serialPort.write(serial.to_bytes(voter_start))
    #print("inicjalizacja")
    time.sleep(0.25)
    serialPort.write(serial.to_bytes(relay_start))
    #print("inicjalizacjia")
    time.sleep(0.25)
    serialPort.write(serial.to_bytes(relay_set))
    #print("inicjalizacjia")
    time.sleep(0.25)
    serialPort.write(serial.to_bytes(mezzazine_enable))
    #print("Inicjalizacja OK, przekazniki zamkna sie i otworza")
    #print("------------------------------")
    serialPort.write(serial.to_bytes(open_all))
    time.sleep(0.5)

#close all and read value
    
def multiple_run():
    serialPort.write(serial.to_bytes(open_all))
    #print("przekazniki otwarte")
    time.sleep(0.5)
    serialPort.write(serial.to_bytes(close_all))
    #print("przekazniki zamkniete")
    time.sleep(0.5)
    serialPort.write(serial.to_bytes(read_status))
    time.sleep(0.5)
    k_close_read = serialPort.read(255).hex()
   # print(k_close_read)
   # print('------')
    time.sleep(1)
    if k_close_read == closed_value:
        #print("wszystkie zamkniete prawidlowo")
        label_closed_relays_status.config(bg='green', text = 'ok')
    else:
       # print("uszkodzony ktorys z przekaznikow")
        label_closed_relays_status.config(bg='red', text = 'Nok')
    time.sleep(0.25)
    #print("------------------------------")

    #open all and read value
    serialPort.write(serial.to_bytes(open_all))
    time.sleep(0.25)
    serialPort.write(serial.to_bytes(read_status))
    time.sleep(0.25)
    k_open_read = serialPort.read(255).hex()
    #print(k_open_read)
    if k_open_read == opened_value:
        #print("wszystkie otwarte prawidlowo")
        label_opened_relays_status.config(bg='green', text = 'ok')
    else:
       # print("Uszkodzony któryś z przekaznikow")
        label_opened_relays_status.config(bg='red', text = 'Nok')
    time.sleep(0.5)
    #print("------------------------------")
    
def start():
    global serialPort
    a = v.get()

    serialPort = serial.Serial(port = "COM"+a, baudrate=115200,
                               bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    initialization()
    multiple_run()
    single_run()
#code for initialization

#relays values
    
def single_run():

    for i in range(0,6):
        serialPort.write(serial.to_bytes(open_all))
        time.sleep(0.25)
        serialPort.write(serial.to_bytes(tablica1[i]))
        time.sleep(0.25)
        serialPort.write(serial.to_bytes(read_status))
        k1_close_read = serialPort.read(255).hex()
       # print(tablica1[i])
        #print(k1_close_read)
        if tablica2[i] == k1_close_read:
           # print("przekaznik K", i )
            tablica3[i].config(bg='green', text = 'ok')
        else:
            #print("przekaznik K", i )     
            tablica3[i].config(bg='red', text = 'Nok')
        time.sleep(0.1)
    print("------------------------------")
    serialPort.close()

#window setup

start_label = tk.Label(master = frame, font =("Arial",9), text = "Program do testowania statusu przekazników\n jeśli kwadrat jest zielony - OK,  czerowny - NOK")
start_label.place(x=40,y=0)
 #button
 
Button1 = tk.Button(master = frame, text = "Rozpocznij test przekazników", font = 30, height = 3, width =30, command = start)
Button1.place(x=15, y=45)

#Com_switcher

com_label = tk.Label(master = frame, text = "Wpisz numer portu COM ................... ",height = 2, font=("Arial",10)) 
com_label.place(x=0,y=135)

#com_input

v = tk.StringVar()
com_input = tk.Entry(master  = frame , textvariable=v)
com_input.place(x=240,y=145)

#close all


label_closed_relays = tk.Label(master = frame, text = "Status wszystkich zamknietych przekaznikow.......",height = 2, font=("Arial",10)) 
label_closed_relays.place(x=0,y=170)

label_closed_relays_status = tk.Label(master = frame, bg = "yellow", text = " ", height = 1, width = 2)
label_closed_relays_status.place(x=350,y=175)

#open all

label_opened_relays = tk.Label(master = frame, text = "Status wszystkich otwartych przekaznikow .........",height = 2, font=("Arial",10)) 
label_opened_relays.place(x=0,y=210)

label_opened_relays_status = tk.Label(master = frame, bg = "yellow", text = "", height = 1, width = 2)
label_opened_relays_status.place(x=350,y=215)

#k1 close

label_closed_k1 = tk.Label(master = frame, text = "Status zamkniecia K1 ...............",height = 2, font=("Arial",10))
label_closed_k1.place(x=0,y=250)

label_closed_k1_status = tk.Label(master = frame, bg = "yellow", text = " ", height = 1, width = 2)
label_closed_k1_status.place(x=250,y=255)

#k2 close

label_closed_k2 = tk.Label(master = frame, text = "Status zamkniecia K2 ...............",height = 2, font=("Arial",10))
label_closed_k2.place(x=0,y=290)

label_closed_k2_status = tk.Label(master = frame, bg = "yellow" , text = " ", height = 1, width = 2)
label_closed_k2_status.place(x=250,y=295)

#k3 close

label_closed_k3 = tk.Label(master = frame, text = "Status zamkniecia K3 ...............",height = 2, font=("Arial",10))
label_closed_k3.place(x=0,y=330)

label_closed_k3_status = tk.Label(master = frame, bg = "yellow" , text = " ", height = 1, width = 2)
label_closed_k3_status.place(x=250,y=335)

#k4_close

label_closed_k4 = tk.Label(master = frame, text = "Status zamkniecia K4 ...............",height = 2, font=("Arial",10))
label_closed_k4.place(x=0,y=370)

label_closed_k4_status = tk.Label(master = frame, bg = "yellow" , text = " ", height = 1, width = 2)
label_closed_k4_status.place(x=250,y=375)

#k5_close

label_closed_k5 = tk.Label(master = frame, text = "Status zamkniecia K5 ...............",height = 2, font=("Arial",10))
label_closed_k5.place(x=0,y=410)

label_closed_k5_status = tk.Label(master = frame, bg = "yellow" , text = " ", height = 1, width = 2)
label_closed_k5_status.place(x=250,y=415)

#k6_clsoe

label_closed_k6 = tk.Label(master = frame, text = "Status zamkniecia K6 ...............",height = 2, font=("Arial",10))
label_closed_k6.place(x=0,y=450)

label_closed_k6_status = tk.Label(master = frame, bg = "yellow" , text = " ", height = 1, width = 2)
label_closed_k6_status.place(x=250,y=455)

tablica3=[label_closed_k1_status, label_closed_k2_status, label_closed_k3_status, label_closed_k4_status, label_closed_k5_status, label_closed_k6_status]

window.mainloop()



