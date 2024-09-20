
while True:
    try:
        print("V for Voltage \n""I for current \n""R for Resistance")
        ask = input("What do you want to calculate?: ")
        if ask.upper() == "V":
            crrnt = float(input("What is the Current(I)?: "))
            resist = float(input("what is the Resistance(R)?: "))
            print(f"Voltage: {crrnt * resist}V")
        elif ask.upper() == "I":
            volt = float(input("What is the Voltage(V)?: "))
            resist = float(input("What is the Resistance(R)?: "))
            print(f"Current: {volt/resist}A")
        elif ask.upper() == "R":
            volt = float(input("What is the Voltage(V)?: "))
            crrnt = float(input("what is the Current(I)?: "))
            print(f"Resistance: {volt/crrnt}Ω")
        break
    except ZeroDivisionError:
        print(("Error Detected: Division by zero \n"))