class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

class StudentStore:
    @staticmethod
    def get_students():
        session = Session()
        
        # Retrieve users from the database using an ORM query
        users = session.query(User).filter(role="STUDENT").all()
        
        session.close()
        
        return users
    
    @staticmethod
    def create_student(user_data):
        session = Session()
        
        # Create a new User object
        user = User(name=user_data['name'], email=user_data['email'], role="STUDENT")
        
        # Add the user to the session and commit the transaction
        session.add(user)
        session.commit()
        
        session.close()