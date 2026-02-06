temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    result = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", result)
elif unit == "F":
    result = (temp - 32) * 5/9
    print("Temperature in Celsius:", result)
else:
    print("Invalid unit")
