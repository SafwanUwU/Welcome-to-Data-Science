import numpy as np

data_type = [
    ('name','S15'),
    ('class', int),
    ('height', float)

]
students_details = [
    ('Safwan', 5,48.5),
    ('Afnan',6,52.5),
    ('Sajid',5,42.10),
    ('Nahian',5,40.11)

]

students=np.array(students_details, dtype=data_type)

print("Original Array:")
print(students)

print()

print("Sort by height")
print(np.sort(students, order='height'))