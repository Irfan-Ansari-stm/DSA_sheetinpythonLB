#first way
def union(arr1,arr2):
    return set(arr1)|set(arr2)
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
res=list(union(a1,a2))
print(res)

#second way
def union1(a1,a2):
    union_arr=[]
    for i in a1:
        if i not in union_arr:
            union_arr.append(i)
    for j in a2:
        if j not in union_arr:
            union_arr.append(j)
    return union_arr
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
res1 = union1(lst1,lst2)
print(res1)