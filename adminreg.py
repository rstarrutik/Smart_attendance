from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import csv
import os
# from django.forms import DateField
# from dbshow import DB_Show
# import mysql.connector
# import cal
# from face import face_cr
# import os



class Register_New_Admin:
    def __init__(self,root):

        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        self.reg_no=IntVar()
        self.password =StringVar()
        self.admin_name=StringVar()
        self.aadhar=StringVar()
        self.gender=StringVar()
        self.address=StringVar()
        self.working_location=StringVar()
        self.email=StringVar()
        self.phone_no=StringVar()
        self.date_of_birth=StringVar()
        self.date_of_joining=StringVar()
        self.register_by=StringVar()
        self.site_location=StringVar()
        self.worker_image=StringVar()
        self.blood_group=StringVar()
        self.city=StringVar()
        self.username=StringVar()
        self.password=StringVar()
        self.password2=StringVar()




        # first img
        img=Image.open(r"Dependencies\MPimg.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"Dependencies\MPimg1.jpeg")
        img1=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"Dependencies\MPimg2.jpg")
        img2=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1015,y=0,width=500,height=130)


        #Bg
        img3=Image.open(r"Dependencies\MANREGA01.png")
        img3=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        BGimg = Label(self.root,image = self.photoimg3)
        BGimg.place(x=0,y=136,width =1530,height=710)


        title_lbl = Label(BGimg,text ="Register New Admin",font=("times new roman",35,"bold"))
        title_lbl.place(width=1530,height=45)


        # Main Frame
    
        main_frame = Frame(BGimg,bd =2)
        main_frame.place(x=20,y=55,width =1480,height=600)

        #left label 
        leftFrame = LabelFrame(main_frame,bg="#fff123", relief=RIDGE,text="New Form",font=("Times new roman",12,"bold"))
        leftFrame.place(x=10,y=5,width=660,height=800)

        img_left=Image.open(r"Dependencies\WorkerDet.jpg")
        img_left=img_left.resize((660,130), Image.Resampling.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(leftFrame, image=self.photoimg_left) 
        f_lbl.place(x=0, y=0,width=720,height=130)


        detailsFrameL=LabelFrame(leftFrame,bg="#fff123", relief=RIDGE,text="New Form",font=("Times new roman",12,"bold"))
        detailsFrameL.place(x=0,y=140,width=660,height=660)


        # registration

        reginame=Label(detailsFrameL, text="Registered by:", font=("times new roman",13, "bold"),bg="white") 
        reginame.grid(row=0, column=0, padx=18, pady=5, sticky=W)

        regiName=ttk.Entry(detailsFrameL,textvariable=self.register_by, width=20, font=("times new roman",13, "bold"),background="white") 
        regiName.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # DOJ
        Doj=Label(detailsFrameL, text="Date of joining:", font=("times new roman",13, "bold"),bg="white") 
        Doj.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        dOJ=ttk.Entry(detailsFrameL,textvariable=self.date_of_joining, width=20, font=("times new roman",13, "bold"),background ="white") 
        dOJ.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # LOcation
        Site=Label(detailsFrameL, text="site location:", font=("times new roman",13, "bold"),bg="white") 
        Site.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        siteentry=ttk.Entry(detailsFrameL,textvariable=self.site_location, width=20, font=("times new roman",13, "bold"),background ="white") 
        siteentry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # UserName
        user=Label(detailsFrameL, text="Username", font=("times new roman",13, "bold"),bg="white") 
        user.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        userentry=ttk.Entry(detailsFrameL,textvariable=self.username, width=20, font=("times new roman",13, "bold"),background ="white") 
        userentry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # Password
        Password=Label(detailsFrameL, text="Password:", font=("times new roman",13, "bold"),bg="white") 
        Password.grid(row=4, column=0, padx=2, pady=10, sticky=W)

        Passwordentry=ttk.Entry(detailsFrameL,textvariable=self.password, width=20, font=("times new roman",13, "bold"),background ="white") 
        Passwordentry.grid(row=4,column=1,padx=2,pady=10,sticky=W)


        RPassword=Label(detailsFrameL, text="Re-Type Password:", font=("times new roman",13, "bold"),bg="white") 
        RPassword.grid(row=5, column=0, padx=2, pady=10, sticky=W)

        RPasswordentry=ttk.Entry(detailsFrameL,textvariable=self.password2, width=20, font=("times new roman",13, "bold"),background ="white") 
        RPasswordentry.grid(row=5,column=1,padx=2,pady=10,sticky=W)





        #bbuttons frame

        # btn_frame=Frame (leftFrame, bd=2, relief=RIDGE, bg="white") 
        # btn_frame.place (x=0, y=250, width=715,height=70)

        # save_btn=Button (btn_frame,command=self.add_data, text="Save",width=15,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        # save_btn.grid(row=0, column=0)

        # updatebtn=Button (btn_frame, text="Update",width=15,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        # updatebtn.grid(row=0, column=1)

        # del_btn=Button (btn_frame, text="Delete",width=15,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        # del_btn.grid(row=0, column=2)

        # del_btn=Button (btn_frame, text="Reset",width=15,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        # del_btn.grid(row=0, column=3)

        

        



        #Right
        rightFrame = LabelFrame(main_frame,bg="#fff123",
        text="Worker Details",font=("Times new roman",12,"bold"))
        rightFrame.place(x=760,y=5,width=660,height=580)

        
        


        # Worker form
        workerFrame = LabelFrame(rightFrame,bg ="white",font=("Times new roman",12,"bold"))
        workerFrame.place(x=0,y=10,width=660,height=400)

        

        

       

        # name

        Name_label=Label(workerFrame, text="Name:", font=("times new roman",13, "bold"),bg="white") 
        Name_label.grid(row=0, column=0, padx=18, pady=5, sticky=W)

        Name_entry=ttk.Entry(workerFrame,textvariable=self.admin_name, width=20, font=("times new roman", 13, "bold"),background= "white") 
        Name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #adhar

        Id_label=Label(workerFrame, text="Aadhar No:", font=("times new roman",13, "bold"),bg="white") 
        Id_label.grid(row=1, column=0, padx=18, pady=5, sticky=W)

        Id_entry=ttk.Entry(workerFrame,textvariable=self.aadhar, width=20, font=("times new roman",13, "bold"),background= "white") 
        Id_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #radio Buttons
        bloodGroup=Label(workerFrame, text=" gender:", font=("times new roman", 13, "bold"),bg="white") 
        bloodGroup.grid(row=3, column=0, padx=10, pady=5, sticky=W)


        radionbtn1=ttk. Radiobutton (workerFrame, text="Male", value="Yes",variable=self.gender) 
        radionbtn1.grid (row=3, column=1)

        radionbtn2=ttk. Radiobutton (workerFrame, text="Female", value="no",variable=self.gender) 
        radionbtn2.grid (row=4, column=1)




        #Date of birth
        bloodGroup=Label(workerFrame, text="DOB:", font=("times new roman", 13, "bold"),bg="white") 
        bloodGroup.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        bloodEntry=ttk. Entry(workerFrame,textvariable=self.date_of_birth,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=2, column=1, padx=10, pady=5, sticky=W)




        #blood group

        bloodGroup=Label(workerFrame, text="Blood group:", font=("times new roman", 13, "bold"),background= "white") 
        bloodGroup.grid(row=5, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,textvariable=self.blood_group,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=5, column=1, padx=10, pady=5, sticky=W)


        #Address
        bloodGroup=Label(workerFrame, text="Address:", font=("times new roman", 13, "bold"),bg="white") 
        bloodGroup.grid(row=6, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,textvariable=self.address,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=6, column=1, padx=10, pady=5, sticky=W)


        #Email
        bloodGroup=Label(workerFrame, text="Email:", font=("times new roman", 13, "bold"),bg= "white") 
        bloodGroup.grid(row=7, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,textvariable=self.email,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=7, column=1, padx=10, pady=5, sticky=W)

        #phone number
        bloodGroup=Label(workerFrame, text="Phone no:", font=("times new roman", 13, "bold"),bg="white") 
        bloodGroup.grid(row=8, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,textvariable=self.phone_no,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=8, column=1, padx=10, pady=5, sticky=W)

        #City
        bloodGroup=Label(workerFrame, text="City:", font=("times new roman", 13, "bold"),bg= "white") 
        bloodGroup.grid(row=9, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,width=20,textvariable=self.city, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=9, column=1, padx=10, pady=5, sticky=W)

        #ID
        bloodGroup=Label(workerFrame, text="ID:", font=("times new roman", 13, "bold"),bg="white") 
        bloodGroup.grid(row=10, column=0, padx=10, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=10, column=1, padx=10, pady=5, sticky=W)

        # Buttons Frame

        bFrame = LabelFrame(rightFrame,bd=2,bg ="white", relief=RIDGE,font=("Times new roman",12,"bold"))
        bFrame.place(x=0,y=410,width=660,height=50)

        save_btn=Button (bFrame, text="Save Data",width=31,font=("times New Roman" , 13, "bold"),bg="blue",fg="white",command=self.createUser)
        save_btn.grid(row=0, column=2,padx=10)

        reset_btn=Button (bFrame, text="Reset Data",width=31,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3,padx=10)



        detFrame = LabelFrame(rightFrame,bd=2,bg ="white", relief=RIDGE,font=("Times new roman",12,"bold"))
        detFrame.place(x=0,y=500,width=660,height=50)

        det_btn=Button (detFrame, text="Show Admins",width=31,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")#,command=self.showadmins())
        det_btn.grid(row=0, column=0,padx=185,pady=5,sticky=W,)
    
    def showadmins(self):
        os.startfile('user_info.csv')


    def createUser(self): 

        username = self.username.get()    
        password = self.checkPass()
        name=self.admin_name.get()
        adhar=self.aadhar.get()
        dob=self.date_of_birth.get()
        gender=self.gender.get()
        blood=self.blood_group.get()
        Addreess=self.address.get()
        Email=self.email.get()
        phone=self.phone_no.get()
        city=self.city.get()
        regi_no=self.reg_no.get()
        reg_by=self.register_by.get()
        doj=self.date_of_joining.get()
        location=self.site_location.get()

        with open('user_info.csv', mode='a', newline='') as user_info:
            user_writer = csv.writer(user_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            user_writer.writerow([username, password,name,adhar,dob,gender,blood,Addreess,Email,phone,city,regi_no,reg_by,doj,location])    
        messagebox.showinfo("Success!","Admin Added Succesfully")


    def checkPass(self):
        password1 = "password1"
        password2 = "password2"
        i =0
        while password1 != password2 and i==0:
            password1 = self.password.get()
            password2 = self.password2.get()
            
            if password1 != password2: 
                i=i+1
                messagebox.showerror("Error!","Passwords don't match. Re-enter matching passwords.")
            if i==1:
                self.checkPass    
        password = password2
        return password

  
    

    

if __name__ == "__main__":
    root = Tk()
    ob =  Register_New_Admin(root)
    root.mainloop()
