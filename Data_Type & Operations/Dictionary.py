# Dictionaries: Objects retrieved by key name.
# Unordered and can not be sorted

# List Objects retrived by location.
# Ordered sequence can be indexed or sliced


my_dict = {'key1':'value1','key2':'value2'}

print(my_dict)

print(my_dict['key1'])


price_lookup={'apple':2.99,'orange':1.99,'milk':5.80}
print(price_lookup['apple'])


d={'k1':123, 'k2': [0,1,2], 'k3':{'insidekey':100}}
print(d['k2'])

print(d['k2'][1])

print(d['k1'])

print(d['k3']['insidekey'])

# insert an object in dict

d['k4']= 'new_item'

print(d)

# It is also mutable

d['k1']= 'I am a replacement'

d={'k1':123, 'k2': [0,1,2], 'k3':{'insidekey':100}}
print(d.keys())
print(d.values())
print(d.items())

