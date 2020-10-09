def insert_data_into_db(data, schema, table, db_conn):
	from sqlalchemy import Table, MetaData, create_engine
	import sqlalchemy
	engine = create_engine(db_conn)
	conn = engine.connect()
	metadata = MetaData()
	table = Table(table, metadata, autoload_with=engine, schema=schema)
	#tweets_table = Table('tweets', metadata, autoload_with=engine, schema='twitter')

	conn.execute(table.insert(), data)




	# date_values = ['Thu', 'Oct', '08', '02:06:32', '+0000', '2020']
	# month = date_values[1]
	# year = date_values[-1]
	# day = date_values[2]
	# date = f'{year}-{month}-{day}'
	#
	# s = .update().\
	# 	where
	# statement = f'''INSERT INTO twitter.tweets (id, text, date) VALUES (10, 'ugh', CAST('{date}' AS DATE));'''
	# engine.execute(statement)