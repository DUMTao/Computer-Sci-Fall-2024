# Write function named greet_user() to print message

def greet_user():
    print('Hello, welcome to Florida Southern College! :)')
    print('this is being recorded >:) -----')

greet_user()

def greet_username(name):
    print(f'Hello! {name}, Welcome to Florida Southern College')

greet_username('Andy')
greet_username('Max')
greet_username('Antoni')
greet_username('lily')
print('  ')

def favorite_book(title):
    print(f'One of my favorite books is {title}!')

favorite_book('Alice in Wonderland')
favorite_book('Brave new World')
print('  ')

def describe_pet(animal_type, pet_name):
    print(f'I have a {animal_type}!')
    print(f"My {animal_type}'s name is {pet_name.title()} ")

describe_pet('hamptr', 'harry')
describe_pet('dog', 'chloe')
describe_pet('cat', 'cheeto')