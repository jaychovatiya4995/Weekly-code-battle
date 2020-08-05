import tkinter as tk
from tkinter import ttk
import os 
win = tk.Tk()
win.title('CURRENCYCONVERTER')

rs = ttk.Label(win,text='Amount INR')
rs.grid(row=2,column=0) 
rsvar = tk.IntVar()
rstxt = ttk.Entry(win,width=16,textvariable=rsvar)
rstxt.grid(row=3,column=0)
cov = ttk.Label(win,text='Covert')
cov.grid(row=4,column=0)
covvar= tk.IntVar()
covtxt= ttk.Entry(win,width=16,textvariable=covvar)
covtxt.grid(row=5,column=0)

def us():
    amount = int(rstxt.get())
    # print(amount)
    dollar = amount/70 
    # print(f'Amount in DOLLAR is {dollar}')
    covvar.set(dollar)
def pou():
    amount = int(rstxt.get())
    poun= amount/98
    covvar.set(poun)
def eu():
    amount = int(rstxt.get())
    eur = amount/88
    covvar.set(eur)
def swiss():
    amount = int(rstxt.get())
    swis = amount/82
    covvar.set(swis)
def y():
    amount = int(rstxt.get())
    ye = amount*1.29 
    covvar.set(ye)

    

usdollar = tk.Button(win,text='    US-DOLLAR  ',command=us)
usdollar.grid(row=7,column=0,sticky='W') 
euro = tk.Button(win,text='EURO',command=eu)
euro.grid(row=6,column=1)
pound = tk.Button(win,text='POUND',command=pou)
pound.grid(row=6,column=0)
swissfrance = tk.Button(win,text='SWISS-FRANCE',command=swiss)
swissfrance.grid(row=7,column=1,sticky='W')
yen = tk.Button(win,text='  YEN  ',command=y)
yen.grid(row=8,column=0,sticky='E')



win.mainloop()
