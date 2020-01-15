
from tkinter import *
from tkinter.ttk import Combobox

class MyWindow:
    def __init__(self, win):
        # Title
        self.ttle = Label(win, text = 'X-Calibrator')
        self.ttle.place(x = 350, y = 0)
        # Date
        self.date = Label(win, text = 'Date')
        self.date.place(x = 700, y = 0)
        # Time
        self.time = Label(win, text = 'Time')
        self.time.place(x = 700, y = 25)
        # 
        self.lbl1=Label(win, text='First number')
        self.lbl1.place(x=100, y=50)

        self.lbl2=Label(win, text='Second number')
        self.lbl2.place(x=100, y=100)


        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        
        self.t1.place(x=200, y=50)
        
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))



window=Tk()
mywin=MyWindow(window)


window.title('ECE 491 GUI')
window.geometry("800x480+10+10")
window.mainloop()