
from werkzeug.datastructures import MultiDict
  
orders = MultiDict([(1, 'GFG'), (1, 'Geeks')])
# print(orders[1])
  
orders[1] = 5

print(orders)