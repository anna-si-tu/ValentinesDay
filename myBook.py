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
        text.config(text = pages[current_page])
        pgNum.config(text=f"Page {current_page + 1} / {len(pages)}")
# Render next page when fnc is called only if another page exists

def prev_page(event = None):
    global current_page
    if current_page > 0:
        current_page -= 1
        text.config(text = pages[current_page])
        pgNum.config(text=f"Page {current_page + 1} / {len(pages)}")

book = tk.Tk()                  # Create a tinker object
book.title("Why I Love You")    # Create title on window popup
book.geometry("1000x600")       # Determine window size

text = tk.Label(
    book,
    text = pages[current_page],
    font = ("Times New Roman", 16),
    wraplength = 550,               # How many pixels are allowed on the line 
                                    # before going to the next line
    justify = "left"                # left-aligned
)
text.pack(expand = True)

pgNum = tk.Label(
    book,
    text = f"Page {current_page + 1} / {len(pages)}",
    font=("Times New Roman", 12),
    justify="right"
)
pgNum.pack(anchor="se", padx=20, pady=10)

# Bind fnc to key buttons
book.bind("<Button-1>", next_page)
book.bind("<Right>", next_page)
book.bind("<Left>", prev_page)
book.focus_set()

book.mainloop()     # Runs application until closed