# Writing a function

def leng_func(line):
	ss = len(line)
	return ss

print (leng_func('arsenal'))

# Writing a function

def colo_func(color, club = 'mc'):
	return 'You like {}, and you support {}' .format(color, club)

print (colo_func('red'))