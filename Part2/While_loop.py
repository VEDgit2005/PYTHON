counter=65
while counter < 91:
    if counter < 70:
        counter +=1
        continue    
    print(str(counter)+ " = " + chr(counter))
    counter +=1
    if counter > 85:
        break 
print("While loop completed")      