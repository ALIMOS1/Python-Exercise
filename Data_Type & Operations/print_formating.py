# print formating with strings

# .format method

# 'String here {} then also {}.format('something1','something2')


print('\nThis is a string {}'.format('Insert anything here'.lower()))

print('')

message = 'Insert anything here'

print('This is a string {} \n'.format(message.upper()))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))


print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))
