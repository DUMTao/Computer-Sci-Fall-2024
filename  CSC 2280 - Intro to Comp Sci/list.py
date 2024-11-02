
silver_eyes = ['Charlie', 'Jessica', 'John', 'Carlton', 'Dave','Michael']
#silver_eyes[3] = 'Marla'
'''
print(silver_eyes[0])
print(silver_eyes[-1])
print(silver_eyes[:3])
'''

#months = ["January", "Febuary", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]

'''
for i in range(len(months)):
    # print(str(months.index(i) + 1)+ '-' + i)
    #print(f"One of the months of the year is {i}!")
    months[i] = months[i] + ' 2024'

for i in months:
    print(i)
'''

#for i in silver_eyes:
#    print(i + " learning Python")
    

for i in range(len(silver_eyes)):
    silver_eyes[i] = silver_eyes[i] + " learning Python"
    print(silver_eyes)