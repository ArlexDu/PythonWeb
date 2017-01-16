import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
 	os.remove(db_file)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Arlex',95)")
cursor.execute(r"insert into user values ('A-002','Altynai',72)")
cursor.execute(r"insert into user values ('A-003','Happy',88)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
	try:
		conn  = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("select name from user where score between %s and %s order by score desc" % (low,high))
		values = cursor.fetchall()
	finally:
		cursor.close()
		conn.close()
	return [x[0] for x in values]

assert get_score_in(90, 95) == ['Arlex'], get_score_in(90, 95)
assert get_score_in(60, 90) == ['Happy', 'Altynai'], get_score_in(60, 90)
assert get_score_in(60, 100) == ['Arlex', 'Happy', 'Altynai'], get_score_in(60, 100)
