# Given a string, count how many times a letter appears in the string using a dictionary

def count_letter(string):
    letter_dict = {}
    
    for i in string:
        if i not in letter_dict:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1
    
    return print(letter_dict)

count_letter("The cat is on the mat. The dog is on the couch")