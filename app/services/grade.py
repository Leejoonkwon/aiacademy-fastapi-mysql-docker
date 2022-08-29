from app.models.grade import Grade
class GradeSerivce(object):

    def set_score(self,name,kor,eng,math):
        grade = Grade(name,kor,eng,math)
        grade.set_avg()
        avg = grade.get_avg()
        if avg > 90:
            self.credit = 'A'
        elif avg > 80:
            self.credit = 'B'
        elif avg > 70:
            self.credit = 'C'
        elif avg > 60:
            self.credit = 'D' 
        elif avg > 50:
            self.credit = 'E' 
        else :
            self.credit = 'F'
    def get_score(self,name,kor,eng,math):
        self.set_score(name,kor,eng,math)
        return self.credit                                                              