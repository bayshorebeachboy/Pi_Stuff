from Tkinter import *

for i in range(1, 4):
    print i

master = Tk()

Label(master, text=i).grid(row=0, column=0)
mainloop()
