
width = int(input("How many rows?: "))
try:
    if width % 2 != 0:
        for i in range(1, width//2 + 2):
            for j in range(width//2 + 1- i):
                print(" ", end="")
            for k in range(2 * i - 1):
                print("*", end="")
            print()
        for i in range(width//2, 0, -1):
            for j in range(width//2+ 1 - i):
                print(" ", end="")
            for k in range(2 * i - 1):
                print("*", end="")
            print()
    else:
        raise ValueError
except ValueError:
    print("Please provide an odd integer")