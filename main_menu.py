def openShapesWindow():

    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer

    from sphere import sphereFormula
    from tri_prism import prismFormula
    from cube import cubeFormula
    from cone import coneFormula
    from cuboid import cuboidFormula
    from cylinder import cylinderFormula
    
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH2 = OUTPUT_PATH / Path(r"build\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH2 / Path(path)


    shapeWindow = Tk()
    shapeWindow.geometry("862x519")
    shapeWindow.configure(bg = "#016938")


    canvas = Canvas(
        shapeWindow,
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
        file=relative_to_assets("shape_1.png"))
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
        file=relative_to_assets("shape_2.png"))
    shape_2 = canvas.create_image(
        192.0,
        148.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:(shapeWindow.destroy(), sphereFormula()),
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
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (shapeWindow.destroy(), prismFormula()),
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
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (shapeWindow.destroy(), cubeFormula()),
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
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (shapeWindow.destroy(), cylinderFormula()),
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
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (shapeWindow.destroy(), coneFormula()),
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
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (shapeWindow.destroy(), cuboidFormula()),
        relief="flat"
    )
    button_6.place(
        x=627.0,
        y=222.0,
        width=89.0,
        height=43.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("shape_3.png"))
    shape_3 = canvas.create_image(
        671.0,
        146.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("shape_4.png"))
    shape_4 = canvas.create_image(
        192.0,
        350.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("shape_5.png"))
    shape_5 = canvas.create_image(
        671.0,
        350.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("shape_6.png"))
    shape_6 = canvas.create_image(
        431.0,
        350.0,
        image=image_image_6
    )
    shapeWindow.resizable(False, False)
    shapeWindow.mainloop()
