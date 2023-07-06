"""
print('Hello, World!')
teams = [ 'Dragons', 'Wolfs', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f'{home_team} vs {away_team}')
""" 
""" 
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            print(result, end='\t')
        print()

multiplication_table(3)

"""

def even_numbers(maximum):
    print('here 1')
    return_string = " "
    for i in range(maximum):
        print('here 2')
        return_string += str(maximum)
        return return_string.strip()
    print('here 3')
    
print(even_numbers(6))