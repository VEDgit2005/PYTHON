students=["John", 88 , "Amber", 90 ,"Harry", 75 , "Ted" ,94 ,"Sandra", 80]
#print(students[2])

"""for x in range(0,len(students),2):
   print(students[x], "scored", students[x+1])
"""
#students.insert(0,"John"), u can do this way
students.append("Todd")
students.append("81")

#for x in range(0,len(students),2):
 #  print(students[x], "scored", students[x+1])
print(students)
students[-1]= 91
#print(students)
students2=["Hobart", 70]
students.extend(students2)

students.remove("Hobart")
students.remove(70)
#print(students)
"""students.pop()
print(students)"""
#students.clear
#print(students)
index =students.index(90)
print(index)
print(students[4])