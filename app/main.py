import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") # 입력받은 아이디와 비번만 콘솔에 출력하기
    menu = input('메뉴 선택')
    return menu

def main():
    # 메소드로 들어가는 것은 1. 변수 2. 식 3. 스테이트먼트(ex - if,for 문)
    # loop = 반복문 
     
    while 1: # 스테이트먼트 값에 브랜치(길)을 건다
        menu = print_menu()
        if menu == '0':
            print('전체 프로그램을 종료합니다.')
            break
        elif menu == '1':
            calculatorService = CalculatorService() # 변수 와 식
            first = int(input('첫번쨰 값 입력:'))
            second = int(input('두번쨰 값 입력:'))
            calculatorService.calculate(first,second)
        elif menu == '2':
            user = UserService()
            ID = str('')
            password = str('')
            user.typing(ID,password)
            break
if __name__ == '__main__':
    main()

