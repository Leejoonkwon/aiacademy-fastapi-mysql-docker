from app.models.classifier import Classifier

class ClassifierService(object):
    def __init__(self) -> None:
        pass
    def typing(self,name,score1,score2,score3):
        classifier=Classifier(name,score1,score2,score3)
        print(f'학생의 이름 : {classifier.name}')
        print(f'{classifier.score1}+{classifier.score2}+{classifier.score3}의 평균 {classifier.score()}')
        if classifier.score() >= 80:
            print(f'A 등급')
        elif classifier.score() >= 66.4:
            print(f'B 등급')
        elif classifier.score() >= 49.8:
            print(f'C 등급')
        elif classifier.score() >= 33.2:
            print(f'D 등급')
        elif classifier.score() >= 16.6:
            print(f'F 등급')
            
            
            
        
      
   

       
   