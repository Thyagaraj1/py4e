t=[1,2,3,4,5]
t.reverse()
print(t)
#[5, 4, 3, 2, 1]
#t={1,2,3,4,5}
#t.reverse()
#print(t)
#AttributeError: 'set' object has no attribute 'reverse'

#t=(1,2,3,4,5)
#t.reverse()
#print(t)
#AttributeError: 'tuple' object has no attribute 'reverse'


t=[1,2,3,4,5]
t.insert(1,7)
print(t)
#[1, 7, 2, 3, 4, 5]

t=[1,2,3,4,5]
t.append(8)
print(t)
#[1, 2, 3, 4, 5, 8]

#t=(1,2,3,4,5)
#t.append(8)
#print(t)
#AttributeError: 'tuple' object has no attribute 'append'