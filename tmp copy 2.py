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