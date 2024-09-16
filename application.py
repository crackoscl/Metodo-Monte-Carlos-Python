import tkinter as tk
from canvas_widget import CanvasWidget

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.current_value = tk.IntVar(value=0)
        self.update_id = None
        self.create_widgets()

    def create_widgets(self):
        self.slice = tk.Scale(
            self,
            from_=0,
            to=100000,
            orient="horizontal",
            command=self.slider_changed,
            width=15,
            length=550
        )
        self.slice.pack(side="top")

        self.value_label = tk.Label(self, text="Puntos dentro de ovalo: 0")
        self.value_label.pack(side="top")
        self.value_pi = tk.Label(self, text="Numero PI: 0")
        self.value_pi.pack(side="top")

        self.canvas_widget = CanvasWidget(self)
        self.canvas_widget.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def slider_changed(self, event):
        if self.update_id:
            self.after_cancel(self.update_id)
        self.update_id = self.after(100, self.update_canvas)

    def update_canvas(self):
        current_value = self.slice.get()
        self.canvas_widget.update_canvas(current_value)

        puntos_dentro = self.canvas_widget.puntos_dentro
        pi_estimado = (puntos_dentro / current_value) * 4 if current_value > 0 else 0
        
        self.value_label.configure(text=f'Puntos dentro de ovalo: {puntos_dentro}')
        self.value_pi.configure(text=f'Numero PI: {pi_estimado}')
