def intersection(arr1,arr2):
    intersection_arr=[]
    for i in arr1:
        if i in arr2:
            intersection_arr.append(i)
    return intersection_arr
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
res = intersection(lst1,lst2)
print(res)