class CourseEnrollment:
    def __init__(self, course_id):
        self.id = course_id
        self.grade = None

class Student:
    def __init__(self, user_id):
        self.id = user_id
        self.active_courses = []

    def enroll_in_course(self, course_id):
        #course = CourseEnrollment(course_id)
        course = [course_id, None]
        self.active_courses.append(course)
    
    def view_courses(self):
        for course in self.active_courses:
            print(f"{course[0]} - {course[1]}")

def finish_course(self, course_id, grade):
    for course in self.active_courses:
        if course[0] == course_id:
            course[1] = grade

if __name__ == "__main__":
    print("NY KJØRING")
    s = Student(123)
    s.enroll_in_course("inf-1100")
    s.enroll_in_course("inf-1049")
    s.enroll_in_course("inf-1400")
    finish_course(s, "inf-1400", "A")
    s.view_courses()


