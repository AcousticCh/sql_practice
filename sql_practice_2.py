#!usr/bin/env pyhton3
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select

#make metadata object and engine object
met = MetaData()
controller = create_engine("sqlite:///user_db.db")
# create table objects, Table() takes (<name>, metadata, **Column())
users = Table("users", met,
	Column("id", Integer, primary_key = True),
	Column("name", String),
	Column("fullname", String),
	)
	
num_of_emails = Table("addresses", met,
	Column("id", Integer, primary_key = True),
	Column("user_id", None, ForeignKey("users.id")),
	Column("email_address", String, nullable = False),
	)
# create actual engine and database
met.create_all(controller)

ins = users.insert() # .values(name = "Jack", fullname = "Jack Birch")
con = controller.connect()
add = con.execute(ins, {"id": 5, "name": "Elise", "fullname": "Elise Veroke"})
sel = select(users)

result = con.execute(sel)
for row in result:
	print(row)
