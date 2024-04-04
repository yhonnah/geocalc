
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH / Path(r"build\assets\frame1")
ASSETS_PATH2 = OUTPUT_PATH / Path(r"build\assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)

def openShapesWindow():


    global shapesWindow
    shapesWindow = Tk()

    shapesWindow.geometry("862x519")
    shapesWindow.configure(bg = "#016938")


    canvas = Canvas(
        shapesWindow,
        bg = "#016938",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        324.0,
        38.0,
        anchor="nw",
        text="Please pick a shape",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))
    shape_1 = canvas.create_image(
        431.0,
        146.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        131.0,
        215.0,
        250.0,
        273.0,
        fill="#FFFFFF",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets2("image_2.png"))
    image_2 = canvas.create_image(
        192.0,
        148.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets2("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=147.0,
        y=222.0,
        width=86.0,
        height=43.0
    )

    canvas.create_rectangle(
        131.0,
        417.0,
        250.0,
        475.0,
        fill="#FFFFFF",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets2("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=143.0,
        y=419.0,
        width=95.0,
        height=55.0
    )

    canvas.create_rectangle(
        374.0,
        215.0,
        493.0,
        273.0,
        fill="#FFFFFF",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets2("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=397.0,
        y=222.0,
        width=68.0,
        height=43.0
    )

    canvas.create_rectangle(
        374.0,
        417.0,
        493.0,
        475.0,
        fill="#FFFFFF",
        outline="")

    button_image_4 = PhotoImage(
        file=relative_to_assets2("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=386.0,
        y=425.0,
        width=96.0,
        height=43.0
    )

    canvas.create_rectangle(
        612.0,
        418.0,
        731.0,
        476.0,
        fill="#FFFFFF",
        outline="")

    button_image_5 = PhotoImage(
        file=relative_to_assets2("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=641.0,
        y=425.0,
        width=61.0,
        height=43.0
    )

    canvas.create_rectangle(
        612.0,
        215.0,
        731.0,
        273.0,
        fill="#FFFFFF",
        outline="")

    button_image_6 = PhotoImage(
        file=relative_to_assets2("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=627.0,
        y=222.0,
        width=89.0,
        height=43.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets2("image_3.png"))
    image_3 = canvas.create_image(
        671.0,
        146.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets2("image_4.png"))
    image_4 = canvas.create_image(
        192.0,
        350.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets2("image_5.png"))
    image_5 = canvas.create_image(
        671.0,
        350.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets2("image_6.png"))
    image_6 = canvas.create_image(
        431.0,
        350.0,
        image=image_image_6
    )
    shapesWindow.resizable(False, False)
    shapesWindow.mainloop()

def validateLogin():
    user = entry_1.get() 
    password = entry_2.get()


    try:
        username = float(user)
    
    except:
        canvas.delete("passwrong")
        canvas.delete("userwrong")
        canvas.create_text(
        500.0,
        152.0,
        anchor="nw",
        text="Please input an ID number",
        fill="#FFFFFF",
        font=("Inter", 16 * -1),
        tag = "nouser",
    )

    userid = (((username // 10000000) * 8) + (((username % 10000000) // 1000000) * 7) + (((username % 1000000) // 100000) * 6) + (((username % 100000) // 10000) * 5) + (((username % 10000) // 1000) * 4) + (((username % 1000) // 100) * 3) + (((username % 100) // 10) * 2) + (username % 10)) / 11 
    if userid % 1 == 0:
        usernameValid = 1
    else:
        usernameValid = 0

    if password == "123":
        passwordValid = 1
    else:
        passwordValid = 0

    if passwordValid == 1 and usernameValid == 1:
        print("VALID LOGIN!!")
        canvas.delete("passwrong")
        canvas.delete("nouser")
        canvas.delete("userwrong")
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        openShapesWindow()
        window.destroy()

    elif passwordValid == 1 and usernameValid == 0:
        canvas.delete("passwrong")
        canvas.delete("nouser")
        canvas.create_text(
        500.0,
        152.0,
        anchor="nw",
        text="Please input a valid ID number",
        fill="#FFFFFF",
        font=("Inter", 16 * -1),
        tag = "userwrong"
    )
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END)
    
    elif passwordValid == 0 and usernameValid == 1:
        canvas.delete("userwrong")
        canvas.delete("nouser")
        canvas.create_text(
        570.0,
        300.0,
        anchor="nw",
        text="Incorrect Password",
        fill="#FFFFFF",
        font=("Inter", 16 * -1),
        tag = "passwrong"
    )
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END)

    else:
        canvas.create_text(
        500.0,
        152.0,
        anchor="nw",
        text="Please input a valid ID number",
        fill="#FFFFFF",
        font=("Inter", 16 * -1),
        tag = "userwrong"
    )
        canvas.create_text(
        570.0,
        300.0,
        anchor="nw",
        text="Incorrect Password",
        fill="#FFFFFF",
        font=("Inter", 16 * -1),
        tag = "passwrong"
    )
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END) 

    

        

    

window = Tk()

window.geometry("762x519")
window.configure(bg = "#00381D")


canvas = Canvas(
    window,
    bg = "#00381D",
    height = 519,
    width = 762,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    764.0,
    539.0,
    fill="#016938",
    outline="")

canvas.create_rectangle(
    504.0,
    345.0,
    704.0,
    426.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    58.0,
    32.0,
    anchor="nw",
    text="ID Num",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    58.0,
    32.0,
    anchor="nw",
    text="ID Num",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    381.0,
    118.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=66.0,
    y=81.0,
    width=630.0,
    height=72.0
)

canvas.create_text(
    58.0,
    173.0,
    anchor="nw",
    text="Password\nHINT: 123",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    381.0,
    261.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show = "*"
)
entry_2.place(
    x=66.0,
    y=224.0,
    width=630.0,
    height=72.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    85.0,
    406.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    85.0,
    352.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    141.0,
    352.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    141.0,
    406.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    157.0,
    43.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    157.0,
    186.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validateLogin,
    relief="flat"
)
button_1.place(
    x=579.0,
    y=364.0,
    width=49.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()






