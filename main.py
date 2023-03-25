import sys
from itertools import combinations

n = int(sys.stdin.readline())

house = list(map(int,sys.stdin.readline().split()))
house.sort()

min_i = -1
min_distance = 1e9
for i in range(n):
  less = house[:i]
  more = house[i+1:]
  distance = house[i]*len(less)-sum(less) + sum(more)-house[i]*len(more)
  print(distance)
  if min_distance > distance:
    min_i = i
    min_distance = distance

print(house[min_i])
  


