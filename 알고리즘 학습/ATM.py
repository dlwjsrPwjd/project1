#https://www.acmicpc.net/problem/11399

def atm_minimum_time():
    # 입력 처리
    N = int(input())  # 사람의 수
    P = list(map(int, input().split()))  # 각 사람이 돈을 인출하는 데 걸리는 시간

    # 오름차순 정렬
    P.sort()

    # 필요한 시간의 합 계산
    total_time = 0
    accumulated_time = 0
    for time in P:
        accumulated_time += time  # 현재 사람까지 기다린 시간
        total_time += accumulated_time  # 총 대기 시간에 추가

    # 결과 출력
    print(total_time)

# 함수 실행
atm_minimum_time()