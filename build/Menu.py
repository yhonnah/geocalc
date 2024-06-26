
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Arjhay Sebua\Downloads\build\assets\frame0")


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
    184.0,
    31.0,
    anchor="nw",
    text="Geometric Calculator Menu",
    fill="#FCFCFC",
    font=("Roboto Bold", 40 * -1)
)

canvas.create_rectangle(
    88.0,
    98.0,
    774.0,
    103.0,
    fill="#FCFCFC",
    outline="")

canvas.create_rectangle(
    88.0,
    143.0,
    774.0,
    259.0,
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
    x=298.0,
    y=179.0,
    width=267.0,
    height=43.0
)

canvas.create_rectangle(
    88.0,
    313.0,
    774.0,
    429.0,
    fill="#FFFFFF",
    outline="")

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
    x=298.0,
    y=349.0,
    width=267.0,
    height=43.0
)
window.resizable(False, False)
window.mainloop()
