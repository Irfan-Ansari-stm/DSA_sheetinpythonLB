def merge2sortedlist(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    arr1.extend([None]*n)
    i,j,k=m-1,n-1,m+n-1
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            arr1[k]=arr2[j]
            i-=1
        else:
            arr1[k]=arr2[j]
            j-=1
        k-=1
    while j>=0:
        arr1[k]=arr2[j]
        j-=1
        k-=1

lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
merge2sortedlist(lst1,lst2)
print(lst1)