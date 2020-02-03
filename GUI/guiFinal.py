import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import tkSimpleDialog as simpledialog
from PIL import ImageTk, Image


class MyWindow:
    def __init__(self, win):
        # window.attributes('-alpha', 0.9)


        # background_label = Label(win, image=back_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Frame.__init__(self)
        self.edited = False

        # self.entry_2 = Entry(self, width=10, font='Helvetica 32', textvariable=self.entry_2_var)
        # self.create_widgets(self,win)
        # self.entry_binding(self,win)
        # background_image=tk.PhotoImage('Decay.png')
        # background_label = Label(win, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.labelling(win)
        self.entries(win)
        self.buttons(win)
        self.placing(win)
        

    def labelling(self,win):
        self.ttle = Label(win, text = 'X-Calibrator')

        self.meas = Label(win, text = 'Meas Range:')
        self.intTime = Label(win, text = 'Int Time (ms):')
        self.samples = Label(win, text = '# of Samples:')
        self.totTime = Label(win, text = 'Total Time (ms):')
        self.bias = Label(win, text = 'Bias Voltage (V):')

        # LEFT SIDE 
        self.temp = Label(win, text = 'Temperature:')
        self.pressure = Label(win, text = 'Pressure:')
        self.correction = Label(win, text = 'T/P Correction:')

        self.averages = Label(win,bd=0, highlightthickness=0, text = '# of Averages:')
        self.measTime = Label(win, text = 'Meas Time (s):')
        self.intervalTime = Label(win, text = 'Interval Time (min):')

        # Results
        self.pC_Label = Label(win, text = 'Charge Results (pC):',font='Helvetica 20')
        self.pA_Label = Label(win, text = 'Current Results (pA):',font='Helvetica 20')




    def entries(self,win):
        self.measIn = Entry(bd=3, width = 10)
        self.intTimeIn = Entry(bd=3, width = 10,textvariable=None)
        self.samplesIn = Entry(bd=3, width = 10,textvariable=None)
        self.totTimeIn = Entry(bd=3, width = 10)
        self.biasIn = Entry(bd=3, width = 10)

        # Left Side
        self.tempIn = Entry(bd=3, width = 10)
        self.pressureIn = Entry(bd=3, width = 10)
        self.correctionIn = Entry(bd=3, width = 10)
        
        self.averagesIn = Entry(bd=3, width = 10)
        self.measTimeIn = Entry(bd=3, width = 10)
        self.intervalTimeIn = Entry(bd=3, width = 10)
        
        # Results
        self.pC = Entry(bd=5, width = 10)
        self.pA = Entry(bd=5, width = 10)
        
    def buttons(self,win):
        self.getAll = Button(win, text = 'Get All')
        self.setAll = Button(win, text = 'Set All')
        self.zero = Button(win, text = 'Zero')
        # START/STOP Button Pl
        self.startButton = Button(win, text = 'Start/Stop Measurements')

        # Radio Buttons
        channel = IntVar()
        self.V1 = Radiobutton(win, text="Channel 1", variable=channel, value=1)
        self.V1.pack( anchor = W )
        self.V2 = Radiobutton(win, text="Channel 2", variable=channel, value=2)
        self.V2.pack( anchor = W )

        tempUnit = IntVar()
        self.celsius = Radiobutton(win, text="C", variable=tempUnit, value=1)
        self.farenheit =  Radiobutton(win, text="F", variable=tempUnit, value=2)
        
        pressureUnit = IntVar()
        self.Hg = Radiobutton(win, text="Hg", variable=pressureUnit, value=1)
        self.mBar =  Radiobutton(win, text="mBar", variable=pressureUnit, value=2)
        
    def placing(self,win):
        self.ttle.place(x = 350, y = 0)
        # Placing Labels
        y = 42
        dispY = 30
        dispX = 25
        self.meas.place(x = 10 + dispX, y = y)
        self.intTime.place(x = 10 + dispX, y = y + dispY)
        self.samples.place(x = 10 + dispX, y = y + dispY*2)
        self.totTime.place(x = 10 + dispX, y = y + dispY*3)
        self.bias.place(x = 10 + dispX, y = y + dispY*4)
        # Placing Entries
        y_ent = 40
        self.measIn.place(x = 150 + dispX, y = y_ent)
        self.intTimeIn.place(x = 150 + dispX, y = y_ent + dispY)
        self.samplesIn.place(x = 150 + dispX, y = y_ent + dispY*2)
        self.totTimeIn.place(x = 150 + dispX, y = y_ent + dispY*3)
        self.biasIn.place(x = 150 + dispX, y = y_ent + dispY*4)
        # Placing Buttons
        self.getAll.place(x = 130 + dispX, y = 200)
        self.setAll.place(x = 192 + dispX, y = 200)
        self.zero.place(x = 253 + dispX, y = 200)

        self.startButton.place(x = 100, y = 270,height = 30, width = 550)

       
        # Placing Radio Buttons 
        self.V1.place(x = 10 + dispX, y = 195)
        self.V2.place(x = 10 + dispX, y = 215)
        #------LEFT SIDE-----#
        leftX = 400
        # Placing Labels
        self.temp.place(x=leftX, y = y)
        self.pressure.place(x = leftX , y = y + dispY*1)
        self.correction.place(x = leftX , y = y + dispY*2)

        self.averages.place(x=leftX, y = y + dispY*4)
        self.measTime.place(x = leftX , y = y + dispY*5)
        self.intervalTime.place(x = leftX , y = y + dispY*6)

        # Placing Entries
        leftEntryX = 500
        self.tempIn.place(x = leftEntryX + dispX, y = y_ent)
        self.pressureIn.place(x = leftEntryX + dispX, y = y_ent + dispY)
        self.correctionIn.place(x = leftEntryX + dispX, y = y_ent + dispY*2)

        # Shifted Entries
        self.averagesIn.place(x = leftEntryX + dispX, y = y_ent + dispY*4)
        self.measTimeIn.place(x = leftEntryX + dispX, y = y_ent + dispY*5)
        self.intervalTimeIn.place(x = leftEntryX + dispX, y = y_ent + dispY*6)
        # Placing  Buttons

        # Placing Radio Buttons
        leftRadio = 630
        dispRadioX = 45
        self.celsius.place(x = leftRadio, y = y)
        self.farenheit.place(x = leftRadio + dispRadioX, y = y)
        
        self.Hg.place(x = leftRadio, y = y + dispY*1)
        self.mBar.place(x = leftRadio + dispRadioX, y = y + dispY*1)

        # Placing Results
        # self.startButton.place(x = 100, y = 270,height = 30, width = 550)
        dispResultsX = 75
        self.pC_Label.place(x = 75 + dispResultsX, y = 330,)
        self.pC.place(x = 300 + dispResultsX, y = 327,width = 175, )
        self.pA_Label.place(x = 75 + dispResultsX, y = 375,)
        self.pA.place(x = 300 + dispResultsX, y = 372,width = 175, )
        



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


path = '/Users/dmackey/Desktop/ENGGY4S2/ECE491/GUI/Decay.png'




window=Tk()

# -- Background Image Stuff -- #
# img = ImageTk.PhotoImage(Image.open(path))
# panel = tk.Label(window, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")

# window.wm_attributes("-transparent", True)
# window.attributes('-alpha', 0.9)
# w = Canvas(window, width=150, height=40, bd=0, highlightthickness=0, relief='ridge')
# w.pack()
mywin=MyWindow(window)



# Canvas(window, bd=0, highlightthickness=0).pack(pady=100)
window.title('ECE 491 GUI')
window.geometry("800x480+10+10")
window.mainloop()