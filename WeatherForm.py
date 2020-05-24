import Tkinter as tk

class Display_Weather():
    def __init__(self, master):
        self.x = "False"
        stop_button = tk.Button(master, text="Stop").grid(row=0,column=0)
        Label(master, textvarible=w).grid(row=1,column=0)      
master = tk.Tk()
D = Display_Weather(master)
master.mainloop()