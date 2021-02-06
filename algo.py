points = {'A+': 4.0,'A': 3.75,'A-': 3.50,'B+': 3.25,'B': 3.0,'B-': 2.75,'C+': 2.50,'C': 2.25,'D': 2.0,'F': 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade =='':
        done = True
    elif grade not in points:
            print("Unknown grade '{0}' being ignored".format(grade))
    else:
                num_courses += 1
                total_points += points[grade]
                if num_courses > 0:
                    print('Your GPA is {0:.3}'.format(total_points / num_courses))