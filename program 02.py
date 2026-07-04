courses = {
    "python": 5000,
    "web development": 7000,
    "Data science": 6000,
    "operating system": 5000   
}
selected_course = []
total = 0
course =  input("enter course or 'done': ")
while course != "done":
    if course in courses:
        selected_course.append(course)
        total += courses[course]
    else:
        print("course not found")
    course =  input("enter course or 'done: ")
    if len(selected_course) >= 3:
        total = total - (total * 15 / 100)
    print("selected course:", selected_course)
    print("total bill:", total)
    
