from tkinter import *

class App(Frame):
    def __init__(self, master=None, Title="Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.title(Title)
        self.grid(sticky = "NEWS")
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.S = StringVar()
        self.E = Entry(self, textvariable = self.S)
        self.E.grid()
        self.M = Entry(self, textvariable = self.S)
        self.M.grid()
        self.L = Label(self)
        self.L.grid(sticky="NEWS")
        self.E.bind('<ButtonRelease>', self.updater)
    def updater(self,ev):
        if(self.E.selection_present()):
            self.L["text"] = self.E.selection_get()   
# class Look(Label):
#     def __init__(self, master=None, Var = None,**kwargs):
#         Label.__init__(self,master,**kwargs)
#         #self.L = Label(self)
#         self.grid(sticky = "NEWS")
#         self.lookup = Var
#         if Var:
#             self.lookup.trace_add("write",touch)
        
# def touch(*a,**p):
    
#     if A.E.select_present():
#         A.L["text"] = A.E.selection_get()   
#     return True

A = App()
A.mainloop()