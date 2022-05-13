
import cv2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
# from dbshow import DB_Show
import mysql.connector
# import cal
# from face import face_cr
import os

class worker:

    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")
# ======TextVariables====================================
        self.worker_category=StringVar()
        self.work_type=StringVar()
        self.register_by=StringVar()
        self.date_of_joining=StringVar()
        self.site_location=StringVar()
        self.worker_name=StringVar()
        self.aadhar=StringVar()
        self.date_of_birth=StringVar()
        self.gender=StringVar()
        self.bloodgroup=StringVar()
        self.address=StringVar()
        self.email=StringVar()
        self.phone_no=StringVar()
        self.city=StringVar()
        self.worker_image=StringVar()
        self.var_id=StringVar()
        



# ====UI==========================================================
        # first img
        img=Image.open(r"Dependencies\MPimg.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"Dependencies\MPimg1.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"Dependencies\MPimg2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1015,y=0,width=500,height=130)


        #Bg
        img3=Image.open(r"Dependencies\MANREGA01.png")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        BGimg = Label(self.root,image = self.photoimg3)
        BGimg.place(x=0,y=136,width =1530,height=710)


        title_lbl = Label(BGimg,text ="Worker Management System",font=("times new roman",35,"bold"))
        title_lbl.place(width=1530,height=45)
    
        main_frame = Frame(BGimg,bd =2)
        main_frame.place(x=20,y=55,width =1480,height=450)
# ======Left Frame============================================================
        #left label 
        leftFrame = LabelFrame(main_frame,bg="#fff123", relief=RIDGE,text="New Form",font=("Times new roman",12,"bold"))
        leftFrame.place(x=10,y=5,width=660,height=430)

        img_left=Image.open(r"Dependencies\WorkerDet.jpg")
        img_left=img_left.resize((660,130), Image.Resampling.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(leftFrame, image=self.photoimg_left) 
        f_lbl.place(x=0, y=0,width=720,height=130)

        # Site Details
        siteFrame = LabelFrame(main_frame,bg="white", relief=RIDGE,text="New Registration",font=("Times new roman",12,"bold"))
        siteFrame.place(x=10,y=136,width=660,height=250)


        # Departmet
        dep_label=Label(siteFrame, text="Category", font=("times new roman",12, "bold"),bg="white") # textvariable=self.var_dep,``
        dep_label.grid(row=0, column=0 , padx=10, sticky=W)

        dep_combo=ttk.Combobox (siteFrame,textvariable=self.worker_category, font=("times new roman",12, "bold"), state="readonly")
        dep_combo ["values"]=("Select Category", "A:PUBLIC WORKS", "B:COMMUNITY ASSETS", "C:.COMMON INFRASTRUCTURE", "ADMIN")
        dep_combo.current (0)
        dep_combo.grid(row=0, column=1,padx=2,pady =10, sticky = W)

        # Sub-dept
        wType=Label(siteFrame, text="Work Type", font=("times new roman",12, "bold"),bg="white") 
        wType.grid(row=1, column=0 , padx=10, sticky= W)

        wType_com=ttk.Combobox (siteFrame,textvariable=self.work_type, font=("times new roman",12, "bold"), state="readonly")
        wType_com ["values"]=("Select Work","Watershed", "Irrigation", "flood management", "Agricultural and Livestock", "Fisheries", "Rural Drinking Water","Admin")
        wType_com.current (0)
        wType_com.grid(row=1, column=1,padx=2,pady =10, sticky = W)

        # registration

        reginame=Label(siteFrame, text="Registered by:", font=("times new roman",13, "bold"),bg="white") 
        reginame.grid(row=2, column=0, padx=18, pady=5, sticky=W)

        regiName=ttk.Entry(siteFrame,textvariable=self.register_by, width=20, font=("times new roman",13, "bold"),background="white") 
        regiName.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        # DOJ
        Doj=Label(siteFrame, text="Date of joining:", font=("times new roman",13, "bold"),bg="white") 
        Doj.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        dOJ=ttk.Entry(siteFrame,textvariable=self.date_of_joining, width=20, font=("times new roman",13, "bold"),background ="white") 
        dOJ.grid(row=3,column=1,padx=2,pady=10,sticky=W)


        # LOcation
        Site=Label(siteFrame, text="site location:", font=("times new roman",13, "bold"),bg="white") 
        Site.grid(row=4, column=0, padx=2, pady=10, sticky=W)

        siteentry=ttk.Entry(siteFrame,textvariable=self.site_location, width=20, font=("times new roman",13, "bold"),background ="white") 
        siteentry.grid(row=4,column=1,padx=2,pady=10,sticky=W)


# =======Buttons====================================================================

        bFrame = LabelFrame(leftFrame,bd=2,bg ="white", relief=RIDGE,font=("Times new roman",12,"bold"))
        bFrame.place(x=0,y=350,width=660,height=60)

        takephoto_btn=Button (bFrame, text="Take photo",command=self.take_pic,width=55,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0, column=2,padx=40,pady=10)

        


       

# ======Right Frame========================================================

        #Right
        rightFrame = LabelFrame(main_frame,bg="#fff123",
        text="Worker Details",font=("Times new roman",12,"bold"))
        rightFrame.place(x=760,y=5,width=660,height=430)


        # Right top image
        
        img_Right=Image.open(r"Dependencies\WorkerDet.jpg")
        img_Right=img_Right.resize((660,130), Image.Resampling.LANCZOS) 
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(rightFrame, image=self.photoimg_Right) 
        f_lbl.place(x=0, y=0,width=720,height=130)
        


        # Worker form
        workerFrame = LabelFrame(rightFrame,bg ="white",font=("Times new roman",12,"bold"))
        workerFrame.place(x=0,y=136,width=660,height=250)

        

        

       

        # name

        Name_label=Label(workerFrame, text="Name:", font=("times new roman",13, "bold"),bg="white") 
        Name_label.grid(row=0, column=0, padx=18, pady=5, sticky=W)

        Name_entry=ttk.Entry(workerFrame,textvariable=self.worker_name, width=20, font=("times new roman", 13, "bold"),background= "white") 
        Name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #adhar

        Id_label=Label(workerFrame, text="Aadhar No:", font=("times new roman",13, "bold"),bg="white") 
        Id_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        Id_entry=ttk.Entry(workerFrame,textvariable=self.aadhar, width=20, font=("times new roman",13, "bold"),background= "white") 
        Id_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #radio Buttons
        Gender=Label(workerFrame, text=" gender:", font=("times new roman", 13, "bold"),bg="white") 
        Gender.grid(row=1, column=0, padx=5, pady=5, sticky=W)


        radionbtn1=ttk. Radiobutton (workerFrame, text="Male", value="Yes",variable=self.gender) 
        radionbtn1.grid (row=1, column=1)

        radionbtn2=ttk. Radiobutton (workerFrame, text="Female", value="no",variable=self.gender) 
        radionbtn2.grid (row=2, column=1)




        #Date of birth
        dateofbirth=Label(workerFrame, text="DOB:", font=("times new roman", 13, "bold"),bg="white") 
        dateofbirth.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dateofbirthEntry=ttk. Entry(workerFrame,textvariable=self.date_of_birth,width=20, font=("times new roman", 13, "bold"),background= "white") 
        dateofbirthEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)




        #blood group

        bloodGroup=Label(workerFrame, text="Blood group:", font=("times new roman", 13, "bold"),background= "white") 
        bloodGroup.grid(row=2, column=2, padx=5, pady=5, sticky=W)


        bloodEntry=ttk. Entry(workerFrame,textvariable=self.bloodgroup,width=20, font=("times new roman", 13, "bold"),background= "white") 
        bloodEntry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        #Address
        Address=Label(workerFrame, text="Address:", font=("times new roman", 13, "bold"),bg="white") 
        Address.grid(row=3, column=0, padx=10, pady=5, sticky=W)


        AddressEntry=ttk. Entry(workerFrame,textvariable=self.address,width=20, font=("times new roman", 13, "bold"),background= "white") 
        AddressEntry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #Email
        Email=Label(workerFrame, text="Email:", font=("times new roman", 13, "bold"),bg= "white") 
        Email.grid(row=3, column=2, padx=5, pady=5, sticky=W)


        EmailEntry=ttk. Entry(workerFrame,textvariable=self.email,width=20, font=("times new roman", 13, "bold"),background= "white") 
        EmailEntry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #phone number
        phone=Label(workerFrame, text="Phone no:", font=("times new roman", 13, "bold"),bg="white") 
        phone.grid(row=4, column=0, padx=10, pady=5, sticky=W)


        phoneEntry=ttk. Entry(workerFrame,textvariable=self.phone_no,width=20, font=("times new roman", 13, "bold"),background= "white") 
        phoneEntry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        #City
        City=Label(workerFrame, text="City:", font=("times new roman", 13, "bold"),bg= "white") 
        City.grid(row=4, column=2, padx=10, pady=5, sticky=W)


        CityEntry=ttk. Entry(workerFrame,width=20,textvariable=self.city, font=("times new roman", 13, "bold"),background= "white") 
        CityEntry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


# =======Right Buttons====================================================================

        #Right bbuttons frame

        btn_frame=Frame (rightFrame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place (x=0, y=350, width=660,height=60)

        save_btn=Button (btn_frame,command=self.add_data, text="Save",width=13,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0,padx=10,pady=10)

        updatebtn=Button (btn_frame, text="Update",command=self.update_fun,width=13,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        updatebtn.grid(row=0, column=1,padx=10,pady=10)

        del_btn=Button (btn_frame, text="Delete",command=self.delete_data,width=13,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        del_btn.grid(row=0, column=2,padx=10,pady=10)

        reset_btn=Button (btn_frame, text="Reset",command=self.reset_data,width=13,font=("times New Roman" , 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3,padx=10,pady=10)


#88888 Show All Data Entry Field 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888 

        tableFrame= Frame(BGimg,bd=2,bg="white",relief=RIDGE)
        tableFrame.place(x=5,y=500,width=1460,height=150)


        scroll_x= ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.workerTB=ttk.Treeview(tableFrame,column=("worker_name","aadhar","date_of_birth","gender","bloodgroup","address","email","phone_no","city","worker_category","work_type","register_by","date_of_joining","site_location"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.workerTB.xview)
        scroll_y.config(command=self.workerTB.yview)

    
        self.workerTB.heading("worker_name",text="Name")
        self.workerTB.heading("aadhar",text="Aadhar No")
        self.workerTB.heading("date_of_birth",text="Date of Birth")
        self.workerTB.heading("gender",text="Gender")
        self.workerTB.heading("bloodgroup",text="Blood Group")
        self.workerTB.heading("address",text="Address")
        self.workerTB.heading("email",text="E-mail")
        self.workerTB.heading("phone_no",text="Phone")
        self.workerTB.heading("city",text="City")
        self.workerTB.heading("worker_category",text="Category")
        self.workerTB.heading("work_type",text="Work")
        self.workerTB.heading("register_by",text="Registerd By")
        self.workerTB.heading("date_of_joining",text="Date of Joining")
        self.workerTB.heading("site_location",text="Site Location")
    
        self.workerTB["show"]="headings"
        


        self.workerTB.column("worker_name",width=100,)
        self.workerTB.column("phone_no",width=100)
        self.workerTB.column("email",width=100)
        self.workerTB.column("address",width=100)
        self.workerTB.column("gender",width=100)
        self.workerTB.column("aadhar",width=100)
        self.workerTB.column("city",width=100)
        self.workerTB.column("date_of_birth",width=100)
        self.workerTB.column("bloodgroup",width=100)
        self.workerTB.column("worker_category",width=100)
        self.workerTB.column("work_type",width=100)
        self.workerTB.column("site_location",width=100)
        self.workerTB.column("register_by",width=100)
        self.workerTB.column("date_of_joining",width=100)
        


        self.workerTB.pack(fill=BOTH,expand=1)
        self.workerTB.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


# =======Functions====================================================================================================================

    
    def add_data(self): 
        if self.worker_name.get()=="" or self.aadhar.get() =="" or self.date_of_birth.get() =="" :
            messagebox.showerror("Something is Missing","All Fields are required",parent=self.root)
        else:
            
            try:
                conn=mysql.connector.connect(host="localhost",user="root",database="smart_attendance")
                my_cursor=conn.cursor()
                
                my_cursor.execute("insert into workers values(%s,   %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s)",
                (
                        
                        self.worker_name.get(),
                        self.aadhar.get(),
                        self.date_of_birth.get(),
                        self.gender.get(),
                        self.bloodgroup.get(),
                        self.address.get(),
                        self.email.get(),
                        self.phone_no.get(),
                        self.city.get(),
                        self.worker_category.get(),
                        self.work_type.get(),
                        self.register_by.get(),
                        self.date_of_joining.get(),
                        self.site_location.get(),
                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data Recorded Successfully",parent=self.root)
            
            except Exception as ex :
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)

    def fetch_data(self):
        
        conn=mysql.connector.connect(host="localhost",user="root",database="smart_attendance")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from workers")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.workerTB.delete(*self.workerTB.get_children())
            for i in data:
                self.workerTB.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_focus=self.workerTB.focus()
        content=self.workerTB.item(cursor_focus)
        data=content["values"]

        self.worker_name.set(data[0]),
        self.aadhar.set(data[1]),
        self.date_of_birth.set(data[2]),
        self.gender.set(data[3]),
        self.bloodgroup.set(data[4]),
        self.address.set(data[5]),
        self.email.set(data[6]),
        self.phone_no.set(data[7]),
        self.city.set(data[8]),
        self.worker_category.set(data[9]),
        self.work_type.set(data[10]),
        self.register_by.set(data[11]),
        self.date_of_joining.set(data[12]),
        self.site_location.set(data[13])




    def update_fun(self):
        if self.worker_name.get()=="" or self.city.get() =="" or self.aadhar.get() ==""  or self.phone_no.get()=="" or self.date_of_birth.get()=="":
            messagebox.showerror("Something is Missing","All Fields are required",parent=self.root)
        else:
            try:
                updatem= messagebox.askyesno("update","Are you Surely update this student details",parent=self.root)
                if updatem >0:
                    conn=mysql.connector.connect(host="localhost",user="root",database="smart_attendance")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update workers set worker_name=%s, date_of_birth=%s,gender=%s,bloodgroup=%s,address=%s,email=%s,phone_no=%s,city=%s,worker_category=%s,work_type=%s,register_by=%s,date_of_joining=%s,site_location=%s where aadhar=%s",                 self.worker_name.get(),
                    self.date_of_birth.get(),
                    self.gender.get(),
                    self.bloodgroup.get(),
                    self.address.get(),
                    self.email.get(),
                    self.phone_no.get(),
                    self.city.get(),
                    self.worker_category.get(),
                    self.work_type.get(),
                    self.register_by.get(),
                    self.date_of_joining.get(),
                    self.site_location.get(),
                    self.aadhar.get())
                else:
                    if not updatem:
                        return
                messagebox.showinfo("Success","Student details Successfully updated")
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)







    def delete_data(self):
        if self.aadhar.get()=="":
            messagebox.showerror("Error","Aadhar No. must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student selete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",database="smart_attendance")
                    my_cursor=conn.cursor()
                    sql="delete from workers where aadhar=%s"
                    val= (self.aadhar.get())
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted")
            
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)




    def reset_data(self):
        self.worker_name.set(""),
        self.aadhar.set(""),
        self.date_of_birth.set(""),
        self.gender.set("Male"),
        self.bloodgroup.set(""),
        self.address.set(""),
        self.email.set(""),
        self.phone_no.set(""),
        self.city.set(""),
        self.worker_category.set("Select Category"),
        self.work_type.set("Select Work"),
        self.register_by.set(""),
        self.date_of_joining.set(""),
        self.site_location.set("")     



    def take_pic(self):
        camera = cv2.VideoCapture(0)
        for i in range(1):
            return_value, image = camera.read()
            path='training_images'
            namep=self.worker_name.get()+'.jpg'
            cv2.imwrite(os.path.join(path,namep), image)
        del(camera)
        messagebox.showinfo("Success","Worker Registerd Successfully ")



    def genrate_dataset(self):
        if self.worker_name.get()=="" or self.aadhar.get() =="" or self.bloodgroup.get() ==""  or self.phone_no.get()=="" or self.city.get()=="":
            messagebox.showerror("Something is Missing","All Fields are required",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",user="root",database="smart_attendance")
                my_cursor=conn.cursor()
                myResult=my_cursor.fetchall()
                id=0
                for x in myResult:
                    id+=1
                my_cursor.execute("update workers set worker_name=%s, date_of_birth=%s,gender=%s,bloodgroup=%s,address=%s,email=%s,phone_no=%s,city=%s,worker_category=%s,work_type=%s,register_by=%s,date_of_joining=%s,site_location=%s,photosample=%s where aadhar=%s",(   self.worker_name.get(),
                    self.date_of_birth.get(),
                    self.gender.get(),
                    self.bloodgroup.get(),
                    self.address.get(),
                    self.email.get(),
                    self.phone_no.get(),
                    self.city.get(),
                    self.worker_category.get(),
                    self.work_type.get(),
                    self.register_by.get(),
                    self.date_of_joining.get(),
                    self.site_location.get(),
                    self.aadhar.get(),
                    self.var_id.get()==id+1
                    ))


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #  Face recogmitiom file
                faceClass=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=faceClass.detectMultiScale(gray,1.3,5)
                    #Scaling factor = 1.3
                    #Minimum Neighour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complet!")

             

            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)

    

    

if __name__ == "__main__":
    root = Tk()
    ob =  worker(root)
    root.mainloop()
