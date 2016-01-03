
import urllib2
import xml.etree.ElementTree as ET

import time
start_time = time.time()

r = urllib2.urlopen('http://python-data.dr-chuck.net/comments_42.xml').read()
root = ET.fromstring(r)

print sum([int(list(count.itertext())[0]) for count in root.findall('.//count')])
print ("--- %s seconds ---" % (time.time() - start_time))

# ['__class__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__len__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_children', 'append', 'attrib', 'clear', 'copy', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']
# link - http://python-data.dr-chuck.net/comments_42.xml


