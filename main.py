import tkinter as tk
from application import Application

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x750")
    root.title("Método de Montecarlo")
    app = Application(master=root)
    app.mainloop()

