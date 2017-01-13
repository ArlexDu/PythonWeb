# import chardet
# def openfile():
# 	tt =open('C:\\Users\\I321258\\Desktop\\123.txt','rb')
# 	ff = tt.readline()
# 	enc = chardet.detect(ff)
# 	print (enc['encoding'])
# 	tt.close()
# openfile()

import json
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob',20,100)
print(s.__dict__)

print(json.dumps(s,default=lambda obj:obj.__dict__))