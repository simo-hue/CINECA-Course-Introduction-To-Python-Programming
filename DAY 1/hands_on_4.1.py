import math
import time
res = 150
old_res = 0
soglia = 1e-10
i = 0


def f(x):
    return x**3

def df(x):
    return 3*x**2

start = time.time()
#while abs(res) - old_res > soglia:
#    res -= f(res)/df(res)
#    old_res = res
#    i += 1

while i < 4:
    res -= f(res)/df(res)
    old_res = res
    i += 1
else:
    print("NOT Converged in ", i, " iterations")
    
end = time.time()
print("Elapsed time: ", end - start)
print(res)