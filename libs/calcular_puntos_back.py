
import random

def dentro_del_ovalo(x1,x2 ,y1, y2, x, y):
    # centro del ovalo
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    # semiejes
    a, b = (x2 - x1) / 2, (y2 - y1) / 2
    return ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2) <= 1


def calcular_puntos_python(current_value,x1, x2 , y1, y2):
    puntos = []
    puntos_dentro =0
    for _ in range(current_value):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        if dentro_del_ovalo(x1, x2  , y1, y2, x, y):
            puntos.append((x, y, "red"))
            puntos_dentro += 1
        else:
            puntos.append((x, y, "blue"))
    return puntos, puntos_dentro
