
import re

s = "node.js ruby python python3 python3.6"
d = {'python': 'python2.7', 'python3': 'python3.5', 'python3.6': 'python3.7'}

pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
result = pattern.sub(lambda x: d[x.group()], s)

print result

#
# modelName = ['Toyota', 'Nissan',  'Honda']
# fuelEfficiency = [15.0, 20.0, 30.0]
# priceGas = 2.41
# totalCost1 = (10000 * priceGas)/15.0
# totalCost2 = (10000 * priceGas)/20.0
# totalCost3 = (10000 * priceGas)/30.0
# totalcost = [totalCost1, totalCost2, totalCost3]
#
# print ("Model", "Cost(MPG)", "TOTALCOST")
# for i in zip(modelName, fuelEfficiency, totalcost):
#     print (" ".join(map(str, list(i))))


