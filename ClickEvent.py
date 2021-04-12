from tkinter import *
window=Tk()
txt=Entry(window, width=20)
txt.grid(row=0, column=3)
l1=Label(window, text="Smart Programmer", font=15)
l1.grid(row=6, columns=1)
def click():
    res="Welcome to " + txt.get()
    l1.configure(text=res)

Btn=Button(window,text="Enter",fg="yellow",bg="blue",command=click)
Btn.grid(row=5,column=2)
window.mainloop()