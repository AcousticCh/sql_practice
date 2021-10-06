#!usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
DB_LINK = 'sqlite:///bookstore.db'

metadata = MetaData()
controller = create_engine(DB_LINK, echo = True)
books = Table("books", metadata,
	Column("id", Integer, primary_key = True),
	Column("title", String),
	Column("primary_author", String),
	)

metadata.create_all(controller)

CON = controller.connect()

data = ({ "id": 4, "title": "The Hobbit", "primary_author": "Tolkien" },
		{ "id": 6, "title": "The Silmarillion", "primary_author": "it works" },
	)

BOOKS_INS = books.insert()
BOOKS_ADD = CON.execute(BOOKS_INS, data[1])
books_sel = select(books)

result = CON.execute(books_sel)

for row in result:
	print(row)

	
	
	
