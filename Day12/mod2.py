def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 수정 전
# print(add(1, 4))
# print(sub(4, 2))

# 수정 후
# if __name__ == "__main__": 구문 추가
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
    
    
# if __name__ == "__main__"을 사용하면, 직접 이 파일을 실행했을 때는__name__ == "__main__"이 참이 되어 if 문 다음 문장이 수행됨
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러 사용할 때는 __name__ == "__main__"이 거짓이 되어 if 문 다음 문장이 수행되지 않음