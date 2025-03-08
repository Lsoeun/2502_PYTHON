import turtle as t  # turtle 모듈을 t라는 이름으로 임포트

t.shape("turtle")  # 거북이 모양을 'turtle'로 설정
t.pensize(10)  # 펜의 두께를 10픽셀로 설정

t.begin_fill()  # 도형을 그리기 시작하며, 채우기를 시작
t.fillcolor("pink")  # 도형을 핑크색으로 채우기 위한 색상 설정

t.circle(100)  # 반지름 100픽셀인 원을 그리기
t.end_fill()  # 채우기 종료 (원 내부를 핑크색으로 채우기 완료)

t.done()  # 그래픽 작업이 끝났음을 알리고, 창을 닫지 않도록 유지