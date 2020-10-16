def insert_data_into_db(data, schema, table, db_conn):
	from sqlalchemy import Table, MetaData, create_engine
	from sqlalchemy.dialects.postgresql import insert

	engine = create_engine(db_conn)
	conn = engine.connect()
	metadata = MetaData()
	table = Table(table, metadata, autoload_with=engine, schema=schema)
	insert_table = insert(table).values(data)
	insert_or_ignore_table = insert_table.on_conflict_do_nothing()
	conn.execute(insert_or_ignore_table)