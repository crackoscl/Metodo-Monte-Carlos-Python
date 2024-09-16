from calcular_puntos_back import calcular_puntos_python
from calcular_puntos import calcular_puntos # type: ignore

import time

x1, y1 = 50, 50
x2, y2 = 550, 550
nsamples = 100000


now_ = time.time()
puntos_ , puntos_dentro_ = calcular_puntos_python(nsamples, x1, x2, y1, y2)
final_ = time.time() - now_

now = time.time()
puntos , puntos_dentro = calcular_puntos(nsamples, x1, x2, y1, y2)
final = time.time() - now


print(puntos_dentro_)
print(f'Python tiempo en seg {final_}')

print(puntos_dentro)
print(f'Cython tiempo en seg {final}')


