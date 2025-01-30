class School:
  school = 'Bot school'


p = School()

#Printing without any changes 
print(p.school)
print(School.school)


#Printing after changing instance variable
p.school = 'Double bot school'
print()
print(p.school)
print(School.school)



#Printing after changing class variable

School.school = 'Tripe bot school'
print()
print(p.school)
print(School.school)