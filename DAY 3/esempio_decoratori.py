def max_number_decorator(f):
    def max_number_decorated(*args, **kwargs):
        #print(args, kwargs)
        #print(len(args), len(kwargs))
        
        # Se c'è anche il limite -> 2 argomenti ( args o kwargs )
        if (len(args) > 1 and args[0] < args[1]) or (kwargs.get('nMax') is not None and args[0] < kwargs['nMax']): 
            return f(args[0])
        elif len(args) == 1 and kwargs.get('nMax') is None: # Se c'è solamente il numero -> 1 argomento
            return f(args[0])
        else: # Casi di errore
            if(len(args) > 1):
                raise ValueError(f"Input must be less than {args[1]}.")
            else:
                raise ValueError(f"Input must be less than {kwargs['nMax']}.")
            
    return max_number_decorated

@max_number_decorator
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(f"Fattoriale: {factorial(10)}")