from app.models.calculator import Calculator

class CalculatorService(object): #영어단어 뜻이 달라지는 시점에서 대문자 파스칼 리스펙
    def __init__(self) -> None :
        pass
    
    def calculate(self,first,second):    # 클래스는 명사 method는 동사
        calculator = Calculator(first,second)
        print(f'첫번째 수 :{calculator.first}') 
        print(f'두번째 수 :{calculator.second}') 
        
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}') 
        print(f'{calculator.first} - {calculator.second} = {calculator.sub()}') 
        print(f'{calculator.first} * {calculator.second} = {calculator.mul()}') 
        print(f'{calculator.first} / {calculator.second} = {calculator.div()}') 
       
        
