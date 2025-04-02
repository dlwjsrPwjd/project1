#https://www.acmicpc.net/problem/2562

def main():
    # 9개의 자연수를 입력받음
    numbers = [int(input()) for _ in range(9)]
    
    # 최댓값과 그 위치 찾기
    max_value = max(numbers)
    max_index = numbers.index(max_value) + 1  # 1-based index
    
    # 결과 출력
    print(max_value)
    print(max_index)

if __name__ == "__main__":
    main()