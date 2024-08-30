#Exercise 2.2
from math import pi

# 1. The volume of The volume of a sphere with radius r is 4/3πr^3. 
# What is the volume of a sphere with radius 5?
radius = 5**3
print(f'The volume of a sphere with radius 5 is: {(4/3) * (pi * radius)} ')

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
cover_price = 24.95
discount = cover_price * (40/100)
price_per_book = cover_price - discount
shipping_cost = 3
shipping_after1 = 0.75
print(f' The total wholesale cost for 60 copies is: {(price_per_book * 60) + 3 + (shipping_after1 * 59)}  ')

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?
beginning_time = 6.52
easy_pace_time = 8.15
tempo_pace_time = 7.12
total_miles = 5
tempo_per_mile = tempo_pace_time / 3
print(tempo_per_mile)

print((1 + 3) / 2)

