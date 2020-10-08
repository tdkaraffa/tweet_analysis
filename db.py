def db():
	import sqlalchemy
	from secret import get_db_conn
	engine = sqlalchemy.create_engine(get_db_conn())
	engine.connect()

	date_values = ['Thu', 'Oct', '08', '02:06:32', '+0000', '2020']
	month = date_values[1]
	year = date_values[-1]
	day = date_values[2]
	date = f'{year}-{month}-{day}'
	statement = f'''INSERT INTO twitter.tweets (id, text, date) VALUES (10, 'ugh', CAST('{date}' AS DATE));'''
	engine.execute(statement)

db()