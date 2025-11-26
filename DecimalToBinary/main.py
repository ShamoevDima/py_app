num = int(input('Enter number: '))
type = str(input("Enter type (signed / unsigned): "))

if (type == 'unsigned'):
    if (num >= 0):
        binary = bin(num)[2:]
        print(binary)
    else:
        print("Not a valid number")

else:
    if num >= 0:
        binary = bin(num)[2:]
        print(binary)
    else:
        binary = bin((1 << 8) + num)[2:]
        print(binary)
