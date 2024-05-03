def rev_arr(arr):
    rev=[]
    for i in range(1,len(arr)+1):
        rev.append(arr[-i])
    return rev
lst=list(map(int,input().split()))
res=rev_arr(lst)
print(res)