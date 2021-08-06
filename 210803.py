# 2007. 패턴 마디의 길이

"""
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
"""

n = int(input())
for i in range(1, n+1):
    text = input()
    for j in range(1, 11):
        if text[:j] == text[j:j*2]:
            print('#' + str(i), j)
            break

# 2005. 파스칼의 삼각형
"""
크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
"""

N = int(input())
for i in range(1, N+1):
    num = int(input())
    