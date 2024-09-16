import tkinter as tk
from calcular_puntos import calcular_puntos  # type: ignore


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # inicializo como entero el current value
        self.current_value = tk.IntVar(value=0)
        self.x1, self.y1 = 50, 50
        self.x2, self.y2 = 550, 550
        self.update_id = None
        self.create_widgets()

    def create_widgets(self):
        # creo el Scale o Range
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

        # creo labes para mostrar la informacion
        self.value_label = tk.Label(self, text="Puntos dentro de ovalo: 0")
        self.value_label.pack(side="top")
        self.value_pi = tk.Label(self, text="Numero PI: 0")
        self.value_pi.pack(side="top")

        self.canvas = tk.Canvas(self, width=700, height=580)

        self.canvas.create_oval(self.x1, self.y1, self.x2,
                                self.y2, outline="black", fill="white", width=2)
        self.canvas.pack(side="top")

        # Boton de salir
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    def slider_changed(self, event):
        # Cancelar cualquier actualización programada anterior
        if self.update_id:
            self.after_cancel(self.update_id)
        
        # Programar una nueva actualización
        self.update_id = self.after(100, self.update_canvas)

    def update_canvas(self):
        current_value = self.slice.get()
        self.canvas.delete("punto")
        
        puntos, puntos_dentro = calcular_puntos(
            current_value, self.x1, self.x2, self.y1, self.y2)
            
        
        for x, y, color in puntos:
            self.canvas.create_oval(
                x - 2, y - 2, x + 2, y + 2, fill=color, outline="", tags="punto")

        if current_value > 0:
            pi_estimado = (puntos_dentro / current_value) * \
                4  # Estimación de Pi
        else:
            pi_estimado = 0
        # actualizo el current value
        self.current_value.set(current_value)
        self.value_label.configure(
            text=f'Puntos dentro de ovalo: {puntos_dentro}')
        self.value_pi.configure(text=f'Numero PI: {pi_estimado}')


# creo el main de la aplicacion
root = tk.Tk()
root.geometry("600x750")
root.title("Método de Montecarlo")
app = Application(master=root)
app.mainloop()
