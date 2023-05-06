import tkinter as Tkinter
from datetime import datetime
c=60000
running=False
def c_label(label):
    def count():
        if running:
            global c
            if c==60000:
                display="Starting..."
            else:
                tt=datetime.fromtimestamp(c)
                string=tt.strftime("%H:%M:%S")
                display=string
            label['text']=display
            label.after(1000, count)
            c+=1
    count()
def Start(label):
    global running
    running=True
    c_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running=False
def Reset(label):
    global c
    c=66600

    if running == False:
        reset['state']='disabled'
        label['text']='Welcome!'


    else:
        label['text']='Starting...'
root=Tkinter.Tk()
root.title("Stopwatch")
root.iconbitmap(r"C:UsersdesusDesktop	ime.ipynb_checkpointsstopwatch.ico")
root.configure(bg="#FFE873")
# Fixing the window size.
root.minsize(width=250,height=70)
label=Tkinter.Label(root,text="Welcome!",fg="#4B8BBE",bg="#FFE873",font="Verdana 30 bold")
label.pack()
f=Tkinter.Frame(root)
start=Tkinter.Button(f,text='Start',width=6,command=lambda:Start(label))
stop=Tkinter.Button(f,text='Stop',width=6,state='disabled',command=Stop)
reset=Tkinter.Button(f,text='Reset',width=6,state='disabled',command=lambda:Reset(label))
f.pack(anchor='center',pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()