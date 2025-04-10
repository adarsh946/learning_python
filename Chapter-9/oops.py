class Student :
    course = "web development"
    subjects = 5

    @staticmethod
    def greet() :
        print(f"good morning, adarsh. your course is {course}. and it contains {subjects} subjects.")


adarsh = Student()
adarsh.course = "GenAI"
print(adarsh.course, adarsh.subjects)
adarsh.greet()
