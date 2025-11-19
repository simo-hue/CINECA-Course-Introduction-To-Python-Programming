import math

l1 = float(input("Enter a number: "))
l2 = float(input("Enter a number: "))
l3 = float(input("Enter a number: "))

def calculate_area(l1, l2, l3):
    if(l1 <= 0 or l2 <= 0 or l3 <= 0):
        print("Error: lengths must be positive numbers.")
        return None
    elif (l1 + l2 <= l3) or (l1 + l3 <= l2) or (l2 + l3 <= l1):
        print("Error: the lengths do not form a valid triangle.")
        return None
    else:
        p = (l1 + l2 + l3) / 2
        return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))

result = calculate_area(l1, l2, l3)

if result:
    print("Il risultato completo è:", result)

    if type(result) == float or type(result) == float:
        print("Il risultato Approssimato è:", round(number=result, ndigits=2))
        print("Il risultato parziale ( INT ) è:", int(result))
        