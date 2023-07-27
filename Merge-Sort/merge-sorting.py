import random
 
def mergesort(array):
    if len(array) > 1:
        mid = len(array)// 2
        left = array[:mid]
        right = array[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k]= left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
            
def random_list(n):
    random_l = []
    for i in range(n):
        random_l.append(random.randint(1,n))
    return random_l

l = random_list(1000000)
print(l)
#l = [1,64,23,0,10,2]
mergesort(l)
print(l)