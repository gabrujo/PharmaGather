from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from functools import partial


def press(num):
    global operator
    operator = operator+str(num)
    pres_code.set(operator)


def btnClear():
    global operator
    operator = ""
    pres_code.set("")


def login():
    print(pres_code.get())
    prescode_info= str(pres_code.get())

    # prescode_info += pres_code.get()
    
    prescode_entry.delete(0, END)

    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    find_user = ('select * from pharma where secretcode=?')
    c.execute(find_user, (prescode_info,))
    result = c.fetchall()
    if result:
        Label(screen, text="login Success",
              fg="green", font=("Calibri", 12)).pack()
        # login_success()
    else:
        Label(screen, text="login failed",
              fg="green", font=("Calibri", 12)).pack()
        # login_failed



global prescode_entry
global pres_code

global screen
screen = Tk()
screen.title("PharmaGather")
screen.geometry("500x500")
operator = ""
pres_code = StringVar()
canvas= tk.Canvas(screen)
canvas.pack(side = TOP, fill=BOTH, expand = True)
prescode_entry = Entry(
    canvas, textvariable=pres_code, justify='center', bd=5, bg="green", font=("Calibri", 40))
prescode_entry.pack(side=TOP, expand=NO, pady = 10)
keyboard_frame = tk.Frame(screen)


status_lbl = StringVar()
Label(screen, textvariable=status_lbl).pack()
status_lbl.set("Plese enter your secret code.")
button1 = Button(keyboard_frame, text=' 1 ', fg='black', bg="pink",
                 command=lambda: press(1), height=3, width=10)
button1.grid(row=0, column=0)

button2 = Button(keyboard_frame, text=' 2 ', fg='black', bg="pink",
                 command=lambda: press(2), height=3, width=10)
button2.grid(row=0, column=1)

button3 = Button(keyboard_frame, text=' 3 ', fg='black', bg="pink",
                 command=lambda: press(3), height=3, width=10)
button3.grid(row=0, column=2)

button4 = Button(keyboard_frame, text=' 4 ', fg='black', bg="pink",
                 command=lambda: press(4), height=3, width=10)
button4.grid(row=1, column=0)

button5 = Button(keyboard_frame, text=' 5 ', fg='black', bg="pink",
                 command=lambda: press(5), height=3, width=10)
button5.grid(row=1, column=1)

button6 = Button(keyboard_frame, text=' 6 ', fg='black', bg="pink",
                 command=lambda: press(6), height=3, width=10)
button6.grid(row=1, column=2)

button7 = Button(keyboard_frame, text=' 7 ', fg='black', bg="pink",
                 command=lambda: press(7), height=3, width=10)
button7.grid(row=2, column=0)
button8 = Button(keyboard_frame, text=' 8 ', fg='black', bg="pink",
                 command=lambda: press(8), height=3, width=10)
button8.grid(row=2, column=1)

button9 = Button(keyboard_frame, text=' 9 ', fg='black', bg="pink",
                 command=lambda: press(9), height=3, width=10)
button9.grid(row=2, column=2)

button0 = Button(keyboard_frame, text=' 0 ', fg='black', bg="pink",
                 command=lambda: press(0), height=3, width=10)
button0.grid(row=3, column=0)
clear = Button(keyboard_frame, text='Clear', fg='black', bg="pink",
               command=btnClear, height=3,width= 10)
clear.grid(row=3, column=1)

log=Button( keyboard_frame,text="login", height=3, width=10,
       bg="pink", command=login)
log.grid(row=3, column=2)

keyboard_frame.pack(pady=10)
screen.mainloop()


if __name__ == '__main__':

    login()
