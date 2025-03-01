#string manipulation 
first_name="Sir"
second_name="Ratan"
last_name="Tata"
#string concatenation
full_name=first_name+second_name+last_name; print(full_name)
full_namewithspaces=first_name+ " " + second_name + " " + last_name; print(full_namewithspaces)
print(len(full_name))
print(full_name[2])
print(full_name[-3])
print(full_name[0:3])
print(full_name[:])
#string methods
print(full_name.upper())
print(full_namewithspaces.swapcase())
