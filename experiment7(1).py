def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

seq = [10, 6, 8, 90, 12, 56]
mx, mn = find_max_min(seq)
print(f"Maximum: {mx}, Minimum: {mn}")