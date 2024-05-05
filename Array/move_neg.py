def move_neg(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr.insert(0,arr.pop(i))
        else:
            arr.append(arr.pop(i))
    return arr
lst=list(map(int,input().split()))
res=move_neg(lst)
print(res)

#or

def rearrange(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]<0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1
    print(arr)
arr=[-19,9,-10,9,90,1,-10]
rearrange(arr)