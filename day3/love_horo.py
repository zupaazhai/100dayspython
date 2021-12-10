'''
Calculate love score you and your love
'''

first_name = input('Enter your name: ').lower()
second_name = input('Enter second name: ').lower()
combined_name = first_name + second_name

scores = {
    't': combined_name.count('t'),
    'r': combined_name.count('r'),
    'u': combined_name.count('u'),
    'e': combined_name.count('e'),
    'l': combined_name.count('l'),
    'o': combined_name.count('o'),
    'v': combined_name.count('v'),
    'e': combined_name.count('v'),
}

total_score = 0

'''
For loop solution
'''
for key, score in scores.items():
    total_score += score

'''
sum() solution
'''
total_sum_sol = sum(list(scores.values()))

print(f"Your love score is : {total_score}")
print(f"Your love score sum by list : {total_sum_sol}")
# print(true_score, love_score)

