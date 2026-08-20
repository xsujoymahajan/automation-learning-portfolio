import math
temperature = float(input("Temperature: "))
if math.ceil(temperature) >= 30:
    print("Fan: ON")
elif math.floor(temperature) <= 27:
    print("Fan: OFF")
