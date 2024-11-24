from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if(usernameEntry.get()=='' or passwordEntry.get()==''):
        messagebox.showerror('Error','username and password are required to login')
    elif(usernameEntry.get()=='Musashi' and passwordEntry.get()=='invincible'):
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Incorrect username or password')




root=CTk()
root.geometry('1000x667')
root.resizable(0,0)
root.title('login page')
img=CTkImage(Image.open('cover.jpg'),size=(1000,667))
imageLabel=CTkLabel(root,image=img,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#d5d7e2',font=('Arial',20,'bold'),text_color='darkblue')
headinglabel.place(x=60,y=150)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',height=40,width=200)
usernameEntry.place(x=95,y=200)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',height=40,width=200,show='*')
passwordEntry.place(x=95,y=250)

loginButton=CTkButton(root,text='Login',height=35,cursor='hand2',command=login)
loginButton.place(x=120,y=310)
root.mainloop()
