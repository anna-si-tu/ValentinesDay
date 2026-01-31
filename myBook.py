import tkinter as tk

# Test pages
# pages = [
#     "First Page",
#     "Second Page",
#     "Third Page"
# ]

# Put personal book.txt in the same directory
with open("book.txt") as f:     # Change name as necessary
    pages = f.read().split("\n\n---\n\n")

current_page = 0                # Current page is instantiated to 0

def next_page(event = None):    # Create a function for the next page
    global current_page         # Use variable existing outside of fnc
    if current_page < len(pages) - 1:
        current_page += 1
        label.config(text = pages[current_page])
# Render next page when fnc is called only if another page exists

def prev_page(event = None):
    global current_page
    if current_page > 0:
        current_page -= 1
        label.config(text=pages[current_page])

book = tk.Tk()                  # Create a tinker object
book.title("Why I Love You")    # Create title on window popup
book.geometry("1000x600")       # Determine window size

label = tk.Label(
    book,
    text = pages[current_page],
    font = ("Times New Roman", 16),
    wraplength = 550,               # How many pixels are allowed on the line 
                                    # before going to the next line
    justify = "left"                # left-aligned
)
label.pack(expand = True)

# Bind fnc to key buttons
book.bind("<Button-1>", next_page)
book.bind("<Right>", next_page)
book.bind("<Left>", prev_page)

book.mainloop()     # Runs application until closed