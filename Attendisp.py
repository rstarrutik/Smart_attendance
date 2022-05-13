
from tkinter import *
import tkinter.ttk as ttk
import csv


class ShowAttendance:
  def __init__(self,root):
    
    root.title("Attendance Sheet")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)


    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Firstname', text="Name", anchor=W)
    tree.heading('Lastname', text="Date", anchor=W)
    tree.heading('Address', text="Time", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    with open('Attendance.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            firstname = row['firstname']
            lastname = row['lastname']
            address = row['address']
            tree.insert("", 0, values=(firstname, lastname, address))

#============================INITIALIZATION==============================
if __name__ == '__main__':
    root = Tk()
    ob = ShowAttendance(root)
    root.mainloop()