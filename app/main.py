import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from app.api.endpoints.url import Url
from app.constants.menus import DDARUNG, LOGIN, LOGOUT, CALCULATOR, GRADE, \
    QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, QUIZ_5, QUIZ_6, QUIZ_7, TITANIC

def print_menu():
    print(' ###################')
    print(f'로그인 : {LOGIN}')
    print(f'로그아웃 : {LOGOUT}')
    print(f'계산기 : {CALCULATOR}')
    print(f'성적표 : {GRADE}') 
    print(f'따릉이 : {DDARUNG}')
    print(f'타이타닉 : {TITANIC}')
    print(f'퀴즈 1 : {QUIZ_1}') 
    print(f'퀴즈 2 : {QUIZ_2}')
    print(f'퀴즈 3 : {QUIZ_3}')
    print(f'퀴즈 4 : {QUIZ_4}')
    print(f'퀴즈 5 : {QUIZ_5}')
    print(f'퀴즈 6 : {QUIZ_6}')
    print(f'퀴즈 7 : {QUIZ_7}')
    menu = input('메뉴에서 URL을 카피해서 입력하시오\n')
    print(' ###################')
    return menu
          
def main():
    url = Url()
    while 1:
        menu = print_menu()
        if menu == f'{LOGOUT}':
            break
        else : url.router(menu)
                         
            
if __name__ == '__main__' :
    main()
    