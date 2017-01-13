class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name,self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

# s1 = Student('Happy',90)
# s1.print_score()
# print(s1.get_grade())

class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be integer!')
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('height must be integer!')
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 19
s.height = 20
print(s.resolution)

