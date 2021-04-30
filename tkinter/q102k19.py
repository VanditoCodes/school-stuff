import tkinter as tkn
from tkinter import messagebox

root = tkn.Tk()
root.title("SI Calculator")
P = tkn.StringVar()
R = tkn.StringVar()
T = tkn.StringVar()
tkn.Label(root, text="Principal Amount: ").grid(column=0, row=0)
tkn.Entry(root, width=20, textvariable=P).grid(column=2, row=0)
tkn.Label(root, text="Rate: ").grid(column=0, row=1)
tkn.Entry(root, width=20, textvariable=R).grid(column=2, row=1)
tkn.Label(root, text="Time Period: ").grid(column=0, row=2)
tkn.Entry(root, width=20, textvariable=T).grid(column=2, row=2)

def fn():
    p = int(P.get())
    r = int(R.get())
    t = int(T.get())
    si = (p*r*t)/100
    messagebox.showinfo("Simple Interest", "Interest: "+str(si))
tkn.Button(root, text="Calculate Interest", command=fn).grid(column=0, row=4)
tkn.Button(root, text="Exit", command=root.destroy).grid(column=2, row=4)

root.mainloop()