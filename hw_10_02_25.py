#kth largest element
arr=list(map(int, input().split())) 
k=int(input()) 
arr.sort(reverse=True) 
print(arr[k-1])

#kth element without sort
arr=list(map(int, input().split()))
k=int(input())
for _ in range(k-1):
    max_val=max(arr)
    arr.remove(max_val)  # Remove only one occurrence of the max value
print(max(arr))  # The k-th largest element


#Check if a num is a disarium number
num=int(input()) 
digits=list(map(int, str(num))) 
disarium_sum=sum(d **(i+1) for i,d in enumerate(digits)) 
if disarium_sum == num: 
print("Disarium Number") 
else: 
print("Not a Disarium Number")
