number = int(input("Enter a number: "))
type = str(input("Enter a type (signed/unsigned): "))

if type == "signed":
    binary = bin(number)[2:]
elif type == "unsigned":
    if number < 0:
        binary = bin((1 << 8) + number)[2:]
    else:
        binary = bin(number)[2:]
        
print(f"Number: {binary}, Type: {type}")