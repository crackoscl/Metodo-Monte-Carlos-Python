import tkinter as tk
from libs.calcular_puntos import calcular_puntos

class CanvasWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.x1, self.y1 = 50, 50
        self.x2, self.y2 = 550, 550
        self.canvas = tk.Canvas(self, width=700, height=580)
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black", fill="white", width=2)
        self.canvas.pack(side="top")
        self.puntos_dentro = 0

    def update_canvas(self, current_value):
        self.canvas.delete("punto")
       
        puntos, self.puntos_dentro = calcular_puntos(current_value, self.x1, self.x2, self.y1, self.y2)

        _ = [self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline="",tags="punto") for x, y, color in puntos]
        
        # for x, y, color in puntos:
        #     self.canvas.create_oval(
        #         x - 2, y - 2, x + 2, y + 2, fill=color, outline="", tags="punto"
        #     )

        
