#name = {key:value} = dictionary
people = {'ppatel': 'parth patel',
          'zmin': 'zhing min',
          'htanaka': 'Haru Tanaka'}
for person in people:
    print(person + " is the key of the value " +  people[person])

print(people)
print(people['ppatel'])

# Popping (deleting) the element
people.pop('zmin')
print(people)
print(len(people))

# Adding the popped element back using a dictionary
people.update({'zmin': 'zhing min'})
print(people)
print(len(people))

