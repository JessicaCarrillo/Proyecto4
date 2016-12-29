import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
my_image=PhotoImage(file="LeanaJek.png")
canvas.create_image(0,0,anchor=NW,image=my_image)

for x in range(0, 60):
   canvas.move(1, 5, 0)
   tk.update()
   time.sleep(0.05)

for x in range(0, 60):
   canvas.move(1, -2, 2)
   tk.update()
   time.sleep(0.05)

for x in range(0, 35):
   canvas.move(1, -5, -2)
   tk.update()
   time.sleep(0.05)
 
tk.mainloop()
