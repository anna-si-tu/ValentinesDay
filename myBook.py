import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

# pip install pillow
# pip install pyinstaller

# Test pages
# pages = [
#     "First Page",
#     "Second Page",
#     "Third Page"
# ]

def resource_path(relative_path):   # Install as an executable
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Put personal book.txt in the same directory
with open("data/sample.txt") as f:    # Change name as necessary
    pages = f.read().split("\n\n---\n\n")

current_page = 0                # Current page is instantiated to 0

def next_page(event=None):      # Create a function for the next page
    global current_page         # Use variable existing outside of fnc
    if current_page < len(pages) - 1:
        current_page += 1
        canvas.itemconfig(text_id, text=pages[current_page])
        canvas.itemconfig(pgNum, text = f"{current_page + 1} / {len(pages)}")
# Render next page when fnc is called only if another page exists

def prev_page(event=None):
    global current_page
    if current_page > 0:
        current_page -= 1
        canvas.itemconfig(text_id, text = pages[current_page])
        canvas.itemconfig(pgNum, text = f"{current_page + 1} / {len(pages)}")


book = tk.Tk()                  # Create a tinker object
book.title("Why I Love You")    # Create title on window popup
book.geometry("1000x600")       # Determine window size

canvas = tk.Canvas(book, width = 1000, height = 600, highlightthickness = 0)
canvas.pack(fill = "both", expand = True)

bg_img = Image.open("data/bookBG.png")  # Add background image here
bg_img = bg_img.resize((1000, 600))
bg_photo = ImageTk.PhotoImage(bg_img)

canvas.create_image(0, 0, image = bg_photo, anchor = "nw") # Never close bg

text_id = canvas.create_text(
    510, 275,                    # Center
    text = pages[current_page],
    font = ("Times New Roman", 15),
    fill = "black",
    width = 510,
    anchor = "center"
)

pgNum = canvas.create_text(
    970, 580,                    # Bottom right
    text = f"{current_page + 1} / {len(pages)}",
    font = ("Times New Roman", 12),
    fill = "black",
    width = 50,
    anchor = "se"
)

# Bind fnc to key buttons
book.bind("<Button-1>", next_page)
book.bind("<Right>", next_page)
book.bind("<Left>", prev_page)
book.focus_set()

book.mainloop()     # Runs application until closed