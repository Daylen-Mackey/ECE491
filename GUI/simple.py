from tkinter import *
from tkinter.ttk import Combobox
import tkSimpleDialog as simpledialog

class MyWindow:
    def __init__(self, win):
        # Frame.__init__(self)
        self.edited = False
        
        # Title
        self.ttle = Label(win, text = 'X-Calibrator')
        self.ttle.place(x = 350, y = 0)
        # Date
        self.date = Label(win, text = 'Date')
        self.date.place(x = 700, y = 0)

        self.meas = Label(win, text = 'Meas Range:')
        self.intTime = Label(win, text = 'Int Time (ms):')
        self.meas.place(x = 10, y = 42)
        self.intTime.place(x = 10, y = 72)

        self.entry_1_var = StringVar()
        self.entry_2_var = StringVar()
        
        self.measIn = Entry(bd=3, width = 10,textvariable=self.entry_1_var)
        self.measIn.place(x = 150, y = 40)
        self.intTimeText = StringVar()
        self.intTimeIn = Entry(bd=3, width = 10,textvariable=self.entry_2_var)
        self.intTimeIn.place(x = 150, y =70)
        self.measIn.bind('<FocusIn>',lambda e: self.set_active_entry('entry_1_var'))
        self.intTimeIn.bind('<FocusIn>',lambda f: self.set_active_entry('entry_2_var'))
        self.intTimeIn.bind('<FocusOut>',self.numpadExit)
        self.measIn.bind('<FocusOut>',self.numpadExit)
    def numpadEntry(self):
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
    
    def set_active_entry(self, name): 
        self._active_entry = name
        print(self._active_entry)
        numPad(self,self)
    
    @property
    def active_entry(self):
        return getattr(self, self._active_entry)

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
            cur = Button(self.top, text=label, width=8, height=3, command=cmd)
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
            currentText = self.parent.active_entry.get()
            self.parent.active_entry.set(currentText[:-1])
        elif label == 'Close':
            self.ok()
        else:
            currentText = self.parent.active_entry.get()
            self.parent.active_entry.set(currentText+label)
    def ok(self):
        self.top.destroy()
        self.top.master.focus()

        

window=Tk()
mywin=MyWindow(window)


window.title('ECE 491 GUI')
window.geometry("800x480+10+10")
window.mainloop()