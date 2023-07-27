import random


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[left] > array[largest]:
       largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array,n,largest)

def heapsort(arr):
    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)
        
       
def random_list(n):
    random_l = []
    for i in range(n):
        random_l.append(random.randint(1,n))
    return random_l

l = random_list(1000)
print(l)
#l = [1,64,23,0,10,2]
heapsort(l)
print(l)

