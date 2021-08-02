# ---callback functions---
def select_button():
    btn.config(bg='green', activebackground='green', relief=SUNKEN)

# ---main---
# List of buttons to be created
list = ['A', 'B', 'C']
buttons = []

# Create buttons
for i, name in enumerate(list, 2):
    btn = Button(root, text=name, command=select_button)
    btn.grid(row=i, column=0, sticky=W)
    buttons.append(btn)
