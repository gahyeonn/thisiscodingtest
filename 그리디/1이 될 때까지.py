n, k = map(int, input().split())

total = 0
while n > 1:
  if n < k : 
    total += n - 1
    break
  else : total += n%k
  
  n //= k 
  total += 1
print(total)
