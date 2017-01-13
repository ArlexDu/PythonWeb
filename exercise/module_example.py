'''
from datetime import datetime,timedelta,timezone

#get time
now = datetime.now()
print(now)

#set time
dt = datetime(2017,1,13,14,50)
print(dt)

timestamp = dt.timestamp()
print(timestamp)

da = datetime.fromtimestamp(timestamp)
print(da)

utc_da  =datetime.utcfromtimestamp(timestamp)
print(utc_da)

cday = datetime.strptime('2017-1-13 15:01:00','%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%A, %b-%d %H:%M'))

ct = now + timedelta(hours = 10)

print(ct)

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)
'''
'''
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('x is %s y is %s' % (p.x,p.y))

'''
'''
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
'''
'''
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
'''
import struct
struct.pack('>I',10240099)
