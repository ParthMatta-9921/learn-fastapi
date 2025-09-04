from fastapi import FastAPI
#. means same directory .. parent directory
from models import Base
from database import engine
from routers import blog,user,auth
app = FastAPI()# this is an instance of FastAPI
#needs to be a pydantic field type or model
#Blog is for schemas and used for requests to communicate between client and server/front end to back end
#BlogModel is for the database and used for ORM (Object Relational Mapping) and as the oject for the db to connect to
#where the data is stored as. this is basically a table no not basically literally a table



#not secure at all as easily the front end is able to communicate with the db so there will be changes to make it secure in further commits not the 3rd one
#ORM means object-relational mapping so thta it map object to a field of a db table. a class becomes a table
Base.metadata.create_all(bind=engine)#creates the table in the database and only one time and not every tiem it is reloaded a new table is created no sireee

# request means whatever we get from browser/client so schemas is for front end and models is for back end

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app.title="My FastAPI Application-Blog Bitches"  
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)






