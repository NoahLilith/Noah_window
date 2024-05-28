import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry('300x200')
        
        ttk.Button(self,text="TOP").pack()
        
        ttk.Button(self,text="MIDDLE").pack()
        
        ttk.Button(self,text="BOTTOM").pack()
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()