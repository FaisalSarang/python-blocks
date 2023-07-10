from tkinter import*
from PIL import ImageTk,Image
import subprocess
root=Tk()
root.title("INFINITY BLOCKS")
root.geometry("816x612")

c=Canvas(root,bg="gray16",height=612,width=816)

bck_end=ImageTk.PhotoImage(file="C:\\Users\\Dell\\Desktop\\Python project\\assets\\python.jpeg")
label_1=Label(root,image=bck_end)
label_1.place(x=0,y=0,relwidth=1,relheight=1)

def run_program():
    subprocess.call(["Python","C:\\Users\\Dell\\Desktop\\Python project\\Minecraft.py"])

#Buttons
button1=Button(root, text="START", bg="black", fg="white", command=run_program)
button1.place(x=250 , y=500)

button2=Button(root, text="EXIT" , bg="black" , fg="white", command=quit)
button2.place(x=500 , y=500)

root.mainloop()