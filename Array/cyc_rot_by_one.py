#lets edit by me
def cyc_rot_by_one(arr):
    if len(arr)<=1:
        return arr
    last_ele=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last_ele
    return arr
lst = list(map(int,input().split()))
res=cyc_rot_by_one(lst)
print(res)