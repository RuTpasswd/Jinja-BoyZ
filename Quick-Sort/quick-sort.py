import random
import time

def quicksorting(myarray):
    if len(myarray) < 1:
        return myarray
    pivot = myarray[0]
    left_side = []
    right_side = []
    for x in myarray:
        if x < pivot:
            left_side.append(x)
        elif x > pivot:
            right_side.append(x)
    left_side = quicksorting(left_side)
    right_side = quicksorting(right_side)   

    return left_side + [pivot] + right_side

usorterd_list = [2,5,1,60]    
 

def random_list(n):
    random_l = []
    for i in range(n):
        random_l.append(random.randint(1,n))
    return random_l

random_l = random_list(1000000)
print(random_l)
print(quicksorting(random_l))  