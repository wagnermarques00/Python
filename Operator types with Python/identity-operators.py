course = "Python course"
course_name = course
withdraw, limit = 200, 200

# Is
print(course is course_name)  # True
print(withdraw is limit)  # True

# Is not
print(course is not course_name)  # False
print(withdraw is not limit)  # False
