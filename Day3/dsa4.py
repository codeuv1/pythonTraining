def binary_addtion(binary1, binary2):
    num1 = int(binary1,2)
    num2 = int(binary2,2)

    return bin(num1+num2)[2:]

print(binary_addtion('10010','10111'))