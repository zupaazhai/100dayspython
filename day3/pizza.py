'''
Pizza Challenge
'''

print('===========================')
print('=  Welcome to Daddy Pizza =')
print('===========================')

is_opened = True

if not is_opened:
    print('Daddy pizza is closed')
    print('-- Bye --')
    exit(0)

size = input('Enter your size (S, M, L): ').lower()
add_pepperoni = input('Add Pepperoni ( $2 for S, $3 for M and L )? (y, n): ').lower()
add_extra_cheese = input('Add extra cheese ( $1 )? (y, n): ').lower()

'''
Handle with short-if
It seems more readable 
I love it

x = 0 if x < 0 else x
'''
add_pepperoni = 'n' if add_pepperoni not in ['y', 'n'] else add_pepperoni
add_extra_cheese = 'n' if add_extra_cheese not in ['y', 'n'] else add_extra_cheese

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

if size not in prices :
    print("Operation failed !!")
    exit(0)

total += prices[size]

if add_pepperoni == 'y':
    if size == 's':
        total += 2
    elif size == 'm' or size == 'l':
        total += 3

if add_extra_cheese == 'y':
    total += 1

print(f'Your total price is {total}')
