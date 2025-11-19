import math
import time
import sys

def super_square_recursive(x):
    if(x == 0):
        return math.sqrt(30)
    else:
        return math.sqrt(30 + super_square_recursive(x - 1))
   
   
def super_square_iterative(x):
    risultato = math.sqrt(30)
    
    i = 0
    while i < x:
        risultato = math.sqrt(30 + risultato) 
        i += 1
    return risultato

n = int(input("Inserisci un numero intero: "))
recursive_time = None

if n > 0: 
    # ITERATIVO
    print("\n\nMetodo Iterativo:")
    start = time.time()     
    risultato = super_square_iterative(n)
    print("Il risultato è:", risultato)
    end = time.time()
    iterative_time = end - start
    print("Tempo di esecuzione:", end - start, "secondi")
    
    # RICORSIVO
    print("\n\nMetodo Ricorsivo:")
    try:
        start = time.time()     
        risultato = super_square_recursive(n)
        print("Il risultato è:", risultato)
        end = time.time()
        recursive_time = end - start
        print("Tempo di esecuzione:", end - start, "secondi")
    except RecursionError:
        print("Errore: il numero inserito è troppo grande per la ricorsione.")

    print("\n\nMetodo iterativo è più veloce? ", recursive_time is None or iterative_time < recursive_time)
else:
    print("Per favore, inserisci un numero intero positivo.")
        