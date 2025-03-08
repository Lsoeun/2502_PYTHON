# 모듈 내의 모든 함수를 사용하고 싶은 경우
from ex01 import *

min = hour_to_min(6) # 파일명.함수를 할 필요 없이 바로 함수명을 사용
print("6 hours =", min, "min")

sec = min_to_sec(13)
print("13 mins =", sec, "sec")

sec = hour_to_sec(3)
print("3 hous =", sec, "sec")