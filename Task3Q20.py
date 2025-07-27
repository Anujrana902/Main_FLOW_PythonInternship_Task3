def decimal_to_binary(n):
    
    if n == 0:
        return "0"
    
    bits = []  
    current = n
    
    # keep dividing by 2
    while current > 0:
        remainder = current % 2  
        bits.append(str(remainder))
        current = current // 2
    
    
    bits.reverse()  # reverse 
    binary_string = ''.join(bits)
    return binary_string

# Main 
n = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(n))
