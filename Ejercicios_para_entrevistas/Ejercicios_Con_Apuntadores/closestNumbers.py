def closestNumbers(numbers):
    
    numbers.sort()
    minDiff = float('inf')
    result = []
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < minDiff:
            minDiff = diff
            result = [(numbers[i-1], numbers[i])]
        elif diff == minDiff:
            result.append((numbers[i-1], numbers[i]))
    
    return result

numbers = [6,2,4,10]
print(closestNumbers(numbers)) # [(2, 4), (4, 6)]
    
    
    
    