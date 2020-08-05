with open('file.txt', mode = 'r') as f:
	print (f.read())

with open('file.txt', mode = 'a') as f:
	f.write('\nsnow - the king of the north')

with open('file.txt', mode = 'r') as f:
	print (f.read())
