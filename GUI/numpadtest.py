from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.set_active_entry('entry_1_var')  # set initial active entry
        self.entry_1_var = StringVar()
        self.entry_2_var = StringVar()
        self.entry_1 = Entry(self, width=10, font='Helvetica 32', textvariable=self.entry_1_var)
        self.entry_2 = Entry(self, width=10, font='Helvetica 32', textvariable=self.entry_2_var)
        self.create_widgets()
        self.entry_binding()

    def set_active_entry(self, name): 
        self._active_entry = name
        print(self._active_entry)

    @property
    def active_entry(self):
        return getattr(self, self._active_entry)

    @active_entry.setter
    def active_entry(self, value):
        setattr(self, self._active_entry, value)

    def create_widgets(self):
        self.entry_1.pack()
        self.entry_2.pack()

        label = '1'
        button_1 = Button(self, text=label, width=10, height=5, command=lambda x=label: self.num_pad(x))
        button_1.pack()

    def entry_binding(self):
        self.entry_1.bind('<FocusIn>', lambda e: self.set_active_entry('entry_1_var'))
        self.entry_2.bind('<FocusIn>', lambda e: self.set_active_entry('entry_2_var'))

    def num_pad(self, label):
        current_text = self.active_entry.get()
        self.active_entry.set(current_text+label)

app = App()
app.mainloop()