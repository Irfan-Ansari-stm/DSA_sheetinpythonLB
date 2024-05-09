def find_duplicate(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
lst = list(map(int,input().split()))
res = find_duplicate(lst)
print(res)