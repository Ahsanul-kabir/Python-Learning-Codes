course = 'Python for Beginners'
print(len(course))

print('\n')
print(course.upper())
print(course.lower())
print(course)

print('\n')
print(course.find('P'))
print(course.find('o'))
print(course.find('Beginners'))

print('\n')
print(course.replace('Beginners','Absolute Beginner'))
print(course)
print(course.replace('P','J'))

print(course)

print('\n')
# in & find both use src any item But find return Index value and in return boolien True/False
print('Python' in course)   # Python likha ta ki course variable er modde ase kina check korbe
print('Jython' in course)

print(course.title())
