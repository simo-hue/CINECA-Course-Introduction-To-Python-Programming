with open("DAY 2/times_100m.dat") as f:
    keys = dict()
    keys.keys = f.readline().strip().split("|")
    data = [ [i.strip() for i in line.split("|")] for line in f]

print(data)
# print(type(data))
print("tempo più veloce: ", min(data[0]))
print(f"Atleta più veloce: {min(data)[3]}")