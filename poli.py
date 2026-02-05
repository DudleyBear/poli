# Parent Class
class SchoolUser:
    def get_role(self):
        print("I am a school user.")


# Child Class: Student
class Student(SchoolUser):
    def get_role(self):
        print("I am a student.")


# Child Class: Teacher
class Teacher(SchoolUser):
    def get_role(self):
        print("I am a teacher.")


# Create objects
student1 = Student()
teacher1 = Teacher()

# Store in a list
users = [student1, teacher1]

# Polymorphism in action
for user in users:
    user.get_role()
