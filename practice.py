N, M = map(int, input().split())
tot = 0
price = []

for i in range(M):
  price.append(list(map(int, input().split())))

  price_six = sorted(price)
  price_one = sorted(price, key=lambda x:x[1])

print(price_one)
print(price_six)

while i < N:
  if price_six[0][0] <= price_one[0][1] * 6:
      tot = price_one[0][1] * N
  else:
    if N < 6:
      tot = price_one[0][1] * N
    else:
      tot = price_six[0][0] * (N//6) + price_one[0][1] * (N%6)
  i=i+1
print(tot)