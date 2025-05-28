class Student:
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m
    def __str__(self):
        return f"RN={self.rn},Name={self.name},Marks={self.marks}"
o1=Student(1,"ram",98)
o2=Student(2,"ramakant",48)
o3=Student(3,"chaudhari",28)
stud_list=[o1,o2,o3]
print(stud_list)
for st in stud_list:
  print(st)

print(stud_list[0])
print(stud_list[0].rn)
print(stud_list[0].name)
print(stud_list[0].marks)


print(stud_list[1])
print(stud_list[1].rn)
print(stud_list[1].name)
print(stud_list[1].marks)


print(stud_list[2])
print(stud_list[2].rn)
print(stud_list[2].name)
print(stud_list[2].marks)
