def kth_large(arr,k):
    sortet_arr=[]
    for i in range(len(arr)):
        min_value=min(arr[i+1:])
        sortet_arr.append(min_value)
        if i==len(arr):
            break
    print(sortet_arr)
arr=list(map(int,input().split()))
k=int(input())
res=kth_large(arr,k)
print(res)