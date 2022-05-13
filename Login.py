from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import csv
from main import Face_Recognition_System



class Login:

    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")


        self.bgimg=ImageTk.PhotoImage (file=r"Dependencies\MANREGA01.png")
        # self.bgimg = Image.open(r"B:\MajorProject\Dependencies\Manrega.png")
        # self.bgimg.resize((1530,1080),Image.Resampling.LANCZOS)
        lbl_bg=Label(self.root, image=self.bgimg) 
        lbl_bg.place(x=0, y=0, relwidth=1,relheight=1)


        frame=Frame(self.root, bg="black")
        frame.place(x=610, y=170,width=340, height=450)

        img1=Image.open(r"Dependencies\LoginAvtar.jpg")

        img1=img1.resize((100,100), Image.Resampling.LANCZOS) 
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1, bg="black",borderwidth=0)

        lblimg1.place(x=730, y=175,width=100, height=100)
        get_str=Label(frame, text="Hello! MANREGA Admin", font=("times new roman", 20, "bold"), fg="white", bg="black") 
        get_str.place(x=15, y=100)


        #label

        usernameLable=Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white",bg="black")
        usernameLable.place(x=70, y=155)

        self.txtuser=ttk. Entry (frame, font=("times new roman", 15, "bold")) 
        self.txtuser.place(x=40, y=180,width=270)

        passwordLable=Label (frame, text="Password", font=("times new roman", 15, "bold"), fg="white",bg="black") 
        passwordLable.place(x=70, y=225)

        self.txtpass=ttk. Entry (frame, font=("times new roman", 15, "bold")) 
        self.txtpass.place(x=40, y=250,width=270)

        #======Icon Images=================

        img2=Image.open(r"Dependencies\usernameIC.png")
        img2=img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk. PhotoImage (img2)

        lblimg1=Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3=Image.open(r"Dependencies\password.jfif")
        img3=img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk. PhotoImage (img3)

        lblimg1=Label(image=self.photoimage3, bg="black", borderwidth=0) 
        lblimg1.place(x=650, y=395, width=25,height=25)

        # LoginButton

        loginbtn=Button(frame, text="Login", font=("times new roman", 15, "bold"),command=self.jumpToMain, bd=3, relief=RIDGE, fg="white", bg="red", activebackground="red" ,activeforeground="white") 
        loginbtn.place(x=110, y=300, width=120,height=35)

        #registerbutton

        registerbtn=Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white",bg="black",activebackground="black",activeforeground="white") 
        registerbtn.place(x=15, y=350, width=168)

        #forgetpassbtn

        registerbtn=Button(frame, text="Forget Password", font=("times new roman",10, "bold"), borderwidth=0, fg="white", bg = "black", activebackground="black" , activeforeground="white") 
        registerbtn.place(x=13, y=370, width=160)




        def login(self):
            details_check =checkDetails(self.txtuser.get(),self.txtpass.get())

            if self.txtuser.get()=="" or self.txtpass.get()=="": 
                messagebox.showerror("Error", "all field required")

            elif details_check == "pass":
                self.faceRec()

            else:

                messagebox.showerror("Invalid", "Invalid username&password")



        def checkDetails(username, password):
            #read csv, and split on "," the line
            user_info = csv.reader(open('user_info.csv', "r"), delimiter=",")
            #loop through the csv list
            for row in user_info:
                #if current rows 1st, 2nd and 3rd values are equal to input, print that row
                if username == row[0] and password == row[1]:
                    details_check = "pass"
                else: details_check = "fail"
            return details_check


    def jumpToMain(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

       
    


    




if __name__ == "__main__":
    root = Tk()
    ob =  Login(root)
    root.mainloop()