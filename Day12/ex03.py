# 모듈에서 특정 함수만 가지고 오기
from ex01 import hour_to_min
from ex01 import min_to_sec
# from ex01 import hour_to_min, min_to_sec -> 이렇게도 가능

min = hour_to_min(7) # 파일명.함수를 할 필요 없이 바로 함수명을 사용
print("7 hours =", min, "min")

sec = min_to_sec(13)
print("13 mins =", sec, "sec")

# 전체 파일이 아닌 특정 함수만 직접 가져오는 경우는 불필요한 부분을 제외하고 원하는 기능만 사용할 수 있기 때문에 메모리의 낭비를 줄일 수 있음