"""Practice with if-then-esle statements."""

choice: int = int(input("Enter a number: "))

# Inplement this logic
# A when < 25
# B when >= 25 and < 50
# C when > 75
# D when >= 50 and <= 75
if choice < 25: 
    print("A")
else: 
    if choice < 50:
        print("B")
    else: 
        if choice > 75:
            print("C")
        else:
            print("D")





