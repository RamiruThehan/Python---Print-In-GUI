from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("862x519")
window.configure(bg = "#3A7FF6")

canvas = Canvas(window, bg = "#3A7FF6", height = 519, width = 862, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_rectangle(431.0, 0.0, 862.0, 519.0, fill="#FCFCFC", outline="")
canvas.create_text(58.0, 168.0, anchor="nw", text="Hello!!!!", fill="#FCFCFC", font=("RobotoRoman ExtraBold", 96 * -1))
canvas.create_text(468.0, 168.0, anchor="nw", text="My Name Is \nRamiru.", fill="#000000", font=("RobotoRoman ExtraBold", 64 * -1))
window.resizable(False, False)
window.mainloop()