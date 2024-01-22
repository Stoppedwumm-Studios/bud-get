import tkinter as tk
import PIL
import threading
import os


def LoadOverview():
    window = tk.Tk()
    window.title("Overview")
    UBar = tk.Frame(window)
    T = tk.Label(UBar, text="Bud-Get Overview")
    T.pack()
    UBar.pack()
    window.mainloop()
    


mainwindow = tk.Tk()
mainwindow.title("Bud-Get")
UpperBar = tk.Frame(mainwindow)
Actions = tk.Frame(mainwindow)
Title = tk.Label(UpperBar, text="Bud-Get", width=20, height=5)
Overview = tk.Button(Actions, text="Overview", command=LoadOverview)
Title.pack()
UpperBar.pack()
Overview.pack()
Actions.pack()

mainwindow.mainloop()
