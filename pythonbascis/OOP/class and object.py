class Student:

    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student()
student1.name = 'Harry'
student1.score = 85

# calling this method using student1 object
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)


# create object
student2 = Student()
student2.name = 'Ronin'
student2.score = 35

# calling this method using student2 object
did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)
