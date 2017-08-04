snacks = {
    'Fruit Snacks': 10,
    'Nutella' : 9,
    'Rice Krispy Treats' : 8,
    'Apples': 7
}
print snacks
snacks['Oranges'] = 6
snacks['Raisins'] = 3
print snacks

for i in snacks:
    snacks['Raisins'] = 2
    print i
    print snacks[i]
    print '%s get a %s out of 10'%(i, snacks[i])

print snacks
