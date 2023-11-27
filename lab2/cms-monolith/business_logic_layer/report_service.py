# "higher" services call "lower" services
def get_grades_for_student(id):
    courses = course_service.get_courses_for_student(id)
    grades = grade_service.get_grades(id, course_ids)