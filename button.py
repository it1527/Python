from tkinter import *
import tkinter


root=tkinter.Tk()
root.title("grid() method")
root.geometry("250x200")



    



sloupec = 1
y = 1
for x in (x+1 for x in range(49)):
    myButton1 = tkinter.Button(root, text=x)
    myButton1.grid(row=y, column=sloupec)
    if (x % 7 == 0):
        y=y+1
        sloupec =0
    sloupec = sloupec +1    

root.mainloop()