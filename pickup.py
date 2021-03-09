from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from functools import partial
import tkinter.messagebox

def closeAllHooks():
    #close all the hooks
    print("All hooks locked")
    return

def openHook(hookNumber):
    #open the hook
    print("Hook number " + str(hookNumber) + " OPEN")
    return

def press(num):
    global operator
    operator = operator+str(num)
    pres_code.set(operator)


def btnClear():
    global operator
    operator = ""
    pres_code.set("")

import random
def generatePassword():
    #return a random number
    global password
    password = str(random.randrange(1000, 9999))
    print(password)
    return
    
from twilio.rest import Client
def sendPassword(current_prescription):
    #send password to the customer
    name = current_prescription[1]
    content = "Hi " + name + " Your Password is: "
    content += str(password)
    phone = "+1" + str(current_prescription[3])
    print(phone, content)
    account_sid = 'AC7643e4456c35f6d62bd43e4feed9072a'
    auth_token = 'e2d838477d73fbebc9245f06754b459f'
    client = Client(account_sid, auth_token)

    client.messages.create(body=content, to=phone, from_ = '+14089158491')
    return

import sqlite3
conn = sqlite3.connect('pharmagather.db')
c = conn.cursor()
def getPSData(pid):
    #return the user   
    query = "select * from hooks where free = 0 and code=" + str(pid)
    c.execute(query)
    result = c.fetchone()
    if result is None:
        return -1
    print(result)
    return result

def updateDB(hookNumber):
    # change status of hook to free
    query = '''update hooks set free=? where hook=?'''
    c.execute(query,(1, hookNumber))
    conn.commit()
    return

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred, {'projectId': "pharma-gather",})
db = firestore.client()

def updateFB(barcode):
    #update status of prescription to loaded
    doc_ref = db.collection(u'Prescription').document(barcode)
    doc_ref.update({"Status" : "pickedUp"})
    return

import time
loginStep = 1
current_prescription = None
password = 0
attempts = 0
def login():
    global current_prescription
    global attempts
    loginCode = pres_code.get()
    global loginStep
    global password
    if loginStep == 1:
        #step 1 of login
        
        if loginCode == "777a":
            #screen lock code
            print("lock the screen")
            while True:
                if input("Enter x to exit")=="xx":
                    break
        else:
            #normal login
            result = getPSData(loginCode)
            print(result)
            if result == -1:
                #no such prescription code
                btnClear()
                tkinter.messagebox.showinfo("Wrong Code", "Please Try again!")
            else:
                #go to second step recognition
                current_prescription = result
                generatePassword()
                #sendPassword(current_prescription)
                btnClear()
                status_lbl.set("Hi " + result[1] + ", Enter your password")
                loginStep = 2
                attempts = 0
    else:
        #step 2 of login
        print(loginCode, password)
        if loginCode == password:

            #correct password
            hookNumber = current_prescription[0]
            updateDB(hookNumber)
            psID = current_prescription[2]
            updateFB(psID)
            openHook(hookNumber)
            time.sleep(1)
            closeAllHooks()
            btnClear()
            status_lbl.set("Please enter your secret code!")
            tkinter.messagebox.showinfo("Successfull Pickup", "Thank you!")
            loginStep = 1
        else:
            #wrong password
            if attempts == 3:
                loginStep = 1
                btnClear()
                status_lbl.set("Please enter your secret code!")
            else:
                attempts +=1
                btnClear()
                tkinter.messagebox.showinfo("Wrong Password" + str(attempts), "Please Try again!")
        return
        


global prescode_entry
global status_entry
global pres_code
global status_lbl
global screen
screen = Tk()
screen.title("PharmaGather")
screen.geometry("500x500")
operator = ""

pres_code = StringVar()
status_lbl = StringVar()
canvas= tk.Canvas(screen)
canvas.pack(side = TOP, fill=BOTH, expand = True)
prescode_entry = Entry(canvas, textvariable=pres_code,justify='center',
    state = "readonly", bd=5, bg="green", font=("Calibri", 40))
prescode_entry.pack(side=TOP, expand=NO, pady = 10)
status_entry = Entry(canvas, textvariable=status_lbl, justify='center',
    state="readonly", width ="30", bd=0, font=("Calibri", 20))
status_entry.pack()
keyboard_frame = tk.Frame(screen)



#statusLabel = Label(screen, textvariable=status_lbl, font=("Courier", 20))
#statusLabel.pack()
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

log=Button( keyboard_frame,text="Enter", height=3, width=10,
       bg="pink", command=login)
log.grid(row=3, column=2)

keyboard_frame.pack(pady=10)
screen.mainloop()



