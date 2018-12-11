from sqlalchemy import Column,String,create_engine,INT,CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
class Departments(object):
    __tablename__ = 'departments'
    dept_no = Column(CHAR(4),primary_key=True)
    dept_name = Column(String(40))

engine = create_engine('mysql+mysqlconnector://root:Zeng123+@localhost:3306/employees')
DBSession = sessionmaker(bind=engine)
session = DBSession()

k = session.query(Departments).limit(1)