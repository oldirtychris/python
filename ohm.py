print("----------------------------------")
print("---------Ohm's Law Calculator-----------")
print("1. Calculate Voltage")
print("2. Calculate Resistance")
print("3. Calculate Current")
print("4. Exit Program")
print("----------------------------------")
option = input("Choose an option (1-4): ")
if (option == "1"):
    print ("-- Calculating Voltage --")
    i = float(input("   Enter the current: "))
    r = float(input("   Enter the resistence: "))
    v = i * r
    print(f"Voltage = {v}")
    
    
elif(option == "2"):
    print ("-- Calculating Resistance --")
    v = float(input("   Enter the voltage: "))
    i = float(input("   Enter the current: "))
    r = v / i
    print(f"Resistance = {r}")
    
elif(option == "3"):
    print ("-- Calculating Current --")
    v = float(input("   Enter the voltage: "))
    r = float(input("   Enter the resistence: "))
    i = v / r
    print(f"Current = {i}")
    
else:
    print("Not an option, Try again")
print("End of Program")
