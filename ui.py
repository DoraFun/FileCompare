# Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import main
import glob

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("350x250")

# Define a function to show the popup message
def show_msg():
    directory =  filedialog.askdirectory()
    main.gethash(glob.glob(directory + "/**/*.*", recursive=True))
    # main.gethash(directory + "/*.*")
    main.copies() 
    

# Add an optional Label widget
Label(win, text= "Click button to choose folder", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "Start", command=show_msg).pack(pady= 20)
win.mainloop()

