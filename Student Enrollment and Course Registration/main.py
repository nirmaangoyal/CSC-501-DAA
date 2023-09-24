import course
import student
import datetime
import enroll

courses=course.AVLTree()


# ADD COURSES-2
start_Time=datetime.time(10,30,0)
end_Time=datetime.time(12,30,0)
courses.insert("MAT100",start_Time,end_Time)


# ADD COURSES-2
start_Time=datetime.time(11,30,0)
end_Time=datetime.time(13,30,0)
courses.insert("CSC501",start_Time,end_Time)


# ADD COURSES-3
start_Time=datetime.time(13,30,0)
end_Time=datetime.time(14,30,0)
courses.insert("CSC582",start_Time,end_Time)


# ADD COURSES-4
start_Time=datetime.time(12,30,0)
end_Time=datetime.time(13,0,0)
courses.insert("PHY300",start_Time,end_Time)


# ADD COURSES-5
start_Time=datetime.time(4,30,0)
end_Time=datetime.time(5,0,0)
courses.insert("CYC531",start_Time,end_Time)




# Add students to the HashMap
student.add_student("101", "Nirmaan")
student.add_student("102", "Anuj")
student.add_student("103", "Tanvi")


# Enroll Students to courses
enroll.add_student_to_course("101","MAT100",courses) 
enroll.add_student_to_course("102","MAT100",courses)
enroll.add_student_to_course("103","MAT100",courses)
enroll.add_student_to_course("103","CSC582",courses)
enroll.add_student_to_course("101","PHY300",courses)
enroll.add_student_to_course("103","CYC531",courses)
enroll.add_student_to_course("103","CSC501",courses)
enroll.add_student_to_course("102","CYC531",courses)




# PRINT COURSE (Generating roster)
courses.print_roster("MAT100")
courses.print_roster("PHY300")
courses.print_roster("CYC531")





# Generate student schedule
student.view_student_info("101")
student.view_student_info("102")
student.view_student_info("103")





# Drop course
student.drop_course("102","MAT100",courses)








