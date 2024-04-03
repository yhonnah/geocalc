
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Yohann\OneDrive - De La Salle University - Manila\DLSU\TERM 2\LBYCPA1\geocalc\geocalc\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    text="User ID",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    58.0,
    32.0,
    anchor="nw",
    text="User ID",
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
    text="Password\n",
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
    highlightthickness=0
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
    command=lambda: print("button_1 clicked"),
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
