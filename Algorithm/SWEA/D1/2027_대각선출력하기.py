"""
주어진 텍스트를 그대로 출력하세요.
"""

for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end = '')
        else:
            print("+", end = '')
    print() # 줄바꿈