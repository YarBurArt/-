#version //1.0.5
from tkinter import *
from mss import mss
import getpass
import datetime
import platform
import random
import math
import cv2
import os


tk = Tk()
tk.geometry("600x250")
tk.title("DUI Python")
tk['bg'] = 'grey'


#обработка ввода значений строки
def click_button():
    global clicks
    global helo
    global rand
    my_file = open("text.txt", "r")
    my_string = my_file.read()
    ni = ent.get()
    uni = entt.get()
    image = cv2.imread(uni)
    clicks += 1
    tk.title("Clicks {}".format(clicks))

    if ni == str('text'):
        ent.delete(0,END)
        ent.insert(0,(my_string))
        my_file.close()

    if ni == str('text hi'):
        mi_file = open("text.txt",'w')
        mi_file.write(helo)
        mi_file.close()
        ent.delete(0, END)
        ent.insert(0, ('done'))

    if ni == str('clear'):
        clen()

    if ni == str('copy'):
        copy_txt()

    if ni == str('print'):
        ent.delete(0, END)
        if clicks % 2 == 0:
            print_file()

    if ni == str('smiley'):
        lof = random.choice(smiley)
        ent.delete(0,END)
        ent.insert(0,(lof))

    if ni == str('user name'):
        ent.delete(0,END)
        byn = platform.node()
        ent.insert(byn)

    if ni == str('exit'):
        ent.delete(0,END)
        exit(0)

    if ni == str('black photo'):
        ent.delete(0, END)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        viewImage(gray_image, "gray_image")

    if ni == str('onum'): #*-*
        ent.delete(0,END)
        nin = [float(i) for i in uni.split()]
        mi = math.ceil(nin)
        ent.insert(mi)

    if ni == str('random num'):
        ent.delete(0,END)
        ent.insert(0, (rand))

    if ni == str('screen'):
        ent.delete(0, END)
        with mss() as sct:
            sct.shot()
        ent.insert(0,('done, saved after exiting'))


    if ni == str('sort'):
        sortik()

    if ni == str('date'):#*-*
        ent.delete(0,END)
        dat = datetime.datetime.today()
        ent.insert(0, (dat))

    if ni == str('num pi'):
        ent.delete(0, END)
        pin = math.pi
        ent.insert(0, (pin, "or 3.14"))

    if ni == str('~num'):
        seath()

    if ni == str('user'):
        ent.delete(0, END)
        enuser = getpass.getuser()
        ent.insert(0, (enuser))

    if ni == str('internet'):
        ent.delete(0, END)
        os.startfile(r'c:/Program Files/Mozilla Firefox/firefox.exe')



#functions
def seath():
    ent.delete(0, END)
    start = -1
    count = 0
    unis = entt.get()
    my_file = open("text.txt", "r")
    my_string = my_file.read()
    while True:
        start = my_string.find(unis, start + 1)
        if start == -1:
            break
        count += 1
    ent.insert(0, ("Количество символа в строке", count))

def clen():
    my_file = open("text.txt", "w")
    my_file.write("I am clean *-*")
    my_file.close()
    ent.delete(0, END)
    ent.insert(0, ('done'))

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sortik():
    un = entt.get()
    ent.delete(0, END)
    la = len(un)
    i = 0
    mas = []
    while (i < la):
        mas.append(un[i])
        i = i + 1
    mas.sort()
    ent.insert(0, ([mas]))

def copy_txt():
    my_file = open("text.txt", "r")
    my_string = my_file.read()
    ent.delete(0, END)
    my_file = open("text.txt", 'w')
    my_file.write(my_string * 2)
    my_file.close()
    ent.delete(0, END)
    ent.insert(0, ('done'))

def print_file():
    nu = ent.get()
    my_file = open("text.txt", "w")
    my_file.write(nu)
    ent.insert(0,('done'))

def clic_file():
    ny = ent.get()
    os.startfile(ny)

#var :

rand = int(random.randint(0, 1000))
smiley = ['U_U',':)','~_~','^o^',':-D','¬_¬','$_$','=_=','Y.Y',';)',';-)']
helo = str("Nice to see you.What's new?")
clicks = 0

#ccs in python
ent = Entry(tk,width=100)
ent.place(relx=.5, rely=.1, anchor="c")
ent.grid(row=0,column=0)
Lbl = Label(tk,background='#808080',text= '-----------------------------------------------------------------------------------------------------------------------')
Lbl.grid(row= 1,column=0)

btn = Button(text='update str',
             background='#222',
             foreground='#ccc',
             padx='20',
             pady='8',
             font='18',
             command = click_button)
btn.grid(row=2,column=0)

Lbln = Label(tk,background='#808080',text= '-----------------------------------------------------------------------------------------------------------------------')
Lbln.grid(row= 3,column=0)
btnn = Button(text='open file',
             background='#222',
             foreground='#ccc',
             padx='20',
             pady='8',
             font='18',
             command = clic_file)
btnn.grid(row=4,column=0)

Lblnb = Label(tk,background='#808080',text= '-----------------------------------------------------------------------------------------------------------------------')
Lblnb.grid(row= 5,column=0)

entt = Entry(tk, width = 100)
entt.place(relx=.5, rely=.1, anchor="c")
entt.grid(row= 6, column = 0)

Lblnbv = Label(tk,background='#808080',text= '-----------------------------------------------------------------------------------------------------------------------')
Lblnbv.grid(row= 7,column=0)

tk.mainloop()