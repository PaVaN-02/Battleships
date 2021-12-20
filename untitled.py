import tkinter as tk
def draw(canvas):
    pass
def makecanvas(w,h):
    root = tk.Tk()
    canvas = tk.Canvas(root,width=w,height=h)
    canvas.create_oval(10, 50, 110, 100,fill="#FF69B4",width=7)
    canvas.pack()
    draw(canvas)
    root.mainloop()
makecanvas(400,400)
