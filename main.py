from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import requests
import json


# Main Window

root=Tk()
root.title('Currency Converter')
root.geometry('450x450')
root.configure(bg='#333')
root.resizable(False,False)

#Logo

logo_image=PhotoImage(file="images/icon.png") 
root.iconphoto(False,logo_image)

#Frames

top=Frame(root,height=100, width=500,bg='#147a19')
top.grid(column=0,row=0)

main=Frame(root,height=400,width=500,bg='#333')
main.grid(column=0,row=1)

def convert():
    
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency1=from_box.get()
    currency2 = to_box.get()
    amount = value_entry.get()
    querystring = {"from":currency1,"to":currency2,"amount":amount}

    headers = {
        "x-rapidapi-key": "70d9a7cd1amshae1a9228b861466p1d4e6ajsnb6544e6a9a39",
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if currency2 == 'PKR':
        symbol = 'Rs'
    elif currency2 =='INR':
        symbol = '₹'
    elif currency2 == 'USD':
        symbol ='$'
    elif currency2 == 'BRL':
        symbol='R$'
    elif currency2 =='CAD':
        symbol='CA $'
    elif currency2 == 'GBP':
        symbol='£'
    elif currency2 == 'EUR':
        symbol ='€'

    data=json.loads(response.text)

    convertedamount = data['result']['convertedAmount']
    formatted = symbol +'{:,.2f}'.format(convertedamount)

    result_label.config(text=formatted)
    print(formatted)

# Top Frame

icon= Image.open('images/icon.png')
icon= icon.resize((40 , 40))
icon= ImageTk.PhotoImage(icon)

appname=Label(top, image=icon , compound=LEFT , text='Currency Converter',height=40 ,padx=35 ,pady=30 ,anchor=CENTER ,font='Arial 24 bold', bg='#147a19' ,fg='#fff')
appname.place(x=0,y=0)

# Main Frame
currency = ['PKR','CAD','BRL','GBP','USD','INR','EUR']

from_label = Label (main, text='From:',font='Arial 14 bold',bg='#333',fg='#fff').place(x=80,y=30)
from_box = Combobox(main,font='Arial 15',width='7',justify=CENTER)
from_box['values'] = (currency)
from_box.place(x=80,y=60)

to_label = Label (main, text='To:',font='Arial 14 bold',bg='#333',fg='#fff').place(x=250,y=30)
to_box = Combobox(main,font='Arial 16',width='7',justify=CENTER)
to_box['values'] = (currency)
to_box.place(x=250,y=60)

value_entry = Entry(main, font='Ivy 16', width=23, justify=CENTER, relief=SOLID)
value_entry.place(x=80, y=120)


button = Button(main,text='Convert',bg='#147a19',fg='#fff',width=22,height=2,command=convert).place(x=140,y=180)


result_label = Label(main,text='',height=2 ,width=20,padx=7,pady=7 ,border=4,relief='solid', font='Ivy 16 bold', bg='#fff' ,fg='black')
result_label.place(x=80,y=240)

root.mainloop()