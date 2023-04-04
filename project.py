from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
a = mysql.connect(user='root', password='root', host='localhost', database="Library")
print(a)
b = a.cursor()
# b.execute("create database Library")
w = Tk()
w.title("Leroy's Library")
w.config(bg="#74bff2")
w.geometry("800x600")
w.minsize(800, 600)
w.maxsize(800, 600)

def Signin():
    for widget in w.winfo_children():
        widget.destroy()

    def validate():
        if e1s.get() == "":
            messagebox.showerror("Error", "Please Enter Your Full Name")
        elif e2s.get() == "":
            messagebox.showerror("Error", "Please Enter Your Phone Number")
        elif e3s.get() == "":
            messagebox.showerror("Error", "Please Enter Your Email")
        elif "@" not in e3s.get():
            messagebox.showerror("Error", "Please Enter Valid Email")
        elif e4s.get() == "":
            messagebox.showerror("Error", "Please Enter a Username")
        elif e5s.get() == "":
            messagebox.showerror("Error", "Please Enter a Password")
        else:
            b = a.cursor()
            b.execute(f"insert into Library.login values('{e1s.get()}', '{int(e2s.get())}', '{e3s.get()}', '{e4s.get()}','{e5s.get()}');")
            a.commit()
            messagebox.showinfo("Success", "Your Registration Was Successful!")

    # Head Sign in
    l1s = Label(text="Sign-in Page", bg="#74bff2", font="Times 40 bold")
    l1s.place(x=225, y=10)

    # Body Sign in
    l2s = Label(text="Your Full Name:", bg="#74bff2", font="Times 17 bold")
    l2s.place(x=65, y=120)

    l3s = Label(text="Your Phone No.:", bg="#74bff2", font="Times 17 bold")
    l3s.place(x=65, y=180)

    l4s = Label(text="Your Email:", bg="#74bff2", font="Times 17 bold")
    l4s.place(x=65, y=240)

    l5s = Label(text="Enter Unique Username:", bg="#74bff2", font="Times 17 bold")
    l5s.place(x=65, y=300)

    l6s = Label(text="Enter Password:", bg="#74bff2", font="Times 17 bold")
    l6s.place(x=65, y=360)

    # Entry Sign in
    e1s = Entry(width=50)
    e1s.place(x=400, y=130)

    e2s = Entry(width=50)
    e2s.place(x=400, y=190)

    e3s = Entry(width=50)
    e3s.place(x=400, y=250)

    # username and password entry Sign in
    e4s = Entry(width=50)
    e4s.place(x=400, y=310)

    e5s = Entry(width=50, show='*')
    e5s.place(x=400, y=370)

    # Buttons Sign in
    b1s = Button(text="Register", activebackground="#45c8f9", activeforeground="black", command=validate)
    b1s.place(x=550, y=510)

    b2s = Button(text="Login here", activebackground="#45c8f9", activeforeground="black", command=login)
    b2s.place(x=200, y=510)

def login():
    for widget in w.winfo_children():
        widget.destroy()

    def check():
        if e1l.get() == "":
            messagebox.showerror("Error", "Please Enter Username")
        elif e2l.get() == "":
            messagebox.showerror("Error", "Please Enter Password")
        else:
            username = e1l.get()
            password = e2l.get()
            b.execute("select username, password from login where username=%s and password=%s", (username, password))
            row=b.fetchone()
            if row==None:
                messagebox.showerror("Error", "Wrong username or password!")
            else:
                Library()

    # Head Login
    l1l = Label(text="Login Page", bg="#74bff2", font="Times 40 bold")
    l1l.place(x=225, y=10)

    #Label Login
    l2l = Label(text="Your Username:", bg="#74bff2", font="Times 17 bold")
    l2l.place(x=65, y=120)

    l3l = Label(text="Your Password:", bg="#74bff2", font="Times 17 bold")
    l3l.place(x=65, y=230)

    #Entry Login
    e1l = Entry(width=50)
    e1l.place(x=400, y=130)

    e2l = Entry(width=50, show="*")
    e2l.place(x=400, y=230)

    # Buttons
    b2l = Button(text="Login", font="Times 15", activebackground="#45c8f9", activeforeground="black", command=check)
    b2l.place(x=575, y=350)

    b1l = Button(text="Sign-up here", font="Times 15", activebackground="#45c8f9", activeforeground="black",command=Signin)
    b1l.place(x=70, y=350)

def Library():
    for widget in w.winfo_children():
        widget.destroy()

    w.geometry("1200x800")
    w.minsize(1200, 800)
    w.maxsize(1200, 800)

    # Head Library
    Li = Label(text="Leroy's Library", bg="#74bff2", font="Times 40 bold")
    Li.place(x=500, y=10)

    




#Main page
l1 = Label(text="Leroy's Library", bg="#74bff2", font="Times 40 bold")
l1.place(x=225, y=10)

#Sign in
l2 = Label(text="Register here", bg="#74bff2", font="Times 17 bold")
l2.place(x=65, y=250)
btn1 = Button(text="Sign-up here", font="Times 15", activebackground="#45c8f9", activeforeground="black", command=Signin)
btn1.place(x=70, y=350)

#Login
l3 = Label(text="Already have an account?\nLogin here", bg="#74bff2", font="Times 17 bold")
l3.place(x=500, y=250)
btn2 = Button(text="Login here", font="Times 15", activebackground="#45c8f9", activeforeground="black", command=login)
btn2.place(x=575, y=350)

w.mainloop()