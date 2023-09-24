import course

class Student:
    def __init__(self, student_id, name, enrolled_courses=None):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = enrolled_courses or []

# Create an empty HashMap for student information
student_info = {}

# Function to add a new student to the HashMap
def add_student(student_id, name):
    if student_id not in student_info:
        student_info[student_id] = Student(student_id, name)
        # print(f"Student Name:{name} with (ID: {student_id}) added successfully.",end="\n\n")
        print("----Student Added------")   
        print(f"Student ID: {student_id}")
        print(f"Name: {name}")
        print("-----------------------",end="\n\n")   

    else:
        print(f"Student with ID {student_id} already exists.",end="\n\n")


# Function to view a student's information
def view_student_info(student_id):
    if student_id in student_info:
        student = student_info[student_id]
        print("----Student Info------")   
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Enrolled Courses: {', '.join(student.enrolled_courses)}")
        print("----------------------",end="\n\n")   

    else:
        print(f"Student with ID {student_id} not found.",end="\n\n")


def drop_course(student_id,course_id,courses):
    if student_id  in student_info:
        student=student_info[student_id]
        c1=courses.search(course_id)

        if course_id in student.enrolled_courses: 
            student.enrolled_courses.remove(course_id)
            c1.enrolled_students.remove(student_id)
            print(f"Course:-{course_id} dropped successfully by {student.name}",end="\n\n")

    else:
        print(f"Student with ID {student_id} does not exist.",end="\n\n")    





















