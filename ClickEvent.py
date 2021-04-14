from tkinter import *

window=Tk()
window.geometry("400x400")
txt=Entry(window, width=20)
txt.grid(row=1, column=0)
l1=Label(window, text="Smart Programmer", font=15)
l1.grid(row=0, column=0)
l2=Label(window)
l2.grid(row=3, column=0)
def click():
    res="Welcome to " + txt.get()
    l2.configure(text=res, font=15)

Btn=Button(window,text="Enter",fg="yellow",bg="blue",command=click)
Btn.grid(row=2,column=0)
window.mainloop()