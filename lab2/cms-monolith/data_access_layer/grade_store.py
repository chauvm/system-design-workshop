# Sqlalchemy
class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    user_id = 
    course_id = ...
    score = ...


class GradeStore:
    @staticmethod
    def get_grade(user_id, course_id):        
        grade = session.query(Grade).filter(user_id,course_id).first()
        return grade