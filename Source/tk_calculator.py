from tkinter import *
from tkinter import ttk


def sum_func(event):
	num1 = float(fnEntry.get())
	num2 = float(snEntry.get())
	sum = num1 + num2

	resEntry.delete(0,"end")
	resEntry.insert(0,sum)

def sub_func(event):
	num1 = float(fnEntry_s.get())
	num2 = float(snEntry_s.get())
	sub = num1 - num2

	resEntry_s.delete(0,"end")
	resEntry_s.insert(0,sub)


root = Tk()
root.resizable(width=False,height=False)
root.title("Simple Addition/Substraction Calculator")



#root.iconbitmap(r'c:\Users\Ermal\Desktop\favicon.ico')

#sum GUI
fnEntry = ttk.Entry(root)
plabel = ttk.Label(root,text="+")
snEntry = ttk.Entry(root)
ebutton = ttk.Button(root,text="=")
resEntry = ttk.Entry(root)

ebutton.bind("<Button-1>",sum_func)

fnEntry.grid(row=0,column=0)
plabel.grid(row=0,column=1)
snEntry.grid(row=0,column=2)
ebutton.grid(row=0,column=3)
resEntry.grid(row=0,column=4)


#sub GUI
fnEntry_s = ttk.Entry(root)
plabel_s = ttk.Label(root,text="-")
snEntry_s = ttk.Entry(root)
ebutton_s = ttk.Button(root,text="=")
resEntry_s = ttk.Entry(root)

ebutton_s.bind("<Button-1>",sub_func)

fnEntry_s.grid(row=1,column=0)
plabel_s.grid(row=1,column=1)
snEntry_s.grid(row=1,column=2)
ebutton_s.grid(row=1,column=3)
resEntry_s.grid(row=1,column=4)


root.mainloop()

