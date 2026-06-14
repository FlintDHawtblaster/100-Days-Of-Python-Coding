import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Visual Novel")
window.geometry("500x300")


story = "You meet a guy at the movie store"

def watchAnime():
    global story
    canvas.itemconfig(container, image=anime)
    story = "He also likes anime"
    storyLabel["text"] = story
    button1.pack_forget()
    button2.pack_forget()
    button3.pack()
    button4.pack()
    
def watchMovies():
    global story
    canvas.itemconfig(container, image=movies)
    story = "He also likes movies"
    storyLabel["text"] = story
    button1.pack_forget()
    button2.pack_forget()
    button5.pack()
    button6.pack()
    
def likeNarutoAnime():
    global story
    canvas.itemconfig(container, image=likeNaruto)
    story = "He also likes Naruto. We talk more about it"
    storyLabel["text"] = story
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()
    
def midNarutoAnime():
    global story
    canvas.itemconfig(container, image=dislikeNaruto)
    story = "He becomes sad"
    storyLabel["text"] = story
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()
    
def watchExpendables():
    global story
    canvas.itemconfig(container, image=expendables)
    story = "He doesn't really like the movie but he recommends me another great movie to watch"
    storyLabel["text"] = story
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()
    
def watchMatrix():
    global story
    canvas.itemconfig(container, image=matrix)
    story = "He really likes the Matrix. We talk about it more it great detail"
    storyLabel["text"] = story
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()
    
def restart():
    global story
    canvas.itemconfig(container, image=anime)
    story = "You meet a guy at the movie store"
    storyLabel["text"] = story
    restartButton.pack_forget()
    button1.pack()
    button2.pack()

generalScene = Image.open("Visualnovel/General.jpg")
originalScene = generalScene.resize((400,200))
start = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1.jpg")
originalScene = generalScene.resize((400,200))
anime = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1a.jpg")
originalScene = generalScene.resize((400,200))
likeNaruto = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene1b.jpg")
originalScene = generalScene.resize((400,200))
dislikeNaruto = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2.jpg")
originalScene = generalScene.resize((400,200))
movies = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2a.jpg")
originalScene = generalScene.resize((400,200))
expendables = ImageTk.PhotoImage(originalScene)
generalScene = Image.open("Visualnovel/Visualscene2b.jpg")
originalScene = generalScene.resize((400,200))
matrix = ImageTk.PhotoImage(originalScene)

canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()
container = canvas.create_image(200, 100, image=start)

storyLabel = tk.Label(text=story)
storyLabel.pack()
button1 = tk.Button(text="Tell him you like anime", command=watchAnime)
button1.pack()
button2 = tk.Button(text="Tell him you like movies", command=watchMovies)
button2.pack()
button3 = tk.Button(text="Tell him you like Naruto", command=likeNarutoAnime)
button4 = tk.Button(text="Tell him that Naruto is mid", command=midNarutoAnime)
button5 = tk.Button(text="Tell him you like The Expendables", command=watchExpendables)
button6 = tk.Button(text="Tell him you like The Matrix", command=watchMatrix)
restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()