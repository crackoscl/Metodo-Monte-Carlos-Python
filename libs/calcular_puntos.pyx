from libc.stdlib cimport rand, srand, RAND_MAX
from libc.time cimport time

srand(time(NULL))

cpdef int dentro_del_ovalo(int x1, int x2 , int y1, int y2, int x, int y):
    # centro del ovalo
    cdef float cx = (x1 + x2) / 2
    cdef float cy = (y1 + y2) / 2
    # semiejes
    cdef float a = (x2 - x1) / 2
    cdef float b = (y2 - y1) / 2
    return ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2) <= 1

cpdef tuple calcular_puntos(int current_value, int x1, int x2 , int y1, int y2):
    cdef list puntos = []
    cdef int puntos_dentro = 0
    cdef int x , y 

    for _ in range(current_value):
        x = x1 + rand() % (x2 - x1 + 1)
        y = y1 + rand() % (y2 - y1 + 1)

        if dentro_del_ovalo(x1, x2  , y1, y2, x, y):
            puntos.append((x, y, "red"))
            puntos_dentro += 1
        else:
            puntos.append((x, y, "blue"))
    return puntos, puntos_dentro
