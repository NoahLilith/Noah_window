def plus1():

    global num

    num+=1

    yrlabeltxt.set(str(num));

import tkinter as tk


yrwin=tk.Tk()

yrlabeltxt=tk.StringVar()

yrbtntxt=tk.StringVar()

yrbtntxt2=tk.StringVar()

num = 0

 

mylabel= tk.Label(yrwin,textvariable=yrlabeltxt)

yrlabeltxt.set("0")

mylabel.pack()

 

mybtn=tk.Button(yrwin,textvariable=yrbtntxt,command=plus1)

yrbtntxt.set("+1")

mybtn.pack()


 

yrwin.mainloop()