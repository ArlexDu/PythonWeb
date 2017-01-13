import re

em_exp =r'[0-9a-zA-Z\_\.]+\@[0-9a-zA-Z\_\.]+[\.com]$'
email = 'someone@gmail.com'
if re.match(em_exp,email):
	print('ok')
else:
	print('failed')

re_name  = re.compile(r'\<(\w+\s?\w+)>\s(\w+\_?\.?\w+\@\w+\.\w+)')
result = re_name.match('<Arlex Du> arlex@sap.com').groups()
#result = re.match(r'^(\d+?)(0*)$', '102300').groups()
for i in result:
	print(i)
