import course
import student


def add_student_to_course(student_id,course_id,courses):
    
    if student_id  in student.student_info:
        s1=student.student_info[student_id]
        # print(courses.conflicting_courses)
        c1=courses.search(course_id) 
        if c1 is None:
            print("Enter valid Course ID",end="\n\n")
            return

        # print(f"student===>{s1.enrolled_courses}")
        for course in s1.enrolled_courses:
            if course in courses.conflicting_courses[course_id]:
                print(f"Cannot add this course :{course_id} due to TIME CONFLICT with the course: {course}",end="\n\n")
                return

        
        # check if student exists in course or course in student
        if course_id not in s1.enrolled_courses and student_id not in c1.enrolled_students:
            # check if course timing CONFLICTS with other courses


            s1.enrolled_courses.append(course_id)
            c1.enrolled_students.append(student_id)
            # print(f"Student {s1.name} (ID: {student_id}) enrolled in course {course_id}.",end="\n\n")
            print("----Student Enrolled------")   
            print(f"Student ID: {student_id}")
            print(f"Name: {s1.name}")
            print(f"Enrolled Course: {course_id}")
            print("--------------------------",end="\n\n")               
        else:
            print(f"Student {s1.name} (ID: {student_id}) is already enrolled in course {course_id}.",end="\n\n")
    else:
        print(f"Student with ID {student_id} not found.",end="\n\n")        
