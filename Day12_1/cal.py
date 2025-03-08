# 다른 패키지에 있는 모듈

FAT = 9
PROTEIN = 4
CARBON = 4

# 입력된 영양소 종류와 그램 수를 기반으로 칼로리 양을 계산하고 반환
def calculate_calories(kind, gram):
  if kind == 1: # 1 이면 지방
    return gram * FAT
  elif kind == 2: # 2 이면 단백질
    return gram * PROTEIN
  elif kind == 3: # 3 이면 탄수화물
    return gram * CARBON
  else: # 조건에 해당하지 않으면 문자열 반환
    return "영양소 종류가 잘못 입력되었습니다."