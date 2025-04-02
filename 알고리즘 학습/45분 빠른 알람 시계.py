#https://www.acmicpc.net/problem/2884

def main():
    # 현재 설정된 알람 시간 입력받기
    H, M = map(int, input().split())
    
    # 45분 빼기
    M -= 45
    if M < 0:  # 분이 음수가 되면
        M += 60  # 분에 60을 더하고
        H -= 1   # 시간을 1 감소
        if H < 0:  # 시간이 음수가 되면
            H += 24  # 시간을 24로 순환
    
    # 결과 출력
    print(H, M)

if __name__ == "__main__":
    main()