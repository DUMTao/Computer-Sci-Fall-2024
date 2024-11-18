import tkinter

window = tkinter.Tk()
temps = tkinter.Label(text='Name', foreground='blue', background='white', width=25, height=5)
temps.pack()

ent_username = tkinter.Entry()
ent_username.pack()

label_password = tkinter.Label(text='Password', foreground='blue', background='white', width=25, height=5)
label_password.pack()

cont_password = tkinter.Entry()
cont_password.pack()

btm_submit = tkinter.Button(text='Submit', width=10, height=3)





window.mainloop()