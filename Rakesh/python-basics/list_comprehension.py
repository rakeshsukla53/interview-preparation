
l = [1, 2, 3, 4, 5, 6, 7]

# filter means what all values you want to use
print filter(lambda x: x if x % 2 == 0 else 0, l)

print filter(lambda x: x if x % 2 == 0 else 0, l)

print [i if i % 2 == 0 else 0 for i in l]

# create a matrix in python using list comprehension

print [[i if i == 2 else 0 for i in range(3)] for j in range(3)]

towns = [{'name': 'Manchester', 'population': 58241}, {'name': 'Coventry', 'population': 12435}, {'name': 'South Windsor', 'population': 25709}]

print [x['name'] for x in towns]

print map(lambda x: x['name'], towns)

a = ['apple', 'mango', 'orange', 'guava']

print sorted(enumerate(a), reverse=True)


