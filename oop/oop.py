class animal:
	def __init__(self,name,color,age,size):
		self.name=name
		self.color=color
		self.age=age
		self.size=size
		 
	def printall(self):
		print (self.name)
		print (self.color)
		print (self.age)
		print (self.size)
		 
	def sleeping(self):
		 print(self.name +" " +"is sleeping")
	def eating(self,food):
		 print(self.name +" " +"is eating"+" " + food)


dog=animal(name="Joe",color="yellow",age=100,size="huge")
bird=animal(name="Katy",color="blue",age=1,size="tiny")
zebra=animal(name="Marty",color="black & white",age=5,size="medium")
lion=animal(name="Alex",color="orange & red",age=7,size="big")

lion.printall()
lion.sleeping()
lion.eating("bone")
print ("       ")
bird.printall()
bird.sleeping()
bird.eating("leaf")
print ("       ")
zebra.printall()
zebra.sleeping()
zebra.eating("grass")
 
