def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements
    
    max1 = max2 = float('-inf')
    
    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    
    return max2 if max2 != float('-inf') else None

# Example
print(second_largest([10, 20, 4, 45, 99]))  # 45
