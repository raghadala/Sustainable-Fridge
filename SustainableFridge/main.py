import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import messagebox


window1 = tk.Tk()
window1.title("Sustainable Fridge")
window1.geometry("415x500")
image1=Image.open('closed fridge.png')
img1=image1.resize((418, 495))
my_img1=ImageTk.PhotoImage(img1)
label1=tk.Label(window1, image=my_img1)
label1.place(x=1,y=1)

def onClick():
    messagebox.showinfo(message = "By tracking your food using our sustainable fridge, we can all do our part in reducing food waste! Keep track of the 'roots' we eat!") 
imagel=Image.open('leaf.png')
imgl=imagel.resize((30, 30))
myimg=ImageTk.PhotoImage(imgl)
buttonl=tk.Button(window1,image=myimg,command=onClick)
buttonl.place(x=375,y=10)

def OpenFridge():
  image1=Image.open('openfridge.jpeg')
  # Create window and set fridge background
  window1 = tk.Toplevel()
  window1.title("Input:")
  #window.geometry("415x480")
  img1=image1.resize((418, 490))
  my_img=ImageTk.PhotoImage(img1)
  label=tk.Label(window1, image=my_img)
  label.place(x=1,y=1)

  # Fonts
  titleFont = Font(family="Times New Roman", size=20, weight="bold")
  subHeaderFont = Font(family="Times New Roman", size=13)
  bodyFont = Font(family="Times New Roman", size = 14)
  
  # Create separation for food and days remaining before expiry
  frame = tk.Frame()
  frame.pack(pady=27)
  foodList = tk.Label(text="Food\t   Days Left", font=subHeaderFont)
  foodList.pack()
  
  # Create a frame so we can scroll the list
  frame = tk.Frame()
  frame.pack(pady=2)
  
  # Create a basic list - testing
  food = {"Strawberries":"2", "Oat Milk":"7", "Cream Cheese":"8"}
  
  # Create listbox for food name
  testList1 = Listbox(frame, font=bodyFont, width=13)
  testList1.pack(side=LEFT, fill=BOTH,expand=TRUE)
  
  # Create listbox for expiry date
  testList2 = Listbox(frame, font=bodyFont, width=3)
  testList2.pack(side=LEFT, fill=X, expand=TRUE)

  openfridge_b = tk.Button(window1, text = 'Open Fridge',bg='#D8BFD8', fg='black',command=OpenFridge)  
  openfridge_b.place(x=150,y=110)
  # Add list to list box
  def displayDict():
    for items in food:
      testList1.insert(END, items)
  
    for items in food:
      testList2.insert(END, food[items])
  
    for key, value in food.items() :
      print (key, value)
  
  # Checking if values are added to dictionary properly in terminal
  displayDict()
  
  # Entry function
  enterItem = tk.Entry(window1, font=subHeaderFont)
  enterItem.pack(pady=2)
  
  # Create addItem and deleteItem functions
  def addItem():
    x = enterItem.get().split(",")
    testList1.insert(END, x[0])
    testList2.insert(END,x[1])
    food[x[0]] = x[1]
    enterItem.delete(0,END)
    # Checking that values get added in properly in terminal
    for key, value in food.items() :
      print (key, value)
  
  # Delete selected item - need to delete food and days left separately
  def deleteItem():
    testList1.delete(ANCHOR) 
    testList2.delete(ANCHOR)
  
  def resetFridge():
    testList1.delete(0,END)
    testList2.delete(0,END)
    food.clear();
    print("Fridge Cleared\n")
    
  # Create buttons to add and delete items
  addButton = tk.Button(text="Add Item",command=addItem)
  addButton.place(x=215,y=365)
  delButton = tk.Button(text="Delete Item",command=deleteItem)
  delButton.place(x=113,y=365)
  resetFridge = tk.Button(text="Clear Fridge",command=resetFridge)
  resetFridge.place(x=157,y=397)


# Open fridge button
openfridge_b = tk.Button(window1, text = 'Open Fridge',bg='#D8BFD8', fg='black',command=OpenFridge)  
openfridge_b.place(x=150,y=110)

tk.mainloop()