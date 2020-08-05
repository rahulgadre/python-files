# Hello World
print (' hello world')

# Length of a sentence
a = 'winter is coming'
print (len (a))

# reversing a strong
mystring = "rahulgadre"
print (mystring[::-1])

# spliting string
secstring = "the world is dark"
print (secstring.split())

# Using variables 
show = "GoT"
time = 7
print (f'Do not forget to watch {show} at {time}')

# Format 
print('Python {}'.format('rules!'))

# List
fcs = ['afc', 'lfc', 'cfc', 'mufc', 'mcfc']
fcs.append('spurs')
fcs.remove('cfc')
fcs.pop(3)
print(fcs)

#Sorting
numlist = [2,3,4,1]
numlist.sort()
print(numlist)
mylist = [1,3,2,4,6,5]
mylist.reverse()
print(mylist)

#Dictionary

pl_clubs = {'MC': 1, 'Lpool': 2, 'CFC': 3}
print(pl_clubs['MC'])
pl_clubs['Lpool'] = 1
print(pl_clubs)
d={'k1':[1,2,3]}
print(d['k1'][1])

#Tuples

t = (1,2,3)
print(type(t))