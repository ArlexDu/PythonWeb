import functools

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

#print(fact(5))

def move(n,a,b,c):
	if n==1:
		print(a,"-->",c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
#move(5,'A','B','C')

#L = list(range(100))
#print(L[:10])
#print(L[-10:-1])
#print(L[1:10:2])
#S = 'ABCDEFGHIGK'
#print(S[:3])

#L = [x*x for x in range(1,11) if x%2 == 0]
#print(L)

#L1 = ['Hello','World',18,'Apple',None]
#L2 = [s.lower() for s in L1 if isinstance(s,str)]
#print(L2)

#g = (x*x for x in range(1,11))
#for x in g:
#	print(x)

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		#print(b)
		yield b
		a,b = b,a+b
		n = n+1
	return 'done'
#f = fib(10)
#for x in f:
#	print(x)

#杨辉三角形
# def triangles():~
# 	n,L = 1,[1]
# 	while True:
# 		if n == 1:
# 			yield L
# 		else:
# 			L = [L[i-1]+L[i] for i in range(1,n-1)]
# 			L = [1]+L+[1]
# 			yield L
# 		n += 1
# n = 0
# for t  in triangles():
# 	print(t)
# 	n+=1
# 	if n == 10:
# 		break

#高阶函数
# def add(a,b,f):
# 	return f(a)+f(b)
# print(add(1,-10,abs))

# def normalize(name):
# 	n_name =name[:1].upper()+name[1:len(name)].lower()
# 	return n_name

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize,L1))
# print(L2)

# def power(x,y):
# 	return x*y

# def pord(L):
# 	S = reduce(power,L)
# 	return S
# print('3 * 5 * 7 * 9 = ',pord([3,5,7,9]))

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def getnum(x,y):
	return 10 * x + y

def str2float(s):
	L = s.split('.')
	R1 = reduce(getnum,map(char2num,L[0]))
	wei = len(L[1])
	R2 = reduce(getnum,map(char2num,L[1]))
	R3 = R1 + R2/(10**wei)
	return R3

# print('str2float(\'123.456\') =', str2float('123.456'))

def decorator(info = None):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if info is not None:
                print('%s%s()'%(info,func.__name__))
                func(*args,**kw)
                print('%s%s()'%(info,func.__name__))
            else:
                print('begin call%s()'%func.__name__)
                func(*args,**kw)
                print('end call%s()'%func.__name__)
        return wrapper
    return log

@decorator()
def gettime():
	print(" 2017.1.10 ")
	return

gettime()


