#https://www.acmicpc.net/problem/2869
from math import ceil

# 입력 처리
A, B, V = map(int, input().split())

# 정상에 도달하기 위해 필요한 일수 계산
days = ceil((V - A) / (A - B)) + 1

# 결과 출력
print(days)