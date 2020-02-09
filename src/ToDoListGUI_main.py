import Tkinter
import tkMessageBox
import random

root = Tkinter.Tk()
root.configure(bg="white")
root.title("Marcelo's Super To Do List")
root.geometry("325x275")

#list
tasks = []
#List used for testing
tasks = []

#Funtions
def update_listbox ():
    #Clear listbox
    clear_listbox()
    #Populate listbox
    for task in tasks:
        lb_tasks.insert("end", task)
    #clear the list box from line 0 until the end of the list   
def clear_listbox():
    lb_tasks.delete(0, "end")
    #Add a task in our list box
def add_task():
    task = txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        tkMessageBox.showwarning("Warning", "Please type a task in the box before click this button")
    txt_input.delete(0,"end")
def del_all():
    if tasks ==[]:
        tkMessageBox.showwarning("Warning","Your list is empty")
    else:
        confirmed = tkMessageBox.askyesno("Please confirm", "Do you really want to delete your list?")
        if confirmed == True:
            global tasks
            tasks = []
            update_listbox()
def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def asc_order():
    tasks.sort()
    update_listbox()
def desc_order():
    tasks.sort()
    tasks.reverse()
    update_listbox()
def choose_random():
    task = random.choice(tasks)
    lbl_display["text"] = task
def number_of_tasks():
    number_of_tasks = len(tasks)
    msg = "Number of tasks: %s" %number_of_tasks
    lbl_display["text"]= msg

#Buttons
lbl_title = Tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = Tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)

txt_input= Tkinter.Entry(root, width="15" )
txt_input.grid(row=1, column=1)

btn_add_task = Tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_del_all = Tkinter.Button(root, text="Delete all", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one = Tkinter.Button(root, text="Delete one", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3, column=0)

btn_asc_order = Tkinter.Button(root, text="Sort (Asc)", fg="green", bg="white", command=asc_order)
btn_asc_order.grid(row=4, column=0)

btn_desc_order = Tkinter.Button(root, text="Sort (Desc)", fg="green", bg="white", command=desc_order)
btn_desc_order.grid(row=5, column=0)

btn_choose_radom = Tkinter.Button(root, text="Choose random", fg="green", bg="white", command=choose_random)
btn_choose_radom.grid(row=6, column=0)

btn_num_task = Tkinter.Button(root, text="Number of Tasks", fg="green", bg="white", command=number_of_tasks)
btn_num_task.grid(row=7, column=0)

btn_exit = Tkinter.Button(root, text="Exit", fg="green", bg="white", command=quit)
btn_exit.grid(row=8, column=0)

lb_tasks = Tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)

root.mainloop()