import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("300x300")

answer = 0
lastNumber = 0
operator = None

def typeAnswer(value):
    global answer
    answer = f"{answer}{value}"
    answer = int(answer)
    solution["text"] = answer   
    
def calcAnswer(thisOp):
    global answer, lastNumber, operator
    lastNumber = answer
    answer = 0
    
    if thisOp == "+":
        operator = "+"
    elif thisOp == "-":
        operator = "-"
    elif thisOp == "*":
        operator = "*"
    elif thisOp == "/":
        operator = "/"
    
    solution["text"] = answer
        
           
def calc():
    global answer, lastNumber, operator
    print(f"{lastNumber}\t{answer}\t{operator}")
    
    if operator == "+":
        total = lastNumber + answer
    elif operator == "-":
        total = lastNumber - answer
    elif operator == "*":
        total = lastNumber * answer
    elif operator == "/":
        total = lastNumber / answer
        
    answer = total
    solution["text"] = answer

solution = tk.Label(text=answer)
solution.grid(row="2", column="4")

button1 = tk.Button(text="   1   ", command= lambda: typeAnswer(1)).grid(row="3", column="3")
button2 = tk.Button(text="   2   ", command= lambda: typeAnswer(2)).grid(row="3", column="4")
button3 = tk.Button(text="   3   ", command= lambda: typeAnswer(3)).grid(row="3", column="5")
button4 = tk.Button(text="   4   ", command= lambda: typeAnswer(4)).grid(row="4", column="3")
button5 = tk.Button(text="   5   ", command= lambda: typeAnswer(5)).grid(row="4", column="4")
button6 = tk.Button(text="   6   ", command= lambda: typeAnswer(6)).grid(row="4", column="5")
button7 = tk.Button(text="   7   ", command= lambda: typeAnswer(7)).grid(row="5", column="3")
button8 = tk.Button(text="   8   ", command= lambda: typeAnswer(8)).grid(row="5", column="4")
button9 = tk.Button(text="   9   ", command= lambda: typeAnswer(9)).grid(row="5", column="5")
button0 = tk.Button(text="   0   ", command= lambda: typeAnswer(0)).grid(row="6", column="4")
buttonPlus = tk.Button(text="   +   ", command= lambda: calcAnswer("+")).grid(row="3", column="6")
buttonMinus = tk.Button(text="   -   ", command= lambda: calcAnswer("-")).grid(row="3", column="7")
buttonProduct = tk.Button(text="   *   ", command= lambda: calcAnswer("*")).grid(row="4", column="6")
buttonDivide = tk.Button(text="   /   ", command= lambda: calcAnswer("/")).grid(row="4", column="7")
buttonEquals = tk.Button(text="   =   ", command= calc).grid(row="6", column="6")

tk.mainloop()
