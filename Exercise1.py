
temp = float(input("Input temperature: "))

print("Enter 1 if: Celsius to Fahrenheit""\n""Enter 2 if: Fahrenheit to Celsius")
con_type = int(input("Conversion type: "))

if con_type == 1:
    print(f"{temp * 9/5 + 32}ºC")
elif con_type == 2:
    print(f"{(temp - 32) * 5/9}ºC")
