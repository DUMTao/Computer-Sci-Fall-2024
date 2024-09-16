import math

def describe_pet(pet_name, animal_type='cat'):
    print(f'I have a {animal_type}!')
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='Cheeto')


"""
describe_pet(animal_type='hamptr', pet_name='haptr')
describe_pet(pet_name='haptr', animal_type='hamptr')
""" 