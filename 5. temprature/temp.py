temp=float(input("Enter the temprature:"))
unit=input("Enter the unit:")
if unit=="F":
    celsius=(temp-32)*5/9
    print(f"{temp}°F is equal to {celsius:}°C") 
elif unit=="C":
    fahrenheit=(temp*9/5)+32
    print(f"{temp}°C is equal to {fahrenheit:}°F")
else:
    print("Invalid unit")