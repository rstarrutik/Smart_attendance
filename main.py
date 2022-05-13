import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from Workers import worker
from train import Train
import facerec as FC
from Attendisp import ShowAttendance as AD
from abtus import AbtUS


class Face_Recognition_System:
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


        #bg image
        img3=Image.open(r"Dependencies\MANREGA01.png")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3) 

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)  

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Worker button
        img4=Image.open(r"Dependencies\WorkerDet.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4) 

        b1=Button(bg_img,image=self.photoimg4,command=self.workerDetails,cursor="hand2")
        b1.place(x=250,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Worker Details",command=self.workerDetails,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=300,width=220,height=40)


        #Detect face button
        img5=Image.open(r"Dependencies\FaceDet.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_img,image=self.photoimg5,command=FC.facrec,cursor="hand2")
        b1.place(x=660,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=FC.facrec,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=660,y=300,width=220,height=40)


        #Attendence  button
        img6=Image.open(r"Dependencies\Attendance.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6) 

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=1050,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",command=self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=300,width=220,height=40)



        # #help  button
        # img7=Image.open(r"Dependencies\Help.png")
        # img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        # self.photoimg7=ImageTk.PhotoImage(img7) 

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b1.place(x=1100,y=100,width=220,height=220)

        # b1_1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=300,width=220,height=40)


        #Train  button
        img8=Image.open(r"Dependencies\FaceTrain.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8) 

        b1=Button(bg_img,image=self.photoimg8,command=self.open_train,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train data",command=self.open_train,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos  button
        img9=Image.open(r"Dependencies\Photos.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9) 

        b1=Button(bg_img,image=self.photoimg9,command=self.open_photos,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_photos,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developer  button
        img10=Image.open(r"Dependencies\AboutUS.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10) 

        b1=Button(bg_img,image=self.photoimg10,command=self.abtopn,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="About Us",cursor="hand2",command=self.abtopn,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)



        #Exit  button
        img11=Image.open(r"Dependencies\exit.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11) 

        b1=Button(bg_img,image=self.photoimg11,command=self.close,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.close,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)


    # Function Define fir buttons
    def workerDetails(self):
        self.new_window=Toplevel(self.root)
        self.app=worker(self.new_window)

    def open_photos(self):
        os.startfile("training_images")

    def close(self):
        win = Tk()
        win.quit()

    
    def open_train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def abtopn(self):
        self.new_window=Toplevel(self.root)
        self.app=AbtUS(self.new_window)
    

    # def faceRecog(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=AD(self.new_window)

if __name__ == "__main__":
    root = Tk()
    ob =  Face_Recognition_System(root)
    root.mainloop()


