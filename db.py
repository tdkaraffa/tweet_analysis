def insert_data_into_db(data, schema, table, db_conn):
	from sqlalchemy import Table, MetaData, create_engine
	engine = create_engine(db_conn)
	conn = engine.connect()
	metadata = MetaData()
	table = Table(table, metadata, autoload_with=engine, schema=schema)
	conn.execute(table.insert(), data)