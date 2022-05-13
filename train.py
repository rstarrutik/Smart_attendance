from logging import root
from tkinter import*
from tkinter import ttk
from xml.sax.handler import feature_namespaces
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from tkinter import messagebox


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",15,"bold"))
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Dependencies\FaceDet.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.take_pic,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"Dependencies\FaceDet.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.'[1]))

            faces.append(imageNp)
            ids.append(id)
            cv2.inshow("Training",imageNp)
            cv2.waitkey(1)==13
        ids=np.array(ids)

        #============Train the classifier And save ================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")



    def funtrn(self):
        faceClass=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        id=1
        cap=cv2.VideoCapture (0)
        img_id=0
        while True:
            ret,my_frame=cap.read()
            if self.face_cropped(my_frame) is not None: 
                img_id+=1
                face=cv2.resize(self.face_cropped (my_frame), (450,450)) 
                face=cv2.cvtColor (face, cv2.COLOR_BGR2GRAY)
                file_name_path="data/user."+str(id)+""+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                cv2.imshow("Crooped Face", face)

            if cv2.waitKey(1)==13 or int (img_id)==100:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data Training completed !!!")

    def face_cropped(img):
            faceClass=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceClass.detectMultiScale(gray,1.3,5)
            # scaling factor=1.3
            #Minimum neighbor -5
            for (x,y,w, h) in faces:
                face_cropped=img[y:y+h, x:x+w]
                return face_cropped



    def take_pic(self):
        camera = cv2.VideoCapture(0)
        for i in range(100):
            return_value, image = camera.read()
            path='data'
            namep='user'+str(i)+'.jpg'
            cv2.imwrite(os.path.join(path,namep), image)
            
        del(camera)
        messagebox.showinfo("Success","Training Data Completed Sucessfully")





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()


