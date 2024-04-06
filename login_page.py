from pathlib import Path
from main_menu import openShapesWindow
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH / Path(r"build\assets\frame1")
ASSETS_PATH2 = OUTPUT_PATH / Path(r"build\assets\frame2")

validid = {12313300: 300, 12313378: 378, 123148406: 406}

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)

def validateLogin():
    user = entry_1.get() 
    password = entry_2.get()

    try:
        username = int(user)
        if username in validid:
            usernameValid = 1
        else:
            usernameValid = 0
    
    except ValueError:
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
        return

    if validid.get(username) == int(password):
        print("VALID LOGIN!!")
        canvas.delete("passwrong")
        canvas.delete("nouser")
        canvas.delete("userwrong")
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        window.destroy()
        openShapesWindow()        

    elif usernameValid == 1 and validid.get(username) is None:
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
    
    elif usernameValid == 0:
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
    text="Password\nHINT: Last 3 digits of ID",
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
