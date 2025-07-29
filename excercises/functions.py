def c_to_f(celsius):
    return (celsius * 9/5) + 32

print("Celsius to Fahrenheit Conversion")
celsius = (input("Enter temperature in Celsius: "))
print(celsius, "Celsius is ", c_to_f(int(celsius)), "Fahrenheit")
