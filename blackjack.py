# BJ 8-deck

# Stand soft 17

from Tkinter import *

root=Tk()
root.title("Blackjack Payout Calculator")

# BJ Payouts

def bj():
    bet=float(betEntry.get())
    payout = bet*1.5
    
    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _21():
    bet=float(betEntry.get())
    payout=bet

    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

# Match the Dealer

def match():
    bet=float(matchEntry.get())
    payout=bet*3.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout) 

def suitmatch():
    bet=float(matchEntry.get())
    payout=bet*14.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def doublematch():
    bet=float(matchEntry.get())
    payout=bet*6.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def doublesuit():
    bet=float(matchEntry.get())
    payout=bet*28.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def matchsuitmatch():
    bet=float(matchEntry.get())
    payout=bet*17.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def insurance():
    amt=float(insuranceEntry.get())

    payout=amt*2.

    insurancePayoutEntry.delete(1,END)
    insurancePayoutEntry.insert(1,payout)

insuranceButton = Button(root, text="Pay Insurnace", command=insurance)
insuranceButton.grid(row=0, column=0, sticky="WE")

bjButton = Button(root, text="BJ", command=bj)
bjButton.grid(row=0, column=1, sticky="WE")

_21Button = Button(root, text="21", command=_21)
_21Button.grid(row=0, column=2, sticky="WE")

matchButton = Button(root, text="Dealer Match", command=match)
matchButton.grid(row=1, column=0, sticky="WE")

suitmatchButton = Button(root, text="Dealer Suited Match", command=suitmatch)
suitmatchButton.grid(row=1, column=1, sticky="WE")

doublematchButton = Button(root, text="Double Dealer Match", command=doublematch)
doublematchButton.grid(row=1, column=2, sticky="WE")

doublesuitButton = Button(root, text="Double Dealer Suited Match", command=doublesuit)
doublesuitButton.grid(row=1, column=3, sticky="WE")

matchsuitmatchButton = Button(root, text="Dealer Match + Dealer Suited Match", command=matchsuitmatch)
matchsuitmatchButton.grid(row=1, column=4, sticky="WE")

# Entries and Labels

betButton = Label(root, text="Enter bet amount($):")
betButton.grid(row=2, column=0)

betEntry = Entry(root)
betEntry.grid(row=2, column=1)
betEntry.insert(0, "")


matchButton = Label(root, text="Enter match bet amount($):")
matchButton.grid(row=4, column=0)

matchEntry = Entry(root)
matchEntry.grid(row=4, column=1)
matchEntry.insert(0, "")


payoutButton = Label(root, text="Amount to be paid on bet($):")
payoutButton.grid(row=3, column=0)

payoutEntry = Entry(root)
payoutEntry.grid(row=3, column=1)
payoutEntry.insert(0, "$0.00")


matchpayoutButton = Label(root, text="Amount to be paid on match($):")
matchpayoutButton.grid(row=5, column=0)

matchPayoutEntry = Entry(root)
matchPayoutEntry.grid(row=5, column=1)
matchPayoutEntry.insert(0, "$0.00")


insuranceButton = Label(root, text="Enter insurance amount($):")
insuranceButton.grid(row=6,column=0)

insuranceEntry = Entry(root)
insuranceEntry.grid(row=6,column=1)
insuranceEntry.insert(0,"")


insurancePayoutButton = Label(root, text="Amount to be paid on insurance($):")
insurancePayoutButton.grid(row=7,column=0)

insurancePayoutEntry = Entry(root)
insurancePayoutEntry.grid(row=7,column=1)
insurancePayoutEntry.insert(0, "$0.00")


extrasButton = Label(root, text="Note bene:")
extrasButton.grid(row=8,column=0)

extrasEntry = Entry(root)
extrasEntry.grid(row=8, column=1, columnspan=4, sticky="WE")
extrasEntry.insert(0, "")

root.mainloop()
    

