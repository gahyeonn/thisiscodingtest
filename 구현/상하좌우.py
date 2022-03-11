import sys
n = int(input())
arr = list(map(str, sys.stdin.readline().rstrip().split()))
x, y = 1, 1

for i in arr :
  if i == 'R' : x += 1 if x < n else 0 
  elif i == 'L' : x -= 1 if x > 1 else 0 
  elif i == 'U' : y -= 1 if y > 1 else 0 
  elif i == 'D' : y += 1 if y < n else 0
  
print(y, x)