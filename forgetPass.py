from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import csv
import pandas as pd
import os
# from django.forms import DateField
# from dbshow import DB_Show
# import mysql.connector
# import cal
# from face import face_cr
# import os



class forgetPass:
    def __init__(self,root):

        self.root =root
        self.root.geometry("500x500+0+0")
        self.root.title("Face recognition System")


        self.username=StringVar()
        self.dob=StringVar()
        self.password=StringVar()
        self.repass=StringVar()        



        # first img
        img=Image.open(r"Dependencies\MPimg.jpeg")
        img=img.resize((500,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=100)


        #Bg
        img3=Image.open(r"Dependencies\MANREGA01.png")
        img3=img.resize((500,400),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        BGimg = Label(self.root,image = self.photoimg3)
        BGimg.place(x=0,y=100,width =500,height=400)


        title_lbl = Label(BGimg,text ="Forget Password",font=("times new roman",20,"bold"))
        title_lbl.place(x=0,y=0,width=500,height=40)


        # Main Frame
    
        main_frame = Frame(BGimg,bd =2)
        main_frame.place(x=10,y=50,width =480,height=340)


        username=Label(main_frame, text="Username:", font=("times new roman",13, "bold"),bg="white") 
        username.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        username=ttk.Entry(main_frame,textvariable=self.username, width=20, font=("times new roman",13, "bold"),background="white") 
        username.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # DOJ
        dob=Label(main_frame, text="Date of Birth:", font=("times new roman",13, "bold"),bg="white") 
        dob.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        dob=ttk.Entry(main_frame,textvariable=self.dob, width=20, font=("times new roman",13, "bold"),background ="white") 
        dob.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # LOcation
        password=Label(main_frame, text="Password:", font=("times new roman",13, "bold"),bg="white") 
        password.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        passwordentry=ttk.Entry(main_frame,textvariable=self.password, width=20, font=("times new roman",13, "bold"),background ="white") 
        passwordentry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # UserName
        re_pass=Label(main_frame, text="Re-type Password", font=("times new roman",13, "bold"),bg="white") 
        re_pass.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        re_passentry=ttk.Entry(main_frame,textvariable=self.repass, width=20, font=("times new roman",13, "bold"),background ="white") 
        re_passentry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        save_btn=Button (main_frame, text="Update Password",width=15,font=("times New Roman" , 13, "bold"),bg="blue",fg="white",command=self.updatetion)
        save_btn.grid(row=4, column=0,padx=30)


    def updatetion(self):
        details_check =self.check(self.username.get(),self.dob.get())

        if self.username.get()=="" or self.dob.get()=="": 
            messagebox.showerror("Error", "all field required")

        elif details_check == "pass":
            messagebox.showinfo("Success","Password changed Successfully")
            
        else:

            messagebox.showerror("Invalid", "Invalid username&password")

    
    



    def check(self,username, dob):
            #read csv, and split on "," the line
            user_info = csv.reader(open('user_info.csv', "r"), delimiter=",")
            i=0
            #loop through the csv list
            for row in user_info:
                i=i+1
                #if current rows 1st, 2nd and 3rd values are equal to input, print that row
                if username == row[0] and dob == row[4]:
                    details_check = "pass"
                    
                    row[1]=self.checkPass()#Update Pass into CSv

                else: details_check = "fail"
            return details_check
    

    def checkPass(self):
        password1 = "password1"
        password2 = "password2"
        i =0
        while password1 != password2 and i==0:
            password1 = self.password.get()
            password2 = self.repass.get()
            i=i+1
            if password1 != password2: 
                messagebox.showerror("Error!","Passwords don't match. Re-enter matching passwords.")
                
        password = password2
        return password



if __name__ == "__main__":
    root = Tk()
    ob =  forgetPass(root)
    root.mainloop()
