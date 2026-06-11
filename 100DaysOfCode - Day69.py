#I meet a guy
#NOTE: I met a guy at the movie store
#- Tell him you like anime
#NOTE: He also likes anime
#* Tell him I like Naruto
#NOTE: He also loves Naruto. We start talking about it and getting along well 
#* Tell him that Naruto is mid
#NOTE: He becomes sad and we go on our separate ways
#- Tell him you like movies
#NOTE: He also says he likes movies
#* I tell him that I love the Expendables
#NOTE: He tells me that he doesn't like the Expendables but recommends another movie similar to that one
#*I tell him that I love the Matrix
#NOTE: He also loves that too. We start talking about the movie

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Visual Novel")
window.geometry("500x300")

mainLabel = "You meet a guy at the movie store"
label1 = "I also love anime"
label1a = "I also love Naruto. (We start talking about it and get along well)"
label1b = "He becomes really sad."
label2 = "I also love movies"
label2a = "I don't really like the Expendables but I can recommend a better movie"
label2b = "I also love The Matrix (We start talking more about it)"
option1text = "Tell him you like anime"
option1text1 = "Tell him that I love Naruto"
option1text2 = "Tell him that Naruto is mid"
option2text = "Tell him you like movies"
option2text1 = "Tell him that I love The Expendables"
option2text2 = "Tell him that I love The Matrix"
label = mainLabel

def nextOption1():
    global label
    
    if label == mainLabel:       
        canvas.itemconfig(container, image=scene1)
        canvas.pack()
        option1["text"] = option1text1
        option2["text"] = option1text2
        novelConv["text"] = label1
        label = label1
    elif label == label1:
        canvas.itemconfig(container, image=scene3)
        novelConv["text"] = label1a
        option1.pack_forget()
        option2.pack_forget()
        restartScenes.pack()
    elif label == label2:
        canvas.itemconfig(container, image=scene5)
        novelConv["text"] = label2a
        option1.pack_forget()
        option2.pack_forget() 
        restartScenes.pack()
        
    return label
    
def nextOption2():
    global label
    
    if label == mainLabel:       
        canvas.itemconfig(container, image=scene2)
        canvas.pack()
        option1["text"] = option2text1
        option2["text"] = option2text2
        novelConv["text"] = label2
        label = label2
    elif label == label1:
        canvas.itemconfig(container, image=scene4)
        novelConv["text"] = label1b
        option1.pack_forget()
        option2.pack_forget()
        restartScenes.pack()
    elif label == label2:
        canvas.itemconfig(container, image=scene6)
        novelConv["text"] = label2b
        option1.pack_forget()
        option2.pack_forget()
        restartScenes.pack()
     
    return label

def restart():
    global label
    canvas.itemconfig(container, image=mainscene)
    novelConv["text"] = mainLabel
    option1["text"] = option1text
    option1.pack()
    option2["text"] = option2text
    option2.pack()
    label = mainLabel
    restartScenes.pack_forget()
    

generalScene = Image.open("Visualnovel/General.jpg")
originalScene = generalScene.resize((400,200))
mainscene = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1.jpg")
originalScene = generalScene.resize((400,200))
scene1 = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2.jpg")
originalScene = generalScene.resize((400,200))
scene2 = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1a.jpg")
originalScene = generalScene.resize((400,200))
scene3 = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1b.jpg")
originalScene = generalScene.resize((400,200))
scene4 = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2a.jpg")
originalScene = generalScene.resize((400,200))
scene5 = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2b.jpg")
originalScene = generalScene.resize((400,200))
scene6 = ImageTk.PhotoImage(originalScene)

canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

container = canvas.create_image(200,100, image=mainscene) 

novelConv = tk.Label(text=mainLabel)
novelConv.pack()

option1 = tk.Button(text=option1text, command = nextOption1)
option1.pack()
option2 = tk.Button(text=option2text, command = nextOption2)
option2.pack()
restartScenes = tk.Button(text="Restart", command = restart)

tk.mainloop()

