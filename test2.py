import tkinter
from tkinter import *
import os
import time
import pyautogui
import customtkinter as tk
from tkinter import filedialog
from winotify import *
import args as ar

tk.set_appearance_mode("System")


def function():
    try:
        a = str(filename)
    except NameError:
        a = str(e1.get())
    a = str(e1.get())
    ask = int(e4.get())
    ask1 = int(e3.get())
    autotyper(a, ask, ask1)


def countdown(sec):
    global l8
    toast = Notification(app_id="Autotyper", title="Autotyper", msg="Countdown Started",
                         icon=r"C:\Users\chara\PycharmProjects\pythonProject3\timer start.png")
    toast.set_audio(audio.Mail, loop=False)
    toast.show()
    while sec >= 0:
        print(sec, "till execution")
        l4 = tk.CTkLabel(master, text=sec, text_color="red")
        l4.place(relx=0.87, rely=0.5)
        l8 = tk.CTkLabel(master, text="sec", text_color="red")
        l8.place(relx=0.9, rely=0.5)
        master.update()
        l4.place_forget()
        l8.place_forget()
        time.sleep(1)
        sec -= 1
    return


def browse_files():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("all files",
                                                      "*.*"),
                                                     ("Text files",
                                                      "*.txt*"),
                                                     ("Python files",
                                                      "*.py*")))
    print(filename)
    e1.delete(0, END)
    e1.insert(0, filename)


my_has = False


def warning_delete():
    global l5
    global my_has
    if var.get() == 1:
        l5 = tk.CTkLabel(master, text="WARNING:The file selected will be deleted after copying",
                         font=("Arial Bold", 13), text_color="red")
        l5.place(relx=0.1, rely=0.85)
        my_has = True
        e2.deselect()
    if var.get() == 0:
        l5.place_forget()
    my_check(ar)


def del_func():
    if my_has:
        l5.place_forget()
    e4.deselect()
    my_check(ar)

def my_check(ar):
    global k
    k=0
    #global l72
    my_flag = False
    try:
        temp = int(e3.get())
        if len(e1.get()) > 0:
            my_flag = True
        else:
            if var.get() == 1:
                e4.deselect()
                l5.place_forget()
            if var1.get() == 2:
                e2.deselect()
            l72 = tk.CTkLabel(master, text="PLEASE FILL THE ABOVE BOXES",
                              font=("Arial Bold", 13), text_color="red")
            l72.place(relx=0.2, rely=0.85)
            k=1
    except ValueError:
        if len(e1.get())==0:
            if var.get() == 1:
                e4.deselect()
                l5.place_forget()
            if var1.get() == 2:
                e2.deselect()
            l72 = tk.CTkLabel(master, text="PLEASE FILL THE ABOVE BOXES",
                              font=("Arial Bold", 13), text_color="red")
            l72.place(relx=0.2, rely=0.85)
            k=1
        else:
            if var.get() == 1:
                e4.deselect()
                l5.place_forget()
            if var1.get() == 2:
                e2.deselect()
            l72 = tk.CTkLabel(master, text="PLEASE FILL THE ABOVE BOXES",
                              font=("Arial Bold", 13), text_color="red")
            l72.place(relx=0.2, rely=0.85)
            k=1

    if my_flag:
        submitbn.configure(state="normal")
        if k==1:
            l72.place_forget()
    else:
        submitbn.configure(state="disabled")

    master.update()
count = 0


def temp_text(e):
    global count
    if count != 1:
        e3.delete(0, END)
        count += 1


def autotyper(a, ask, ask1):
    if os.path.exists(a):
        fout = open(a, 'r')
        countdown(ask1)
        for line in fout:
            pyautogui.typewrite(line)
        if ask == 1:
            fout.close()
            os.remove(a)
        toast = Notification(app_id="Autotyper", title="Autotyper", msg="Task Completed Sucessfully",
                             icon=r"C:\Users\chara\PycharmProjects\pythonProject3\Sucessful.png")
        toast.set_audio(audio.Mail, loop=False)
        toast.show()
        e1.delete(0, END)
        e3.delete(0, END)
        l8.place_forget()
        submitbn.configure(state="disabled")
        if var.get() == 1:
            var.set(0)
        else:
            var1.set(0)
    else:
        toast = Notification(app_id="Autotyper", title="Autotyper", msg="File Doesn't Exist",
                             icon=r"C:\Users\chara\PycharmProjects\pythonProject3\Broken file1.png")
        toast.set_audio(audio.Mail, loop=False)
        toast.show()


master = tk.CTk()
master.geometry("500x200")
master.resizable(False, False)
master.title("Autotyper (BETA)")
var = tkinter.IntVar()
var1 = tkinter.IntVar()
photo = PhotoImage(file="logo.png")
master.iconphoto(False, photo)

l1 = tk.CTkLabel(master, text="Enter the Path", font=("Arial Bold", 13))
l1.place(relx=0.1, rely=0.1)

e1 = tk.CTkEntry(master, width=35)
e1.place(relx=0.6, rely=0.1, width=100)

l2 = tk.CTkLabel(master, text="Delete File after copying", font=("Arial Bold", 13))
l2.place(relx=0.1, rely=0.5)

e2 = tk.CTkCheckBox(master, text="No", font=("Arial Bold", 10), variable=var1, onvalue=2, offvalue=0, command=del_func)
e2.place(relx=0.6, rely=0.5, width=100)

e4 = tk.CTkCheckBox(master, text="Yes", font=("Arial Bold", 10), variable=var, onvalue=1, offvalue=0,
                    command=warning_delete)
e4.place(relx=0.7, rely=0.5, width=100)

l3 = tk.CTkLabel(master, text="Enter Delay", font=("Arial Bold", 13))
l3.place(relx=0.1, rely=0.3)

e3 = tk.CTkEntry(master, width=35)
e3.place(relx=0.6, rely=0.3, width=100)
e3.insert(0, "In Seconds")
e3.bind("<FocusIn>", temp_text)

submitbn = tk.CTkButton(master, text="Execute", state="disabled", command=function)
submitbn.place(relx=0.45, rely=0.75, width=80, anchor=tkinter.CENTER)

buttuon_explore = tk.CTkButton(master, text="Browse Files", command=browse_files)
buttuon_explore.place(relx=0.8, rely=0.1, width=105)

# result=tk.Label(master)
master.mainloop()
