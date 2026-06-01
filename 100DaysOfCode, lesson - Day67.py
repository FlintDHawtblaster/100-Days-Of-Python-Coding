import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Hello There!")
window.geometry("300x300")

def changeImage():
    canvas.itemconfig(container, image=newImage)

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me now!", command = changeImage)
button.pack()

canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()
image = tk.PhotoImage(file="sushiChef.png")
newImage = tk.PhotoImage(file="drone.png")
image = image.subsample(5)
newImage = newImage.subsample(5)
container = canvas.create_image(150,1, image=image)

tk.mainloop()