def solution(list1, list2,m, n):
    
    i = m-1 #ultima posicion de la lista 1
    j=n-1   #ultima posicion de la lista 2
    k = m+n-1 #ultima posicion de la lista 1 + lista 2
    
    while i >= 0 and j >= 0: #mientras i y j sean mayores o iguales a 0
        if list1[i] > list2[j]: #si el elemento de la lista 1 es mayor al de la lista 2
            list1[k] = list1[i] #el elemento de la lista 1 en la posicion k sera igual al elemento de la lista 1 en la posicion i
            i -= 1 #decrementamos i
        else: #si no
            list1[k] = list2[j] #el elemento de la lista 1 en la posicion k sera igual al elemento de la lista 2 en la posicion j
            j -= 1 #decrementamos j
        k -= 1  #decrementamos k
    

    while j >= 0: #mientras j sea mayor o igual a 0
        list1[k] = list2[j] #el elemento de la lista 1 en la posicion k sera igual al elemento de la lista 2 en la posicion j
        j -= 1 #decrementamos j
        k -= 1 #decrementamos k
    
    return list1 #retornamos la lista 1
          

    
list1 = [1,2,3,0,0,0]
m=3
list2 = [-4,5,6]
n=3 

print(solution(list1, list2, m, n)) # [1,2,2,3,5,6] 