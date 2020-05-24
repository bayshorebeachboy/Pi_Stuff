import  Tkinter as tk
from Tkinter import *

class StartStop():
    def __init__(self, root):
        self.x="False"
        self.ctr=0
        #d = StringVar()
        x_btn = tk.Button(root, text="Stop", background="Snow", width=20)
        x_btn.grid(row=0, column=4, sticky="W", padx=20, pady=5)
        x_btn.bind('<Button-1>', self.stop)
        x_lab = tk.Label(root, textvariable = d)
        x_lab.grid(row=2, column=4)

        self.resume_btn = tk.Button(root, text="Start", background="Snow", width=20)
        self.resume_btn.configure(state="disabled")
        self.resume_btn.grid(row=0, column=6, sticky="W", padx=20, pady=5)
        self.resume_btn.bind('<Button-1>', self.start)


    def xval(self):
        if self.x=="False":
            print "x=false %d=counter value"%self.ctr
            self.ctr += 1
            if self.ctr < 9:
                ## after gives the program time to update
                ## time.sleep() stops everyting
                root.after(1000, self.xval)

    def stop(self, event):
            self.resume_btn.configure(state="normal")
            self.x ="True"
            print "execution stopped:%s"%self.x

    def start(self, event):
            self.x ="False"
            print "execution started:%s"%self.x
            self.ctr=0
            self.xval()
            
    def display():
        p = StringVar()
        for i in range(0, 10000):
            p.set(str(i))
            d = p.get()
            print d
            root.update_idletasks()

def main():
    p = StringVar()
    for i in range(0, 10000):
        p.set(str(i))
        d = p.get()
        print d
        root.update_idletasks()

root = tk.Tk()
d = StringVar()
S=StartStop(root)
main()
root.mainloop()

