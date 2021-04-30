    import tkinter as tkn
import numpy as np
import matplotlib.pyplot as plt
b = tkn.Tk()
b.geometry('500x300')
b.title('Calculate karega kuch')

y = tkn.StringVar()
t1 = tkn.StringVar()
t2 = tkn.StringVar()
rangeL = tkn.StringVar()
rangeU = tkn.StringVar()
steps = tkn.StringVar()
from PIL import ImageTk, Image

def suma():
    a = 0
    a = (float(t1.get())+float(t2.get()))
    tkn.messagebox.showinfo("Sum", a)
def diff():
    a = 0
    a = (float(t1.get())-float(t2.get()))
    tkn.messagebox.showinfo("Difference", a)
def multi():
    a = 0
    a = (float(t1.get())*float(t2.get()))
    tkn.messagebox.showinfo("Product", a)
def div():
    try:
        a = 0
        a = (float(t1.get())/float(t2.get()))
        tkn.messagebox.showinfo("Quotient", a)
    except :
        print("Sorry! Dividing by Zero")
def powa():
    a = 0
    a = (float(t1.get())**float(t2.get()))
    tkn.messagebox.showinfo("Power", a)

tkn.Label(b, text = 'First number: ').grid(row=1,column=1)
tkn.Entry(b, textvariable = t1).grid(row = 1,column = 2)
tkn.Label(b, text = 'Second number: ').grid(row=2,column=1)
tkn.Entry(b, textvariable = t2).grid(row = 2,column = 2)
tkn.Label(b, text = 'Function f(x): ').grid(row=3,column=1)
tkn.Entry(b, textvariable = y).grid(row = 3,column = 2)
tkn.Label(b, text = 'Lower Limit: ').grid(row=4, column = 1)
tkn.Entry(b, textvariable = rangeL).grid(row = 4, column = 2)
tkn.Label(b, text = 'Upper Limit: ').grid(row=5, column = 1)
tkn.Entry(b, textvariable = rangeU).grid(row = 5, column = 2)
tkn.Label(b, text = 'Steps: ').grid(row=6, column = 1)
tkn.Entry(b, textvariable = steps).grid(row = 6, column = 2)

tkn.Button(b, text = "+", command = suma ).grid(row = 7, column = 1)
tkn.Button(b, text = "-", command = diff ).grid(row = 7, column = 2)
tkn.Button(b, text = "*", command = multi).grid(row = 8, column = 1)
tkn.Button(b, text = "/", command = div  ).grid(row = 8, column = 2)
tkn.Button(b, text = "^", command = powa  ).grid(row = 9, column = 1, columnspan=2)

def plot():
    plt.savefig('balle.png')
    path = "C:/Users/vandi/OneDrive/Documents/Python Scripts/balle.png"
    x = np.arange(eval(rangeL.get()),eval(rangeU.get()),eval(steps.get()))
    yy = eval(y.get())
    plt.plot(x,yy)
    plt.show()
    img = ImageTk.PhotoImage(Image.open(path))
    tkn.messagebox.show("graph",img)
    
tkn.Button(b, text = "plot", command = plot ).grid(row = 6, column = 3)
'''
    path = "C:/Users/vandi/OneDrive/Documents/Python Scripts/balle.png"
    plt.savefig('balle.png')
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tkn.Label(b, image = img)
    tkn.messagebox.showinfo("Sum", img)
'''
b.mainloop()    
