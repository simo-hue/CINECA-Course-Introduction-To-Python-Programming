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