from cProfile import label
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
base = tk.Tk()
apps = []

# function to enable a user to add the app of their chossing into a list that will later be ran
def addApp():
       for widget in frame.winfo_children():
              widget.destroy()

       filename= filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
       apps.append(filename)
       for app in apps:
              label = tk.Label(frame, text=app, bg="gray")
              label.pack()
# function that runs the previously mentioned app that were selected.
def runApps():
       for app in apps:
              os.startfile(app)

hello= tk.Canvas(base, height=300, width=300, bg= "#263D42")
hello.pack()

#canvas
canvas = tk.Canvas(root, height=500, width=700, bg="#263D42")
canvas.pack()
#frame to display selected apps 
frame = tk.Frame(root, bg="white")
frame.place(relwidth= 0.8, relheight=0.8, relx=0.1, rely=0.1)
#method to give functoinality to app
openFile = tk.Button(root, text="Open File", padx=5, pady=5, fg="white", bg="black", command=addApp)

openFile.pack()
#method to run apps
runApps = tk.Button(root, text="Run Apps", padx=5, pady=5, fg="white", bg="black", command=runApps)

runApps.pack()
root.mainloop()
