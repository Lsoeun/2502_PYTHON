# 다른 패키지에 있는 모듈 사용하기
# 패키지? - 디렉터리 형태로 모듈을 그룹화한것
# 만약 모듈이 다른 디렉터리에 있다면, 해당 디렉터리를 sys.path에 추가하거나 PYTHONPATH 환경 변수에 등록해야 함
# 이 작업은 Python이 모듈을 찾을 수 있도록 경로를 명시적으로 알려주기 위해 필요함
# Day12_1 패키지의 모듈에서 모든 함수와 변수 가지고 오기

import sys
sys.path.append(r"C:\Users\SoJung\2412_PYTHON")
from Day12_1.cal import *

fat_calories = calculate_calories(1, 10)
print(fat_calories)

protein_calories = calculate_calories(2, 20)
print(protein_calories)

carbon_calories = calculate_calories(3, 50)
print(carbon_calories)

other_calories = calculate_calories(10, 7)
print(other_calories)