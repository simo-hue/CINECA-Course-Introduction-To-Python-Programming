a, b = 12, 3
z = complex(a, b)

print("indirizzo di z: ", id(z))
print("parte reale: ", z.real, " che punta a: ", id(z.real))
print("parte immaginaria: ", z.imag, " che punta a: ", id(z.imag))