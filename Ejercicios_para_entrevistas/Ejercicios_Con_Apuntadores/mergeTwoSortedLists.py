def solution(list1, list2, m, n):
    i = m - 1  # Last position of the valid elements in list1
    j = n - 1  # Last position of the elements in list2
    k = m + n - 1  # Last position of the merged list (list1 + list2)
    
    # While there are elements to compare in both lists
    while i >= 0 and j >= 0: 
        if list1[i] > list2[j]:  # If the current element in list1 is greater than in list2
            list1[k] = list1[i]  # Place the larger element at position k in list1
            i -= 1  # Move the pointer in list1 backward
        else:  # If the current element in list2 is greater or equal
            list1[k] = list2[j]  # Place the element from list2 at position k in list1
            j -= 1  # Move the pointer in list2 backward
        k -= 1  # Move the merged pointer backward
    
    # If there are remaining elements in list2, add them to list1
    while j >= 0: 
        list1[k] = list2[j]  # Copy elements from list2 to list1
        j -= 1  # Move the pointer in list2 backward
        k -= 1  # Move the merged pointer backward
    
    return list1  # Return the merged and sorted list

# Example input
list1 = [1, 2, 3, 0, 0, 0]  # Array with space for merging
m = 3  # Number of valid elements in list1
list2 = [-4, 5, 6]  # Second sorted list
n = 3  # Number of elements in list2

print(solution(list1, list2, m, n))  # Expected output: [-4, 1, 2, 3, 5, 6]
 