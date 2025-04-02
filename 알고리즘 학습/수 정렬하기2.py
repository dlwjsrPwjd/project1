#https://www.acmicpc.net/problem/2751
import sys

def main():
    # 입력 처리
    N = int(sys.stdin.readline().strip())
    numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
    
    # 오름차순 정렬
    numbers.sort()
    
    # 결과 출력
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()