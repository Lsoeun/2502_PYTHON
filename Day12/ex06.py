# 길이 단위 변환 모듈 활용하기
from ex05 import *

kilometer = 500
meter = 50
miles = 310.6855

miles_from_kilometer = kilometer_to_miles(kilometer)
print(kilometer, "킬로미터를 miles로 환산하면", miles_from_kilometer, "마일입니다.")

kilometer_from_meter = meter_to_kilometer(meter)
print(meter, "미터를 kilometer로 환산하면", kilometer_from_meter, "킬로미터입니다.")

kilometer_from_miles = miles_to_kilometer(miles)
print(miles, "마일을 kilometer로 환산하면", kilometer_from_miles, "킬로미터입니다.")
