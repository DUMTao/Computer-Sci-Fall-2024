# List Comprehension
# Make a list to convert the temp F to temp C
# °C = (°F - 32) × 5/9

'''
temp_F = [72, 75, 68]
temp_C = []


for i in range(len(temp_F)):
    temp_C_formula = (temp_F[i] - 32) * (5/9)
    temp_C.append(temp_C_formula)
    
print(temp_C)



# List Comprehension
temp_F = [72, 75, 68]
temp_C = [int((temp - 32) * (5/9)) for temp in temp_F]
print(temp_C)
'''

# Update last 3 elements of the list with t, u, v
# [start:end] putting any number is optional and no number means 0
'''
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[-3:] = ['t', 'u', 'v']

print(t)
'''
'''
names = ["mark", "ethan", "john", "peter", "liam", "noah"]
def cap_names(lst):
    cap_lst = []
    
    for i in lst:
        cap_lst.append(i.capitalize())
    
    return cap_lst

print(cap_names(names))
'''






