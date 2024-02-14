import tkinter as tk
from PIL import ImageTk, Image

########## functions ###############################
# Must switch to open fridge screen
def openFridge():
  return 0

# changes back to main title screen
def closeFridge():
  return 0
  
def displayFridge():
  return 0
  
######### beginning of main ##################
  
closescreen = tk.Tk()
#openscreen = tk.Tk()

hello = tk.Label(text="Sustainable Fridge", font = ("Gabriola",20))
hello.pack()

#background image
closescreen.title("Closed Fridge")
closescreen.geometry("450x600")
image=Image.open('closed fridge.png')
img=image.resize((450, 600))
my_img=ImageTk.PhotoImage(img)
label=tk.Label(closescreen, image=my_img)
label.pack()


def switch():
    image = tk.PhotoImage(file = "open fridge.png")
    imageLabel.configure(image = image)
    imageLabel.image = image
frame = tk.Frame(closescreen)
frame.pack()

#buttons displayed on the close fridge screen
openfridge_b = tk.Button(closescreen, text = 'Open Fridge', command=switch,bg='#D8BFD8', fg='black',command=switchToOpen)  
openfridge_b.place(x=160,y=120)

def switchToOpen():
  null
#add_b = tk.Button(openscreen, text='Add Item', command=addItem)
#delete_b = tk.Button(openscreen, text='Delete Item', command=deleteItem)
imageLabel = tk.Label(frame)

closescreen.mainloop()