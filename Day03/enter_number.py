# 여러 선택지 중 하나를 선택해서 입력받는 while문 만들기
prompt = """
 1. Add
 2. Del
 3. List
 4. Quit

Enter number: 
"""

number = 0

while number != 4:
  print(prompt)
  number = int(input()) # 사용자 입력