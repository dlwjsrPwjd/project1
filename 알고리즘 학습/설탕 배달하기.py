#https://www.acmicpc.net/problem/2839

def sugar_delivery(N):
    # 초기 봉지 개수
    bag_count = 0
    
    # 최대한 5kg 봉지를 사용
    while N >= 0:
        if N % 5 == 0:  # 5로 나눠떨어질 경우
            bag_count += N // 5
            print(bag_count)
            return
        N -= 3  # 그렇지 않으면 3kg 봉지를 하나 사용
        bag_count += 1
    
    # 정확히 N킬로그램을 만들 수 없는 경우
    print("X")

# 입력 처리
N = int(input())
sugar_delivery(N)