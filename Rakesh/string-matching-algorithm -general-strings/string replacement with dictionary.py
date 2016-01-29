
import re

s = "node.js ruby python python3 python3.6"
d = {'python': 'python2.7', 'python3': 'python3.5', 'python3.6': 'python3.7'}

pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
result = pattern.sub(lambda x: d[x.group()], s)

print result

