
i = 0
for i in range(5):
    print("Hello using loop")

i = 0
while i < 5:
    print("Hello using while loop")
    i = i + 1

print('Done')
print('----------------------- \n')

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    
    print("Blastoff!")


countdown(45)