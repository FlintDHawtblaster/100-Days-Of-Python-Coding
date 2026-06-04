import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x600")

label = "Guess Who?"

def showImage():
    person = text.get("1.0", "end")
    if person.lower().strip() == "naruto":
        canvas.itemconfig(container, image=naruto)
    elif person.lower().strip() == "sasuke":
        canvas.itemconfig(container, image=sasuke)
    elif person.lower().strip() == "sakura":
        canvas.itemconfig(container, image=sakura)
    elif person.lower().strip() == "kakashi":
        canvas.itemconfig(container, image=kakashi)
    else:
        hello["text"] = "Unable to find this character"
 
hello = tk.Label(text=label)
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command = showImage)
button.pack()

canvas = tk.Canvas(window, width=400, height=500)
canvas.pack()
naruto = ImageTk.PhotoImage(Image.open("guessWho/Naruto.png"))
sasuke = ImageTk.PhotoImage(Image.open("guessWho/Sasuke.png"))
kakashi = ImageTk.PhotoImage(Image.open("guessWho/Kakashi.png"))
sakura = ImageTk.PhotoImage(Image.open("guessWho/Sakura.png"))
container = canvas.create_image(150,1, image=naruto)

tk.mainloop()