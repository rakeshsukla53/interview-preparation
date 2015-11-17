
class C:
    dangerous = 2

D = C

D().dangerous = 5

c1 = C()
c2 = C()

print c1.dangerous  # because by default everything is public in Python

c1.dangerous = 3

print c1.dangerous
print c2.dangerous

del c1.dangerous

print c1.dangerous

C.dangerous = 3

print c2.dangerous

# classes are just a template and class object is what we should talk about always and do check the diagrams






