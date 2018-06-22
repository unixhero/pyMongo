from Connection import *
from tkinter import *

root = Tk()

label = Label(root, text="Überschrift")

root.mainloop()

# GUI tkinter
# .....
# Live-DB
#

db = Connection()
db.getdocuments('Trump')
