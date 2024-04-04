
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Arjhay Sebua\Downloads\build\assets\frame3")


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
canvas.create_rectangle(
    43.0,
    61.0,
    282.0,
    154.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    306.0,
    61.0,
    545.0,
    154.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    574.0,
    61.0,
    813.0,
    154.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    574.0,
    61.0,
    813.0,
    154.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    45.0,
    174.0,
    284.0,
    267.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    308.0,
    174.0,
    547.0,
    267.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    576.0,
    174.0,
    815.0,
    267.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    46.0,
    279.0,
    285.0,
    372.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    309.0,
    279.0,
    548.0,
    372.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    577.0,
    279.0,
    816.0,
    372.0,
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
    x=73.0,
    y=71.0,
    width=178.0,
    height=72.0
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
    x=338.0,
    y=71.0,
    width=178.0,
    height=72.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=595.0,
    y=71.0,
    width=191.0,
    height=72.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=71.0,
    y=197.0,
    width=189.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=341.0,
    y=192.0,
    width=178.0,
    height=47.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=586.0,
    y=174.0,
    width=218.0,
    height=93.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=71.0,
    y=297.0,
    width=189.0,
    height=47.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=331.0,
    y=297.0,
    width=197.0,
    height=47.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=576.0,
    y=290.0,
    width=238.0,
    height=71.0
)

canvas.create_rectangle(
    43.0,
    385.0,
    283.0,
    478.0,
    fill="#FFFFFF",
    outline="")

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=107.0,
    y=397.0,
    width=111.0,
    height=70.0
)

canvas.create_rectangle(
    311.0,
    385.0,
    551.0,
    478.0,
    fill="#FFFFFF",
    outline="")

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=342.0,
    y=396.0,
    width=178.0,
    height=72.0
)

canvas.create_rectangle(
    575.0,
    385.0,
    815.0,
    478.0,
    fill="#FFFFFF",
    outline="")

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=599.0,
    y=396.0,
    width=192.0,
    height=71.0
)

canvas.create_text(
    384.0,
    20.0,
    anchor="nw",
    text="Pick a Formula",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()