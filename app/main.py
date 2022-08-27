import os
import sys
from venv import create

from sklearn.metrics import SCORERS

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
# from app.services.classifier import ClassifierService
from app.services.grade import GradeSerivce
from app.services.pandas_quiz import PandasQuiz
def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") # 입력받은 아이디와 비번만 콘솔에 출력하기
    print("3. 성적표 프로그램") # 입력받은 아이디와 비번만 콘솔에 출력하기
    print("4. Pandas 퀴즈풀기")
    menu = input('메뉴 선택')
    return menu

def main():
    # 메소드로 들어가는 것은 1. 수(변수 or 상수) 2. 식 3. 스테이트먼트(ex - if,for 문)
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
            ID = input('ID :')
            password = input('ID :')
            user.typing(ID,password)
        elif menu == '3':
            gradeService = GradeSerivce()
            name = input('이름 :')
            kor = int(input('국어 :'))
            eng = int(input('영어 :'))
            math = int(input('수학 :'))
            grade = gradeService.get_score(name,kor,eng,math)
            print(f'이름 : {name} 학점 :{grade}')
        elif menu == '4':
            quiz = PandasQuiz()
            while 1:
                quiz_number = input('퀴즈번호 선택. 종료는 0 :')
                if quiz_number == '0':
                    break
                elif quiz_number == '1':
                    quiz.quiz_1()
                elif quiz_number == '2':
                    quiz.quiz_2()
                elif quiz_number == '3':
                    quiz.quiz_3()       
                elif quiz_number == '4':
                    quiz.quiz_4()
              
              
                   
                
if __name__ == '__main__':  
    main()

