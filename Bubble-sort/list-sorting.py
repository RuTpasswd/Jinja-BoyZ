def sortin():
    lists = [5, 100, 50, 19, 20, 98]
    
    for x in range(len(lists)): 
        for y in range(x+1, len(lists)):
            if (lists[x] > lists[y]):
                swap(x, y, lists)
    return lists
 
def swap(x,y, l):
    temp = l[x]
    l[x] = l[y]
    l[y] = temp
    
print(sortin())