# Given a string, count how many times a letter appears in the string using a dictionary

'''
def count_letter(string):
    letter_dict = {}
    
    for i in string:
        if i not in letter_dict:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1
    
    return print(letter_dict)

count_letter("The cat is on the mat. The dog is on the couch")



# Creating an empty dictionary
#captains = dict()
captain_pairs = ( ('Enterprise', 'Picard'), 
('Voyager', 'Janeway'), 
('Defiant', 'Sisko') )
captains = dict(captain_pairs)

# Adding key-value pairs to the dictionary
#captains['Enterprise'] = 'Picard'
#captains['Voyager'] = 'Janeway'
#captains['Defiant'] = 'Sisko'

# Checking whether a key exists in the dictionary, if not; delete it
if 'Enterprise' not in captains:
    captains['Enterprise'] = 'unknown'
    
elif 'Discovery' not in captains:
    captains['Discovery'] = 'unknown'
    
else:
    print("Either Enterprise or Discovery is not in the dictionary")

del captains['Discovery']

# For loop to print out the key-value pairs
for key in captains.items():
    print(f"The {key[0]} and its captain are {key[1]}")

'''
'''
inventory = {'apples' : 430, 'bananas' : 312, 'oranges' : 525, 'pears' : 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k, v) in inventory.items():
    print("Got", k, "that maps to", v)
'''

import random

# Create dic
capitals_dict = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 
    'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver',
    'Conneticut' : 'Hartford', 'Delaware': 'Dover',
    'Florida' : 'Tallahassee', 'Georgia' : 'Atlanta'
}

# Take a random key
questions = list(capitals_dict.keys())


# Ask user for the capital of the state
while len(questions) > 0:
    state = random.choice(questions)
    
    answer = input(f"What is the capital of {state}? ")
    
    

    # If ans correct
    if answer.lower() == capitals_dict[state].lower():
        print("Correct!")

    # If ans exit
    elif answer.lower() == 'exit':
        print("Goodbye")
        break;
    
    # If ans is incorrect
    else:
        print(f"Good try! the capital of {state} is {capitals_dict[state]}")




