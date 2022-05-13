import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
# from workers import worker
# from train import Train
# from FaceRecog import Face_Recognition


class AbtUS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")

        self.root.title("MGNREGA Attendance System")
        img=Image.open(r"Dependencies\MPimg.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)   


        img1=Image.open(r"Dependencies\MPimg1.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=500,height=130) 


        img2=Image.open(r"Dependencies\MPimg2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2) 

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=500,height=130) 
        

        title_lbl=Label(self.root,text="About  US",font=("cambria math",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=150,width=1530,height=50)

# 23333333333 Left Frame  3333333333322222222222222222222222222222222222222222222222222222


        leftFrame = LabelFrame(self.root,bg="#fff123", relief=RIDGE,font=("Times new roman",12,"bold"))
        leftFrame.place(x=40,y=205,width=660,height=600)

        rut=Image.open(r"Dependencies\rutik.jpg")
        rut=rut.resize((250,250),Image.Resampling.LANCZOS)
        self.photorut=ImageTk.PhotoImage(rut) 

        f_lbl=Label(leftFrame,image=self.photorut)
        f_lbl.place(x=20,y=20,width=250,height=250) 

        Rut_Lab=Label(leftFrame, text="Rutik Mahurkar", font=("cambria math",30, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        Rut_Lab.place(x=300,y=0)

        Rut_Lab=Label(leftFrame, text="rutik.rstar@gmail.com", font=("cambria math",15, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        Rut_Lab.place(x=320,y=180)




        sam=Image.open(r"Dependencies\My photo.jpg")
        sam=sam.resize((250,250),Image.Resampling.LANCZOS)
        self.photosam=ImageTk.PhotoImage(sam) 

        f_lbl=Label(leftFrame,image=self.photosam)
        f_lbl.place(x=20,y=300,width=250,height=250) 


        samlab=Label(leftFrame, text="Samadhan Bhoi", font=("cambria math",30, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        samlab.place(x=300,y=250)

        samlab=Label(leftFrame, text="samadhanbhoi98@gmail.com", font=("cambria math",15, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        samlab.place(x=320,y=430)







        rightFrame = LabelFrame(self.root,bg="#fff123", relief=RIDGE,font=("Times new roman",12,"bold"))
        rightFrame.place(x=830,y=205,width=660,height=600)


        Hem=Image.open(r"Dependencies\My photo.jpg")
        Hem=Hem.resize((250,250),Image.Resampling.LANCZOS)
        self.photohem=ImageTk.PhotoImage(Hem) 

        f_lbl=Label(rightFrame,image=self.photohem)
        f_lbl.place(x=390,y=20,width=250,height=250) 

        hemi_Lab=Label(rightFrame, text="Hemlata Tak", font=("cambria math",30, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        hemi_Lab.place(x=20,y=0)

        hemi_Lab=Label(rightFrame, text="hemlatatak16@gmail.com", font=("cambria math",15, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        hemi_Lab.place(x=20,y=180)



        gauri=Image.open(r"Dependencies\My photo.jpg")
        gauri=sam.resize((250,250),Image.Resampling.LANCZOS)
        self.photogauri=ImageTk.PhotoImage(gauri) 

        f_lbl=Label(rightFrame,image=self.photogauri)
        f_lbl.place(x=390,y=300,width=250,height=250) 


        gaurilab=Label(rightFrame, text="Gauri Mundada", font=("cambria math",30, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        gaurilab.place(x=20,y=250)

        gaurilab=Label(rightFrame, text="gaurirajput2608@gmail.com", font=("cambria math",15, "bold"),bg="#fff123",fg="blue") # textvariable=self.var_dep,``
        gaurilab.place(x=20,y=430)



        dd=Label(self.root, text="Special Thanks To Our Project Guide D. D. Puri Sir ", font=("times new roman",25, "bold"),bg="#fff123",fg="red") # textvariable=self.var_dep,``
        dd.place(x=400,y=745)




        
if __name__ == "__main__":
    root = Tk()
    ob =  AbtUS(root)
    root.mainloop()
