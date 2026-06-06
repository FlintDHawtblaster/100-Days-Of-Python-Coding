import tkinter as tk

window = tk.Tk()
window.title("Hello There!")
window.geometry("300x300")

#labelOn = True

#def hideLabel():
#    global labelOn
#    if labelOn == True:
#        hello.pack_forget()
#        labelOn = False
#    else:
#        button.pack_forget()
#        hello.pack()
#       button.pack()
#        labelOn = True

def changeImage():
    canvas.itemconfig(container, image=newImage)
    
def hideImage():
    canvas.pack_forget()

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me now!", command = changeImage)
button.pack()
button2 = tk.Button(text="Hide Image", command = hideImage)
button2.pack()

canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()
image = tk.PhotoImage(file="sushiChef.png")
newImage = tk.PhotoImage(file="drone.png")
image = image.subsample(5)
newImage = newImage.subsample(5)
container = canvas.create_image(150,1, image=image)

tk.mainloop()