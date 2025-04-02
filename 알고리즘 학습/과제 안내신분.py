#https://www.acmicpc.net/problem/5597

def find_missing_students(submitted_students):
    all_students = set(range(1, 31))  # 1번부터 30번까지의 출석번호
    missing_students = sorted(all_students - submitted_students)  # 제출 안 한 학생 찾기
    return missing_students

# 제출한 학생들의 출석번호를 입력받음
submitted_students = {int(input()) for _ in range(28)}

# 결과 출력
missing = find_missing_students(submitted_students)
print(missing[0])
print(missing[1])