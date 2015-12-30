print


# 1 - Intro
def filter(x):
    return x >= 'B'

def expressions(x):
    return '(%s)' % x


alpha_list = ['A','B','C']
print alpha_list

new_list = []
for i in alpha_list:
    if filter(i):
        new_list.append(expressions(i))

print new_list

# Read statements, left to right
print [expressions(i) for i in alpha_list if filter(i)]


# 2 - Chained vs Embeded
num_list = [20,40,60]
print ['%s-%d' % (x, y) for x in alpha_list for y in num_list]

out_list = []
for x in alpha_list:
    for y in num_list:
        out_list.append('%s-%d' % (x, y))

print out_list

print [['%s-%d' % (x, y) for x in alpha_list] for y in num_list]

out_list = []
for y in num_list:
    out_list_inner = []
    for x in alpha_list:
        out_list_inner.append('%s-%d' % (x, y))
    out_list.append(out_list_inner)
print out_list

print ['%s-%d' % (x, y) for x in alpha_list if x < 'C' for y in num_list if y < 55]
print ['%s-%d' % (x, y) for x in alpha_list for y in num_list if y < 55 and x < 'C']
print ['%s-%d' % (x, y) for x in alpha_list if y < 55 and x < 'C' for y in num_list]

['%s-%d' % (x, y)
	for x in alpha_list
		if x < 'C'
			for y in num_list
				if y < 55]


# matrix example

 [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*B)] for X_row in A]

# nested loop list comprehension

print [[float(y) for y in x] for x in l]
print [[i for i in words[index:]] for index, j in enumerate(words)]
# nested for loop if you don't want list of list

print [i for index, j in enumerate(words) for i in words[index + 1:]]

out_list = []
for x in alpha_list:
    if x < 'C':
        for y in num_list:
            if y < 55:
                out_list.append('%s-%d' % (x, y))
print out_list

out_list = []
for x in alpha_list:
    for y in num_list:
        if y < 55 and x < 'C':
            out_list.append('%s-%d' % (x, y))
print out_list

out_list = []
for x in alpha_list:
    if y < 55 and x < 'C':
        for y in num_list:
            out_list.append('%s-%d' % (x, y))
print out_list

vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]


# 3 - Reversed / iterators # double for loop
rev_old = reversed(alpha_list)
print [i + a for i in alpha_list for a in rev_old]

print [i for i in rev_old]
print rev_old

rev_old = reversed(alpha_list)
out_list = []
for y in alpha_list:
    out_list_inner = []
    for x in rev_old:
        out_list_inner.append('%s-%s' % (x, y))
    out_list.append(out_list_inner)

print out_list

rev_list = list(reversed(alpha_list))
print [i + a for i in alpha_list for a in rev_list]

print [i + a for i in alpha_list for a in reversed(alpha_list)]

rev_old = reversed(alpha_list)
print [i + a for i in rev_old for a in alpha_list]
print [i + a for i in alpha_list for a in alpha_list[::-1]]
rev_old = alpha_list[::-1]
print [i + a for i in alpha_list for a in rev_old]


# 4 - Dictionary comprehension
keys = [10,30,50]
print dict((x, y) for x in keys for y in num_list)

print [(x, y) for x in keys for y in num_list]

print [x for x in zip(keys, num_list)]

print dict(zip(keys, num_list))

class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s (%d)" % (self.name, self.id)

people = [
    Person(1, 'Joe'),
    Person(2, 'Marry'),
    Person(3, 'Kieth')
]

print dict([(p.id, p) for p in people])

print