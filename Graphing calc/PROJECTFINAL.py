import tkinter as tkn
import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt
#To import tkinter, numpy and pyplot

'''
Input ‘%matplotlib qt5’ in the console (if using spyder)
Type %matplotlib qt5 directly into the code for jupyter
'''
b = tkn.Tk()
b.title('Graphing Calculator')

num1 = tkn.StringVar()			
#First number
num2 = tkn.StringVar()			
#Second number

y = tkn.StringVar()				
#String to store function in terms of x
rangeL = tkn.StringVar()			
#Lower limit of domain
rangeU = tkn.StringVar()			
#Upper limit of domain
steps = tkn.StringVar()			
#Intervals before a new step is created

def suma():					
    a = 0
    a = (float(num1.get())+float(num2.get()))
    tkn.messagebox.showinfo("Sum", a)
#Function to calculate sum
def diff():					
    a = 0
    a = (float(num1.get())-float(num2.get()))
    tkn.messagebox.showinfo("Difference", a)
#Function to calculate difference
def multi():					
    a = 0
    a = (float(num1.get())*float(num2.get()))
    tkn.messagebox.showinfo("Product", a)
#Function to calculate difference
def div():
    try:
        a = 0
        a = (float(num1.get())/float(num2.get()))
        tkn.messagebox.showinfo("Quotient", a)
    except :
        print("Sorry! Dividing by Zero")
#Function to calculate quotient 
def powa():
    a = 0
    a = (float(num1.get())**float(num2.get()))
    tkn.messagebox.showinfo("Power", a)
#Function to calculate power


#Arithmetic calculator
tkn.Label(b, text = 'Arithmetic calculator').grid(row = 1, column = 1, columnspan = 2)
tkn.Label(b, text = 'First number: ').grid(row=2,column=1)
tkn.Entry(b, textvariable = num1).grid(row = 3,column = 1)
tkn.Label(b, text = 'Second number: ').grid(row=2,column=2)
tkn.Entry(b, textvariable = num2).grid(row = 3,column = 2)
		#Labels and inputs

tkn.Button(b, text = "+", command = suma ).grid(row = 4, column = 1, ipadx = 58)
tkn.Button(b, text = "-", command = diff ).grid(row = 4, column = 2, ipadx = 60)
tkn.Button(b, text = "*", command = multi).grid(row = 5, column = 1, ipadx = 60)
tkn.Button(b, text = "/", command = div  ).grid(row = 5, column = 2, ipadx = 60)
tkn.Button(b, text = "^", command = powa  ).grid(row = 6, column = 1, columnspan=2, ipadx = 140)
		#Buttons

#Graphing Calculator
tkn.Label(b, text = '').grid(row = 7, column = 1, columnspan = 2)
tkn.Label(b, text = 'Graph renderer').grid(row = 8, column = 1, columnspan = 2) 
tkn.Label(b, text = 'Function f(x): ').grid(row=9,column=1)
tkn.Entry(b, textvariable = y).grid(row = 9,column = 2)
tkn.Label(b, text = 'Lower Limit: ').grid(row=10, column = 1)
tkn.Entry(b, textvariable = rangeL).grid(row = 11, column = 1)
tkn.Label(b, text = 'Upper Limit: ').grid(row=10, column = 2)
tkn.Entry(b, textvariable = rangeU).grid(row = 11, column = 2)
tkn.Label(b, text = 'Step: ').grid(row=12, column = 1)
tkn.Entry(b, textvariable = steps).grid(row = 12, column = 2)
		#Labels and inputs

def plot():
    x = np.arange(eval(rangeL.get()), eval(rangeU.get()), eval(steps.get()))
    ''' Defines the domain of the function and thus the range of the graph from rangeL to rangeU with a step after every steps.
        eval() function converts the Tkinter String Variables into a numpy array
    '''
    yy = eval(y.get())
		#yy represents the function to be graphed in the range defined by x
    plt.plot(x,yy)
    plt.show()
    		#To plot the graph
tkn.Button(b, text = "Plot", command = plot ).grid(row = 13, column = 1, columnspan = 2, ipadx = 140)
		#Button to display the graph of the function

b.mainloop()
