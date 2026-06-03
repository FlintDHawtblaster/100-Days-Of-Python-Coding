import tkinter as tk

window = tk.Tk()
window.title("Guess My Characters")
window.geometry("400x400")

def changeTheImage():
    inputValue = characterInput.get("1.0", "end-1c")
    if inputValue.capitalize().strip() == "Naruto":
        canvas.itemconfig(container, image=image2) 
    elif inputValue.capitalize().strip() == "Sasuke":
        canvas.itemconfig(container, image=image3)
    elif inputValue.capitalize().strip() == "Sakura":
        canvas.itemconfig(container, image=image4)
    elif inputValue.capitalize().strip() == "Kakashi":
        canvas.itemconfig(container, image=image1)
    else:
        tk.Label(text="Can't find the character")

character = tk.Label(text="Guess the character")
character.pack()

characterInput = tk.Text(window, height=1, width=25) 
characterInput.pack()

button = tk.Button(text="Find", command = changeTheImage)
button.pack()

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

image1 = tk.PhotoImage(file="guessWho/Naruto.png")
image2 = tk.PhotoImage(file="guessWho/Sasuke.png")
image3 = tk.PhotoImage(file="guessWho/Sakura.png")
image4 = tk.PhotoImage(file="guessWho/Kakashi.png")

container = canvas.create_image(150,1, image=image1 )

tk.mainloop()