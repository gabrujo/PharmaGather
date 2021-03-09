import urllib.request
import urllib


pdict={"pinnumber": 1,"pinstate": 0,"firstname" : "gabriel","lastname":"arejo", "address":"156 hill road","dob":"01/01/2000","phone":"203-56703452","password":"hiash","secretcode":"123445"}


def Send_sms(pdict, pnum):
    phone_num = pdict.get("phone")

    params = {
        'username': 'fati8663',
        'password': 'Cd9lXRQ2',
        'to': phone_num,
        'from': 'D7SMS',
        'content': 'Your prescription is ready for pick up, please use this prescription number' + str(pnum) +
                   ' in the Pharmagather machine',
    }
    urllib.request.urlopen("http://smsc.d7networks.com:1401/send?%s" % urllib.parse.urlencode(params)).read()


Send_sms(pdict, 12345)

import sqlite3

conn = sqlite3.connect('pharmacy.db')
c = conn.cursor()


def is_pin_free():
    query = "select * from pharma where pinstate=0"
    c.execute(query)
    result = c.fetchone()
    #print(result)
    if result is None:
        return -1
    else:
        return result[0]


def get_free_pin():
    if is_pin_free() != -1:
        return is_pin_free()

def updat_pin_data(pdict, pNum):

    query = '''update pharma set pinstate=? , firstname= ? ,lastname=? , address=  ? , dob= ?,phone= ?, password= ?, secretcode= ? where pinnumber=?'''

    c.execute(query,(1,pdict.get("firstname"),pdict.get("lastname"),pdict.get("address"),pdict.get("dob"),pdict.get("phone"),pdict.get("password"),pdict.get("secretcode"),pNum))
    conn.commit()

    return 1

get_free_pin()

updat_pin_data(pdict,get_free_pin())




