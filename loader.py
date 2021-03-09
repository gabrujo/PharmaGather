

def closeAllHooks():
    #close all the hooks
    print("All hooks locked")
    return

def openHook(hookNumber):
    #open the hook
    print("Hook number " + str(hookNumber) + " OPEN")
    return

def flashRed():
    #flash red led
    print("Red Light flashes")
    return

def flashGreen():
    #flash green led
    print("Green Light flashes")
    return

import sqlite3
conn = sqlite3.connect('pharmagather.db')
c = conn.cursor()
def getFreeHook():
    #return the first free hook number otherwise -1
    
    query = "select * from hooks where free=1"
    c.execute(query)
    result = c.fetchone()
    if result is None:
        return -1
    return result[0]

def updateDB(currentHook, prescriptionData, secretCode, barcode):
    # update the database using prescription data
    query = '''update hooks set name=? , pid= ? ,phone=? , code=?, free=? where hook=?'''
    name = prescriptionData.get("FirstName")
    phone = prescriptionData.get("Phone")
    c.execute(query,(name, barcode, phone, secretCode, 0, currentHook))
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
    doc_ref.update({"Status" : "loaded"})
    return

def getPrescriptionData(barcode):
    #fetch data from the firebase
    doc_ref = db.collection(u'Prescription').document(barcode)
    try:
        doc = doc_ref.get()
        return doc.to_dict()
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
        return {}
    
from twilio.rest import Client
def sendSMS(prescriptionData, secretCode):
    #send sms to the customer
    name = prescriptionData.get("FirstName")
    content = "Hi " + name + " Your Prescription is ready! "
    content += "Your secret code is: " + str(secretCode)
    phone = "+1" + str(prescriptionData.get("Phone"))
    account_sid = 'AC7643e4456c35f6d62bd43e4feed9072a'
    auth_token = 'e2d838477d73fbebc9245f06754b459f'
    client = Client(account_sid, auth_token)

    client.messages.create(body=content, to=phone, from_ = '+14089158491')
    return

import random
def generateSecretCode(currentHook):
    #return a random number
    res = random.randrange(10000, 99990, 10) + currentHook
    return res


def loader():
    currentHook = -1
    prescriptionData = {}
    secretCode = 0
    barcode = -1
    while True:
        print("waiting for input")
        incode = input()
        print("input code is:", incode)
        
        if incode == "cancel":
            if barcode == -1:
                print("Nothing to cancel!!")
            else:
                print("Canceled !")
                closeAllHooks()
                flashRed()
                barcode = -1
        elif incode == "done":
            if barcode == -1:
                print("Nothing to done!")
            else:
                print("Confirmed")
                closeAllHooks()
                secretCode = generateSecretCode(currentHook)
                updateDB(currentHook, prescriptionData, secretCode, barcode)
                updateFB(barcode)
                sendSMS(prescriptionData, secretCode)
                flashGreen()
                barcode = -1
        else:
            barcode = incode
            currentHook = getFreeHook()
            if currentHook == -1:
                print("All Hooks are taken!")
                flashRed()
                barcode = -1
            else:
                openHook(currentHook)
                prescriptionData = getPrescriptionData(barcode)
                
loader()           
           
