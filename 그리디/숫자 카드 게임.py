n, m = map(int, input().split())
maxt = 0
for i in range(n) :
  mina = min(map(int, list(map(int, input().split()))))
  maxt = max(maxt, mina)
print(maxt)
