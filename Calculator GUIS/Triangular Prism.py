
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Arjhay Sebua\Desktop\build\build\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#016938")


canvas = Canvas(
    window,
    bg = "#016938",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    282.0,
    33.0,
    anchor="nw",
    text="Triangular Prism Calculator",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    142.0,
    175.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=46.0,
    y=138.0,
    width=192.0,
    height=72.0
)

canvas.create_text(
    69.0,
    95.0,
    anchor="nw",
    text="Input Length",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    142.0,
    295.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=46.0,
    y=258.0,
    width=192.0,
    height=72.0
)

canvas.create_text(
    81.0,
    215.0,
    anchor="nw",
    text="Input Base",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    720.0,
    175.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=624.0,
    y=138.0,
    width=192.0,
    height=72.0
)

canvas.create_text(
    646.0,
    90.0,
    anchor="nw",
    text="Input Height",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    342.0,
    429.0,
    519.0,
    487.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    757.0,
    25.0,
    825.0,
    64.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=363.0,
    y=436.0,
    width=128.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=757.0,
    y=25.0,
    width=68.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    432.0,
    242.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
