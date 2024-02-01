import tkinter
from tkinter import *
import os
import time
import pyautogui
import customtkinter as tk
from tkinter import filedialog
from winotify import *


tk.set_appearance_mode("System")



def fubction():
    try:
        a = str(filename)
    except NameError:
        a=str(e1.get())
    a=str(e1.get())
    ask=int(e4.get())
    ask1=int(e3.get())
    autotyper(a,ask,ask1)

def countdown(sec):
    toast = Notification(app_id="Autotyper", title="Autotyper", msg="Countdown Started",
                         icon=r"C:\Users\chara\PycharmProjects\pythonProject3\timer start.png")
    toast.set_audio(audio.Mail, loop=False)
    toast.show()
    while sec>=0:
        print(sec,"till execution")
        l4=tk.CTkLabel(master,text=sec, text_color="red")
        l4.place(relx=0.9,rely=0.5)
        master.update()
        l4.place_forget()
        time.sleep(1)
        sec-=1
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
    e1.insert(0,filename)

my_has=False
def warning_delete():
    global l5
    global my_has
    if var.get()==1:
        l5=tk.CTkLabel(master,text="WARNING:The file selected will be deleted after copying",font=("Arial Bold",13),text_color="red")
        l5.place(relx=0.1,rely=0.85)
        my_has=True
        e2.deselect()
    if var.get()==0:
        l5.place_forget()
def del_func():
    if my_has:
        l5.place_forget()
    e4.deselect()


count=0
def temp_text(e):
    global count
    if count!=1:
        e3.delete(0,END)
        count+=1

def autotyper(a,ask,ask1):
    if os.path.exists(a):
        fout = open(a, 'r')
        countdown(ask1)
        for line in fout:
            pyautogui.typewrite(line)
        if ask==1:
            fout.close()
            os.remove(a)
        toast = Notification(app_id="Autotyper", title="Autotyper", msg="Task Completed Sucessfully",
                             icon=r"C:\Users\chara\PycharmProjects\pythonProject3\Sucessful.png")
        toast.set_audio(audio.Mail, loop=False)
        toast.show()
    else:
        toast = Notification(app_id="Autotyper", title="Autotyper", msg="File Doesn't Exist",
                             icon=r"C:\Users\chara\PycharmProjects\pythonProject3\Broken file1.png")
        toast.set_audio(audio.Mail, loop=False)
        toast.show()


master=tk.CTk()
master.geometry("500x200")
master.resizable(False,False)
master.title("Autotyper")
var=tkinter.IntVar()
var1=tkinter.IntVar()
var17=tkinter.IntVar()
photo = PhotoImage(file ="logo.png")
master.iconphoto(False, photo)




l1=tk.CTkLabel(master,text="Enter the Path",font=("Arial Bold",13))
l1.place(relx=0.1,rely=0.1)

e1=tk.CTkEntry(master,width=35)
e1.place(relx=0.6,rely=0.1,width=100)





l2=tk.CTkLabel(master,text="Delete File after copying",font=("Arial Bold",13))
l2.place(relx=0.1,rely=0.3)

e2=tk.CTkCheckBox(master,text="No",font=("Arial Bold",10),variable=var1,onvalue=2,offvalue=0,command=del_func)
e2.place(relx=0.6,rely=0.3,width=100)


e4=tk.CTkCheckBox(master,text="Yes",font=("Arial Bold",10),variable=var,onvalue=1,offvalue=0,command=warning_delete)
e4.place(relx=0.7,rely=0.3,width=100)





l3=tk.CTkLabel(master,text="Enter Delay",font=("Arial Bold",13))
l3.place(relx=0.1,rely=0.5)

e3=tk.CTkEntry(master,width=35)
e3.place(relx=0.6,rely=0.5,width=100)
e3.insert(0,"In Seconds")
e3.bind("<FocusIn>",temp_text)





submitbn=tk.CTkButton(master,text="Execute",command=fubction)
submitbn.place(relx=0.45,rely=0.75,width=80,anchor=tkinter.CENTER)

buttuon_explore=tk.CTkButton(master,text="Browse Files",command=browse_files)
buttuon_explore.place(relx=0.8,rely=0.1,width=105)



#result=tk.Label(master)
master.mainloop()