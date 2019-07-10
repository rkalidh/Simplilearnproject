#!/usr/bin/env python
import sqlalchemy
import os
import json
from sqlalchemy import *
from sqlalchemy.orm.session import sessionmaker
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey, ForeignKeyConstraint
os.chdir("/app")
db=create_engine('sqlite:///userlogin.db')
metadata=MetaData()
metadata.bind=db
conn=db.connect()
Session=sessionmaker(bind=db)
session=Session()
#Newusers=Table('userdata',metadata,
        #Column ('user-id',Integer,primary_key=True,nullable=False),
        #Column ('username',String(40),nullable=False),
        #Column('password',String(40),nullable=False),
        #Column('active',Integer)
        #)
#Newusers.create()
#ins=Newusers.insert()
result=conn.execute('''select * from userdata''')
for row in result:
    print(row)
session.commit()
