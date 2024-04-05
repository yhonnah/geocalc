def coneFormula():
    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer
    # testing tesing

    from main_menu import openShapesWindow
    from pathlib import Path
    from math import pi, sqrt
    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rsebua\Desktop\geocalc\Calculator GUI\build\assets\frame3")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def coneRadius(base, height, radius):
        coneDiameter = radius * 2
        coneArea = (pi * radius) * (radius + sqrt((height ** 2) + (radius ** 2)))
        coneVolume = (pi * (radius ** 2) * height) / 3

        return coneArea, coneVolume, coneDiameter

    # cone given diameter

    def coneDiameter(base, height, diameter):
        coneRadius = diameter / 2
        radius = coneRadius
        coneArea = (pi * radius) * (radius + sqrt((height ** 2) + (radius ** 2)))
        coneVolume = (pi * (radius ** 2) * height) / 3

        return coneArea, coneVolume, coneRadius

    def calculate_cone():
        try:
            # Get the input values from entry widgets
            height = float(entry_2.get())
            radius = float(entry_1.get())
            base = float(entry_3.get())

            # Calculate using coneRadius function
            area, volume, coneDiameter = coneRadius(base, height, radius)

            # Format the results to three decimal points
            area = "{:.3f}".format(area)
            volume = "{:.3f}".format(volume)
            coneDiameter = "{:.3f}".format(coneDiameter)

            # Display the results in the text widget
            result_text = f"Surface Area: {area}\nVolume: {volume}\nCone Diameter: {coneDiameter}"
            result_display.config(state="normal")
            result_display.delete(1.0, "end")
            result_display.insert("end", result_text)
            result_display.config(state="disabled")

        except ValueError:
            # Handle invalid input (non-numeric)
            result_display.config(state="normal")
            result_display.delete(1.0, "end")
            result_display.insert("end", "Invalid input: Please enter a number.")
            result_display.config(state="disabled")

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
        341.0,
        33.0,
        anchor="nw",
        text="Cone Calculator",
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
        text="Input Radius",
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
        72.0,
        215.0,
        anchor="nw",
        text="Input Height",
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
        633.0,
        95.0,
        anchor="nw",
        text="Input Base",
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
        command=calculate_cone,
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
        command=lambda: (window.destroy(), openShapesWindow()),
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
        431.0,
        237.0,
        image=image_image_1
    )

    result_display = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        wrap="word",
        font=("Inter", 13)
    )
    result_display.place(
        x=600,
        y=432.0,
        width=200.0,
        height=58.0
    )

    window.resizable(False, False)
    window.mainloop()
