import time

def file(filname):
    with open(filname, "r") as f:
        for line in f:
            yield line
            
            
z = file("requirements.txt")
print("-------------------- CONTENUTO FILE --------------------")
while True:
    try:
        print(next(z), end="")
    except MemoryError:
        print("errore di memoria")
    except StopIteration:
        break
    
print("---------------------- FINE FILE ----------------------")


va = 800


def fattoriale (n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)
    
t1= time.time()
f1 = 0
try:
    f1 = fattoriale(va)
except RecursionError:
    print("non ce la si fa")
    
t2= time.time()

print(f"""risultato: {f1} con tempo di: {t2-t1}""")

def fattoriale_rec(n, res):
    if n == 0:
        return res
    else:
        return fattoriale_rec(n-1, n*res)

def fattoriale (n):
    if n == 0:
        return 1
    else:
        return fattoriale_rec(n - 1, n) 
    
print(fattoriale(3))
        
t3= time.time()
f1 = fattoriale(va)
t4= time.time()

print(f"""risultato: {f1} con tempo di: {t2-t1}""")
print(f"""\n\n{(t2-t1) < (t4-t3)} | {(t4-t3) - (t2-t1)}""")