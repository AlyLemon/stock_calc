from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("735x500")
root.title("Stock Market Calculator ")


from PIL import Image, ImageTk
# Create a photoimage object of the image in the path
bg=PhotoImage(file="man.png")
l5=Label(root,image=bg)
l5.place(x=0,y=0)
frame1=Frame(root)
frame1.pack(pady=10)

# this is the main code to get the calc to work and the results to show
def orgasmic_calculation():
    global inputtxt, inputtxt2
    user_input=inputtxt.get()
    user_input2=inputtxt2.get()
    result=int(user_input)/int(user_input2)
    result=round(result,2)
    Output1.configure(text=f"${result} USD")

l = Label(text = "What is the Market Cap? ", font=('Arial'))

inputtxt = Entry(root,
                width = 25,
                bg = "pink")

inputtxt.focus_set()

l2 = Label(text = "What is the Circulating Supply?", font=('Arial'))
inputtxt2 = Entry(root,
                width = 25,
                bg = "pink")
inputtxt2.focus_set()

Output1 = Label(root, height = 1, 
              width = 35, 
              bg = "light cyan")


# this is the main code for market cap calc
def market_calculation():
    global inputtxt3, inputtxt4
    user_input3=inputtxt3.get()
    user_input4=inputtxt4.get()
    
    result1=int(user_input3)*int(user_input4)
    result1=round(result1,2)
    Output2.configure(text=f"${result1} USD")

l3 = Label(text = "How many Outstanding Shares? ", font=('Arial'))

inputtxt3 = Entry(root,
                width = 25,
                bg = "pink")

inputtxt3.focus_set()

l4 = Label(text = "What is the Price? ", font=('Arial'))
inputtxt4 = Entry(root,
                width = 25,
                bg = "pink")
inputtxt4.focus_set()

Output2 = Label(root, height = 1, 
              width = 35, 
              bg = "light cyan")

l.pack()
inputtxt.pack()

l2.pack()
inputtxt2.pack()


l3.pack()
inputtxt3.pack()

l4.pack()
inputtxt4.pack()

ttk.Button(root, text="Calculate Market Cap", width=20, command=market_calculation).pack(pady=20)
Output2.pack()

mainloop()
