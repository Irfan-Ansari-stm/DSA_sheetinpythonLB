def max_min(arr):
    max=arr[0]
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        if arr[i]<min:
            min=arr[i]
    return min,max

arr=list(map(int,input().split()))
res=max_min(arr)
print("Minimum",res[0],"and","Maximum",res[1])