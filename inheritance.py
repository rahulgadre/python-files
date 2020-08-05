class Parent():
  
	def lastname(self):
		print('Gadre')

class Child(Parent):
	def firstname(self):
		print('Rahul')        
        
chi = Child()
chi.firstname()
chi.lastname()