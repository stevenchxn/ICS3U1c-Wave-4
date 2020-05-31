ages = {'Steven':'16', 'Bill':'15', 'Jack':'15', 'Jill':'14', 'Ross':'14'}
search = input("Please enter an age: ")
matches = []

for k, v in ages.items():
    if search == v:
        matches.append(k)

if len(matches) > 1:
    print (" and ".join(matches) + ' are ' + str(search) + ' years old') 
elif len(matches) == 1:
    print (''.join(matches) + ' is ' + str(search) + ' years old')
else: 
    print('Please enter a different age')