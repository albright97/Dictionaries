#dictionaries

students= ['bob', 13, 'jane', 15, 'mark', 14, 'kate', 16]
print(students[0], students[1])

students= {'bob':13, 'jane':15, 'mark':14, 'kate':16}

print(students['bob'])

students['bob'] = 14
del students['kate']

print(len(students))
