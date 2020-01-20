
from tkinter import *
from tkinter.ttk import Combobox
import tkSimpleDialog as simpledialog

class MyWindow:
    def __init__(self, win):
        # Frame.__init__(self)
        self.edited = False
        self.textEntryVar = StringVar()
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
        self.intTimeIn.bind('<FocusIn>',self.numpadEntry)
        self.intTimeIn.bind('<FocusOut>',self.numpadExit)

        self.samplesIn = Entry(bd=3, width = 10,textvariable=self.textEntryVar)
        self.samplesIn.place(x = 150, y = 100)
        self.samplesIn.bind('<FocusIn>',self.numpadEntry)
        self.samplesIn.bind('<FocusOut>',self.numpadExit)
        
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
    def numpadEntry(self,event):
        if self.edited == False:
            print("You Clicked on me")
            # self.e['bg']= '#ffffcc'
            self.edited = True
            new = numPad(self,self)
        else:
            self.edited = False

    def numpadExit(self,event):
        print('hi')
        # self.e['bg']= '#ffffff'

class numPad(simpledialog.Dialog):
    def __init__(self,master=None,parent=None):
        self.parent = parent
        self.top = Toplevel()
        self.top.protocol("WM_DELETE_WINDOW",self.ok)
        self.createWidgets()
    def createWidgets(self):
        btn_list = ['7',  '8',  '9', '4',  '5',  '6', '1',  '2',  '3', '0',  'Close',  'Del']
        # create and position all buttons with a for-loop
        # r, c used for row, column grid values
        r = 1
        c = 0
        n = 0
        # list(range()) needed for Python3
        btn = []
        for label in btn_list:
            # partial takes care of function and argument
            cmd = lambda x = label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=10, height=5, command=cmd)
            btn.append(cur)
            # position the button
            btn[-1].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c == 3:
                c = 0
                r += 1
    def click(self,label):
        print(label)
        if label == 'Del':
            currentText = self.parent.textEntryVar.get()
            self.parent.textEntryVar.set(currentText[:-1])
        elif label == 'Close':
            self.ok()
        else:
            currentText = self.parent.textEntryVar.get()
            self.parent.textEntryVar.set(currentText+label)
    def ok(self):
        self.top.destroy()
        self.top.master.focus()



     
# ------- EVERYTHING HERE IS FOR REFERENCE -------- #
    #     self.lbl1=Label(win, text='First number')
    #     self.lbl1.place(x=400, y=50)

    #     self.lbl2=Label(win, text='Second number')
    #     self.lbl2.place(x=400, y=100)


    #     self.lbl3=Label(win, text='Result')
    #     self.t1=Entry(bd=3)
    #     self.t2=Entry()
    #     self.t3=Entry()
    #     # self.btn1 = Button(win, text='Add')
    #     # self.btn2=Button(win, text='Subtract')
        
    #     self.t1.place(x=500, y=50)
        
    #     self.t2.place(x=500, y=100)
    #     self.b1=Button(win, text='Add', command=self.add)
    #     self.b2=Button(win, text='Subtract')
    #     self.b2.bind('<Button-1>', self.sub)
    #     self.b1.place(x=450, y=150)
    #     self.b2.place(x=500, y=150)
    #     self.lbl3.place(x=400, y=200)
    #     self.t3.place(x=500, y=200)
    # def add(self):
    #     self.t3.delete(0, 'end')
    #     num1=int(self.t1.get())
    #     num2=int(self.t2.get())
    #     result=num1+num2
    #     self.t3.insert(END, str(result))
    # def sub(self, event):
    #     self.t3.delete(0, 'end')
    #     num1=int(self.t1.get())
    #     num2=int(self.t2.get())
    #     result=num1-num2
    #     self.t3.insert(END, str(result))

#-------EVERYTHING ABOVE IS FOR REFERENCE -------# 



window=Tk()
mywin=MyWindow(window)


window.title('ECE 491 GUI')
window.geometry("800x480+10+10")
window.mainloop()