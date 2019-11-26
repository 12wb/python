class class1():
    def __init__(self,student1=[],teacher1=[]):
        self.students = student1
        self.teachers = teacher1
    def count(self,people):
        return len(people)
teachers = ['高老师','康老师','杨老师']
students = ['毕志刚','谢丽文','谢文玉','丁芳','孙萍']

showMyClass = class1(students,teachers)
print('该班有%d个学生，%d个老师'%(showMyClass.count(showMyClass.students),showMyClass.count((showMyClass.teachers))))
