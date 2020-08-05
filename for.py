# For loop
city = ["Denver","Colorado Springs","Boulder","Lone Tree","Broomfield","Fort Collins"]

for i in city:
	print(i)
	print(len(i))

# For loop

for i in range(1, 5):
	print(i)

# For loop with continue

numbers = [1, 2, 5, 8, 11, 13, 17, 19, 20]

for n in range(20):
	if n in numbers: 
		continue 
	print (n)

# For loop with break
t = 20

for t in range(18, 25):
	print(t)
	t += 1
	if t == 23:
		break	

# While loop

x = 10

while x < 15:
	print(x)
	x += 1