#https://www.acmicpc.net/problem/11726

def tile_2xn(n):
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1  # 2×1 직사각형을 채우는 방법의 수
    if n > 1:
        dp[2] = 2  # 2×2 직사각형을 채우는 방법의 수
    
    # 점화식: dp[n] = dp[n-1] + dp[n-2]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    
    return dp[n]

# 입력 처리
n = int(input())
print(tile_2xn(n))