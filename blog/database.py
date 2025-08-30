from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base# for declaring a mapping
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL='sqlite:///../blog.db'# this is not secure

#engine=create_engine('sqlite:///:memory:',echo=True)#stores in memory but we gonna store in blog.db so lets look into that
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal= sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()
