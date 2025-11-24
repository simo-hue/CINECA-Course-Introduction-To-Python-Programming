a = list[str]

a = [1, 2, 3, 4, 5, 6, 7]

a_iter = iter(a)

while True:
    try:
        print(a_iter.__next__())
    except:
        print("iteratore finito")
        break
    