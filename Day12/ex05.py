# 길이 단위 변환 모듈 만들기
MILES = 0.621371 # kilometer를 mile로 변환할 때 사용되는 상수
KILOMETER = 1000 # 1 kilometer는 1000 meter

def kilometer_to_miles(kilometer): # 킬로미터(kilometer)를 마일(miles)로 변환
  return kilometer * MILES


def kilometer_to_meter(kilometer): # 킬로미터(kilometer)를 미터(meter)로 변환
  return kilometer * KILOMETER


def meter_to_kilometer(meter): # 미터(meter)를 킬로미터(kilometer)로 변환
  return meter / KILOMETER


def meter_to_miles(meter): # 미터(meter)를 마일(miles)로 변환
  return (meter / KILOMETER) * MILES


def miles_to_meter(miles): # 마일(miles)을 미터(meter)로 변환
  return (miles / MILES) * KILOMETER


def miles_to_kilometer(miles): # 마일(miles)을 킬로미터(kilometer)로 변환
    return miles / MILES