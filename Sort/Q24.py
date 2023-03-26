import sys

n = int(sys.stdin.readline())

house = list(map(int,sys.stdin.readline().split()))
house.sort()

print(house[(n-1)//2])
# 1. 계속 풀어보는데 시간초과가 계속 떳다.. 답을 확인했는데 좀 허무했다. 정렬 문제라고 하기에는 좀 어이가 없다는 느낌이 들었다. 뭔가 정렬 문제라고 인식하고 풀어서 그런지 수학적으로 생각하지 못한거 같다. 그래도 딱히 좋은 문제인거 같진 않다.