from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Sportka')
root.geometry("500x500")
my_tree = ttk.Treeview(root)

#Sloupce
my_tree['columns'] = ("1","2","3","4","5","6","7")

my_tree.column("#0", width=0, minwidth=0)
my_tree.column("#1", anchor=CENTER, width=50)
my_tree.column("#2", anchor=CENTER, width=50)
my_tree.column("#3", anchor=CENTER, width=50)
my_tree.column("#4", anchor=CENTER, width=50)
my_tree.column("#5", anchor=CENTER, width=50)
my_tree.column("#6", anchor=CENTER, width=50)
my_tree.column("#7", anchor=CENTER, width=50)

#První radek
#my_tree.heading("#0", text="Label")
#my_tree.heading("#1", text="Label")
#my_tree.heading("#2", text="Label")
#my_tree.heading("#3", text="Label")
#my_tree.heading("#4", text="Label")
#my_tree.heading("#5", text="Label")
#my_tree.heading("#6", text="Label")
#my_tree.heading("#7", text="Label")


#Data
my_tree.insert(parent='', index='end', iid=0, text="", values=(1,2,3,4,5,6,7))
my_tree.insert(parent='', index='end', iid=1, text="", values=(8,9,10,11,12,13,14))
my_tree.insert(parent='', index='end', iid=2, text="", values=(15,16,17,18,19,20,21))
my_tree.insert(parent='', index='end', iid=3, text="", values=(22,23,24,25,26,27,28))
my_tree.insert(parent='', index='end', iid=4, text="", values=(29,30,31,32,33,34,35))
my_tree.insert(parent='', index='end', iid=5, text="", values=(36,37,38,39,40,41,42))
my_tree.insert(parent='', index='end', iid=6, text="", values=(43,44,45,46,47,48,49))



my_tree.pack(pady=20)

root.mainloop()