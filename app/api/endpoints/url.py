from app.services.calculator import CalculatorService
from app.services.titanic import TitanicService
from app.services.user import UserService
from app.services.grade import GradeSerivce
from app.services.pandas_quiz import PandasQuiz
from app.services.ddarung import DDarungService
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, GRADE, \
    QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, QUIZ_5, QUIZ_6, QUIZ_7 , DDARUNG, TITANIC
class Url:
    
    def router(self, menu):
        if menu == LOGIN:
            UserService().typing(
                input('id'), 
                input('password'))
        elif menu == CALCULATOR:
            CalculatorService().calculate(
                int(input('첫번째 값 입력: ')), 
                int(input('두번째 값 입력: ')))
        elif menu == GRADE:
            name = input('이름')
            korean = int(input('국어'))
            english = int(input('영어'))
            math = int(input('수학'))
            print(f'이름: {name} \
                학점: {GradeSerivce().get_score(name,korean, english, math)}')
        elif menu == DDARUNG : DDarungService().submit(
            path='data/ddarung/',
            train= 'train.csv',
            test='test.csv'
        )
        elif menu == TITANIC :
            titanicService = TitanicService()
            titanicService.submit(
            path='data/kaggle_titanic/',train='train.csv', test='test.csv')
        elif menu == QUIZ_1: PandasQuiz().quiz_1()
        elif menu == QUIZ_2: PandasQuiz().quiz_2()
        elif menu == QUIZ_3: PandasQuiz().quiz_3()
        elif menu == QUIZ_4: PandasQuiz().quiz_4()
        elif menu == QUIZ_5: 
            subject = input('과목 명:')
            PandasQuiz().quiz_5(subject)
        elif menu == QUIZ_6: PandasQuiz().quiz_6() 
        elif menu == QUIZ_7: PandasQuiz().quiz_7() 
        
            
            