import tkinter as tk
from tkinter import ttk

def get_names() -> list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:str = file.read()
    names:list[str] = content.split()
    return names

class Window(tk.Tk):
    def __init__(self, title:str = "Hellp! Tkinter!", **kwargs):
        super().__init__(**kwargs)
        #多做一些事
        self.title(title)
        self.geometry('500x300')
        self.resizable(1,1)
        label:ttk.Label = ttk.Label(self, 
                                    text = "Hello! World!",
                                    font = ('Arial',20,'bold'),
                                    foreground = '#f00')
        label.pack(padx=100,pady=40)

        
if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window(title = "FIRST GUI")
    #window.title("FIRST GUI")
    CT = tk.Button(text="計數器")
    CT.pack(padx=100,pady=80)
    window.mainloop()
