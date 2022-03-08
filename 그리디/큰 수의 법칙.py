n,m,k = map(int, input().split())
sum = 0
arr = list(map(int, input().split()))
arr.sort()

while m != 0:
  for i in range(k):
    if(m == 0) : break
    sum += arr[n-1]
    m -= 1
  if(m == 0) : break
  sum += arr[n-2]
  m -= 1
  
print(sum)
  
    
    
    
  