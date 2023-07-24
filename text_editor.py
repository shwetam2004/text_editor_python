from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

stimulator_window = Tk()
stimulator_window.geometry('600x600') 
stimulator_window.title('Shweta Muthukumar')

heading = Label(stimulator_window, text='Welcome to the Text Editor', font=('Hello valentica', 20), bg='turquoise')
heading.pack()

scrollbar = Scrollbar(stimulator_window)
scrollbar.pack(side=RIGHT, fill=Y)

Editor = Text(stimulator_window, width=400, height=450, yscrollcommand=scrollbar.set)
Editor.pack(fill=BOTH)
scrollbar.config(command=Editor.yview)

def save():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = Editor.get(1.0, tk.END)
        output_file.write(text)
    stimulator_window.title(f"Entitled - {filepath}")

button = Button(stimulator_window, text='Save', font=('Comic sans', 14), command=save, bg='yellow')
button.place(x=270, y=520)

stimulator_window.mainloop()
