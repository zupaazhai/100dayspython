'''
Pizza Challenge
'''

print('===========================')
print('=  Welcome to Daddy Pizza =')
print('===========================')

size = input('Enter your size (S, M, L): ').lower()
add_pepperoni = input('Add Pepperoni ( $2 for S, $3 for M and L )? (y, n): ').lower()
add_extra_cheese = input('Add extra cheese ( $1 )? (y, n): ').lower()

total = 0

'''
# Version 1

if size == 's':
    total += 15
elif size == 'm':
    total += 20
elif size == 'l':
    total += 25
'''

prices = {
    's': 15,
    'm': 20,
    'l': 25
}

total += prices[size]

if add_pepperoni == 'y':
    if size == 's':
        total += 2
    elif size == 'm' or size == 'l':
        total += 3

if add_extra_cheese == 'y':
    total += 1

print(f'Your total price is {total}')
