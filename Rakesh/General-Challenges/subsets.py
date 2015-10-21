__author__ = 'rakesh'


from collections import defaultdict

hashmap = defaultdict(int)

hashmap[(1, 2)] = 1

print hashmap

if hashmap.has_key((1, 2)):  #since tuple is immutable that you cannot
    print "Rakesh"

#this problem can be easily done using this concept or there are other



