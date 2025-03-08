# import를 통해 모듈을 불러와 다른 파일의 코드를 사용
# import로 파일 전체를 가지고 옴(ex01.py)
import ex01

min = ex01.hour_to_min(6)
print("6 hours =", min, "min")

sec = ex01.min_to_sec(12)
print("12 mins =", sec, "sec")

sec = ex01.hour_to_sec(3)
print("3 hours =", sec, "sec")