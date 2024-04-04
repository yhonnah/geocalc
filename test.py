import tkinter
import math

root = tkinter.Tk()

root.title('Ractangle')
root.geometry("600x400")
root.configure(bg="white")
root.resizable(0,0)


label_heading = tkinter.Label(root, text="Calculate Area of Ractangle ",bg="white")
label_heading.config(font=("OpenSans", 15))
label_heading.pack()

label_blank1 = tkinter.Label(root,bg="white")
label_blank1.config()
label_blank1.pack()


def ractangle_result():
    num1 = int(side1.get())
    num2 = int(side2.get())
    area = (num1 + num2 ) *2
    label_area.config(text = "Area: "+str(area))


#creating top frame
frame = tkinter.Frame(root,bg="white")
frame.config()
frame.pack()

frameLeft = tkinter.Frame(frame,bg="white")
frameLeft.config()
frameLeft.pack(side=tkinter.LEFT)

label_blank2 = tkinter.Label(frame,bg="white",text="  ")
label_blank2.config()
label_blank2.pack(side=tkinter.LEFT)
        
frameCenter = tkinter.Frame(frame,bg="white")
frameCenter.config()
frameCenter.pack(side=tkinter.LEFT)

label_blank3 = tkinter.Label(frame,bg="white",text="  ")
label_blank3.config()
label_blank3.pack(side=tkinter.LEFT)

frameRight = tkinter.Frame(frame,bg="white")
frameRight.config()
frameRight.pack(side=tkinter.LEFT)

side1= tkinter.StringVar()
side2 = tkinter.StringVar()


#adding controls to left frame
label_left = tkinter.Label(frameLeft, text="Enter side 1:",bg="white")
label_left.config(font=("OpenSans", 15))
label_left.pack()
entry1 = tkinter.Entry(frameLeft, textvariable=side1)
entry1.pack()
        

#Creating Canvas Using Center frame
        
convas = tkinter.Canvas(frameCenter, bg='white', width=150, height=200, bd=0, relief='ridge')
convas.pack()
convas.create_line(20, 20, 20, 180)
convas.create_line(20, 180, 140, 180)
convas.create_line(140, 180,140, 20)
convas.create_line(140, 20,20,20)
        
label_center = tkinter.Label(frameCenter, text="Enter side 2:",bg="white")
label_center.config(font=("OpenSans", 15))
label_center.pack()

entry2 = tkinter.Entry(frameCenter, textvariable=side2)
entry2.pack()

        

#Creating Right Frame for result
        
label_area = tkinter.Label(frameRight, text="Area: ?",bg="white",width = 20)
label_area.config(font=("OpenSans", 15))
label_area.pack()


label_right = tkinter.Button(frameRight, text="Find Result", bg="white",fg="blue",command = ractangle_result)
label_right.config(font=("OpenSans", 15))
label_right.pack(pady = 30)

root.mainloop()