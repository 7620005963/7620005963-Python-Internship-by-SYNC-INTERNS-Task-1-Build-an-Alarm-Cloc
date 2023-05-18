from tkinter import *
from tkinter import ttk
import time

timeVar = time.localtime()

root = Tk()

root.title("Display")
hourVar = StringVar()
minVar = StringVar()
secVar = StringVar()

Ahour = StringVar()
Amin = StringVar()
Asec = StringVar()
AsetTimeHour = StringVar()
AsetTimeMin = StringVar()
AsetTimeSec = StringVar()

frame = ttk.Frame(root)
frame.grid()

frame11 = ttk.Frame(root, padding=10)
frame11.grid(column=1, row=0)

s = ttk.Style()
s.theme_use("alt")


def update():
    global timeVar

    timeVar = time.localtime()
    hourVar.set(str(timeVar.tm_hour))
    minVar.set(str(timeVar.tm_min))
    secVar.set(str(timeVar.tm_sec))
    if ((hourVar.get() == Ahour.get()) and (minVar.get() == Amin.get()) and (secVar.get() == Asec.get())):
        alarmWin = Toplevel(root)
        root.bell()
        alarmWin.title("Alarm")
        s.configure("Aframe.TFrame", background="cyan")
        Aframe = ttk.Frame(alarmWin, style="Aframe.TFrame", padding=100)
        # Aframe.configure(background = "cyan")
        Aframe.grid()

        ttk.Label(Aframe, text="Alarm ").grid(column=2, row=0, sticky=(W, E))
        ttk.Button(Aframe, text="QUIT", command=alarmWin.destroy).grid(column=0, row=10)


    root.after(1000, update)


def alarmset():
    childWin = Toplevel(root)
    childWin.title("Alarm Set")
    frame1 = ttk.Frame(childWin)
    frame1.grid()
    ttk.Label(frame1, text="Hour").grid(column=2, row=0, ipadx=20, ipady=10)
    ttk.Entry(frame1, textvariable=AsetTimeHour).grid(column=2, row=1)
    ttk.Label(frame1, text="Min").grid(column=3, row=0)
    ttk.Entry(frame1, textvariable=AsetTimeMin).grid(column=3, row=1)
    ttk.Label(frame1, text="Sec").grid(column=4, row=0)
    ttk.Entry(frame1, textvariable=AsetTimeSec).grid(column=4, row=1)

    def Aset():
        try:
            xyz = AsetTimeHour.get()
            Ahour.set(str(int(AsetTimeHour.get())))
        except:
            Ahour.set("")
        try:
            Amin.set(str(int(AsetTimeMin.get())))
        except:
            Amin.set("")
        try:
            Asec.set(str(int(AsetTimeSec.get())))
        except:
            Asec.set("")


    ttk.Button(frame1, text="QUIT", command=childWin.destroy).grid(column=0, row=10)
    ttk.Button(frame1, text="Set", command=Aset).grid(column=1, row=10)


def alarmset15sec():
    global timeVar
    x = int((timeVar.tm_sec + 15) if (timeVar.tm_sec + 15) <= 59 else (timeVar.tm_sec + 15) - 60)
    y = 0
    z = 0
    if x < 15:
        y = int((timeVar.tm_min + 1) if (timeVar.tm_min + 1) <= 59 else (timeVar.tm_min + 1) - 60)
        z = int((timeVar.tm_hour))
        if y < 1:
            z = int((timeVar.tm_hour + 1) if (timeVar.tm_hour + 1) <= 23 else (timeVar.tm_hour + 15) - 24)
        try:
            Amin.set(str(y))
        except:
            Amin.set("")
        try:
            Asec.set(str(x))
        except:
            Asec.set("")
        try:
            Ahour.set(str(z))
        except:
            Ahour.set("")

    if x >= 15:
        y = int((timeVar.tm_min))
        z = int((timeVar.tm_hour))
        try:
            Amin.set(str(y))
        except:
            Amin.set("")
        try:
            Asec.set(str(x))
        except:
            Asec.set("")
        try:
            Ahour.set(str(z))
        except:
            Ahour.set("")


s.configure("timelabel.TLabel", font="Arial 24", padding=20)
hourLabel = ttk.Label(frame, textvariable=hourVar, style="timelabel.TLabel")
hourLabel.grid(column=1, row=1, sticky=(E))
ttk.Label(frame, text=" : ", style="timelabel.TLabel").grid(column=2, row=1)
minLabel = ttk.Label(frame, textvariable=minVar, style="timelabel.TLabel")
minLabel.grid(column=3, row=1, sticky=(E))
ttk.Label(frame, text=" : ", style="timelabel.TLabel").grid(column=4, row=1)
secLabel = ttk.Label(frame, textvariable=secVar, style="timelabel.TLabel")
secLabel.grid(column=5, row=1, sticky=(E))

ttk.Label(frame11, text="Alarm Time").grid(column=1, row=0)
ttk.Label(frame11, text="Hour").grid(column=1, row=2)
ttk.Label(frame11, textvariable=Ahour).grid(column=1, row=3)

ttk.Label(frame11, text=" : ").grid(column=2, row=3)

ttk.Label(frame11, text="Min").grid(column=3, row=2)
ttk.Label(frame11, textvariable=Amin).grid(column=3, row=3)

ttk.Label(frame11, text=" : ").grid(column=4, row=3)

ttk.Label(frame11, text="Sec").grid(column=5, row=2)
ttk.Label(frame11, textvariable=Asec).grid(column=5, row=3)

ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=10)
ttk.Button(frame, text="Alarm Set", command=alarmset).grid(column=2, row=10)
ttk.Button(frame, text="Alarm Set 15 sec", command=alarmset15sec).grid(column=3, row=10)
update()
root.mainloop()
