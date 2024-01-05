from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#================GUI====================
win = Tk()
win.geometry('300x350+700+100')
win.resizable(0,0)
win.title('Salary')
win.config(bg = 'Orange')
#==============Function=================



#==================WIDGET==================
#==================Label===================
lbl_name = Label(win , text='Name:' , bg = 'Yellow' , font= 'arial 16')
lbl_name.place(x=20 , y=50)
lbl_fname = Label(win , text='Family:' , bg = 'Orange' , font= 'arial 16')
lbl_fname.place(x=20 , y=100)
lbl_Salary = Label(win , text='Salary:' , bg = 'Orange' , font= 'arial 16')
lbl_Salary.place(x=20 , y=150)


#==================Button===================
btn_tax = ttk.Button(win , text= 'Tax' , width= 18)
btn_tax.place(x=20 , y = 210)
btn_bime = ttk.Button(win , text= 'Bime' , width= 18)
btn_bime.place(x=160 , y = 210)
btn_Status = ttk.Button(win , text= 'Status' , width= 18)
btn_Status.place(x=20 , y = 260)
btn_Exit = ttk.Button(win , text= 'Exit' , width= 18)
btn_Exit.place(x=160 , y = 260)

#==================Entry========================
ent_name = Entry(win , width= 24)
ent_name.place(x=100 , y =55)
ent_fname = Entry(win , width= 24)
ent_fname.place(x=100 , y =105)
ent_Salary = Entry(win , width= 24)
ent_Salary.place(x=100 , y =155)


win.mainloop()
