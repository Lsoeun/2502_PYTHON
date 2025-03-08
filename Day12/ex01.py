# 상수 만들기
# 상수란? 한번 정하면 변경하지 않는 값
# 관습적으로 대문자로 선언하며, 변경하지 않는다는 규칙이 있음
# 상수를 강제하는 문법이 없으므로, 개발자가 값을 변경하지 않는다는 규칙을 잘 지켜야 함

MIN = 60
SEC = 60

# 매개변수로 시간이 들어오면 분 단위로 변환하여 반환
def hour_to_min(hour): # 시간을 입력받는 함수
  return hour * MIN

# 매개변수로 분이 들어오면 초 단위로 변환하여 반환
def min_to_sec(min): # 분을 입력받는 함수
  return min * SEC

# 매개변수로 시간이 들어오면 초 단위로 변환하여 반환
def hour_to_sec(hour): # 이전에 정의한 두 함수 이용
  return min_to_sec(hour_to_min(hour))

# 이 코드를 다른 파이썬 파일에서 활용할 예정