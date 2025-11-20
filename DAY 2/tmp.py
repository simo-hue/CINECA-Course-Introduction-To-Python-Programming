x = 45
strx = str(x)
print("Il valore di x è " + strx)

for i in range(len(strx)):
    print("Posizione " + str(i) + " : " + strx[i])
    
print(str.find(strx, '5'))

