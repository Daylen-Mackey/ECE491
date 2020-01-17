
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
        # serial port with dropdown list 
        self.portLbl = Label(win,text = 'Port:')
        self.portLbl.place(x = 10,y = 10)
        self.port = Combobox(win, width = 10, 
                            values=[
                                    "Com 5", 
                                    "Com 6",
                                    "Com 6"])
        self.port.place(x = 50, y = 10)

        self.meas = Label(win, text = 'Meas Range:')
        self.intTime = Label(win, text = 'Int Time (ms):')
        self.samples = Label(win, text = '# of Samples:')
        self.totTime = Label(win, text = 'Total Time (ms):')
        self.bias = Label(win, text = 'Bias Voltage (V):')

        self.meas.place(x = 10, y = 42)
        self.intTime.place(x = 10, y = 72)
        self.samples.place(x = 10, y = 102)
        self.totTime.place(x = 10, y = 132)
        self.bias.place(x = 10, y = 162)

        self.measIn = Entry(bd=3, width = 10)
        self.measIn.place(x = 150, y = 40)

        self.intTimeIn = Entry(bd=3, width = 10)
        self.intTimeIn.place(x = 150, y =70)

        self.samplesIn = Entry(bd=3, width = 10)
        self.samplesIn.place(x = 150, y = 100)
        
        self.totTimeIn = Entry(bd=3, width = 10)
        self.totTimeIn.place(x = 150, y =130)

        self.biasIn = Entry(bd=3, width = 10)
        self.biasIn.place(x = 150, y = 160)

        # Defining and Placing Buttons:

        self.measB = Button(win, text = 'Set')
        self.intTimeB = Button(win, text = 'Set')
        self.samplesB = Button(win, text = 'Set')
        self.biasB = Button(win, text = 'Set')

        self.measB.place(x=260, y=45)
        self.intTimeB.place(x=260, y=75)
        self.samplesB.place(x=260, y = 105)
        self.biasB.place(x=260, y=165)

        self.getAll = Button(win, text = 'Get All')
        self.setAll = Button(win, text = 'Set All')
        self.zero = Button(win, text = 'Zero')

        self.getAll.place(x = 130, y = 200)
        self.setAll.place(x = 192, y = 200)
        self.zero.place(x = 253, y = 200)

        var = IntVar()
        R1 = Radiobutton(win, text="Channel 1", variable=var, value=1)
        R1.pack( anchor = W )
        R2 = Radiobutton(win, text="Channel 2", variable=var, value=2)
        R2.pack( anchor = W )
        R1.place(x = 10, y = 195)
        R2.place(x = 10, y = 215)

        # v = StringVar(win, "1") 


        # values = {"RadioButton 1" : "1", 
        #   "RadioButton 2" : "2" }
        # for (text, value) in values.items(): 
        #     Radiobutton(win, text = text, variable = v,  
        #         value = value, indicator = 0, 
        #         background = "light blue").pack(fill = X, ipady = 5) 





        self.lbl1=Label(win, text='First number')
        self.lbl1.place(x=400, y=50)

        self.lbl2=Label(win, text='Second number')
        self.lbl2.place(x=400, y=100)


        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        # self.btn1 = Button(win, text='Add')
        # self.btn2=Button(win, text='Subtract')
        
        self.t1.place(x=500, y=50)
        
        self.t2.place(x=500, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=450, y=150)
        self.b2.place(x=500, y=150)
        self.lbl3.place(x=400, y=200)
        self.t3.place(x=500, y=200)
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