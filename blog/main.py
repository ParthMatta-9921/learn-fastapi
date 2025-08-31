from fastapi import FastAPI,Depends,status,HTTPException as HTTPE
from schemas import Blog,BlogShow,User,ShowUser,BlogResponse #. means same directory .. parent directory
from models import Blog as BlogModel,User as UserModel #to avoid name conflict
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from hashing import Hash
app = FastAPI()# this is an instance of FastAPI
#needs to be a pydantic field type or model
#Blog is for schemas and used for requests to communicate between client and server/front end to back end
#BlogModel is for the database and used for ORM (Object Relational Mapping) and as the oject for the db to connect to
#where the data is stored as. this is basically a table no not basically literally a table



#not secure at all as easily the front end is able to communicate with the db so there will be changes to make it secure in further commits not the 3rd one
#ORM means object-relational mapping so thta it map object to a field of a db table. a class becomes a table
BlogModel.metadata.create_all(bind=engine)#creates the table in the database and only one time and not every tiem it is reloaded a new table is created no sireee

# request means whatever we get from browser/client so schemas is for front end and models is for back end

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#If you declare both a return type and a response_model, the response_model will take priority and be used by FastAPI.
#201 for creating something
@app.post("/blog",status_code=status.HTTP_201_CREATED,tags=["blogs"])#tags for documentation and easy seeing shit and all
#never do like this this sucks ass these are query parametwers so we gonna create pydfamnmtic models to make it easy
#def create(title,body):
#   return {"title":title,"body":body}
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog= BlogModel(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.delete("/blog/{blog_id}",status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
def delete_blog(blog_id:int,db:Session=Depends(get_db)):
    blog=db.query(BlogModel).filter(BlogModel.id==blog_id).first()
    #blog=db.query(BlogModel).filter(BlogModel.id==blog_id).delete(synchronize_session=False) #so no need for db.delete()
    if not blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    db.delete(blog)
    db.commit()
    #db.refresh(blog)
    #return {"done"}


# update means you have to update all of it, there will be a patch too or partial update i hope so otherwise i will do it
@app.put("/blog/{blog_id}",status_code=status.HTTP_200_OK,tags=["blogs"])
def update_blog(blog_id:int,request:Blog,db:Session=Depends(get_db)):# Blog is from schemas
    #up_blog=db.query(BlogModel).filter(BlogModel.id==blog_id).first()
    up_blog=db.query(BlogModel).filter(BlogModel.id==blog_id).first()
    if not up_blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    up_blog.title=request.title
    up_blog.body=request.body

    #up_blog.update(request)# also an alternative
    db.commit()
    #db.refresh(up_blog) # as using update here and not filter only
    #return up_blog
    return 'updated'





@app.get("/blog",response_model=List[BlogResponse],tags=["blogs"],status_code=status.HTTP_200_OK)# all the blogs coming towards me/client
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs

#blogshow is schema 
@app.get("/blog/{blog_id}",status_code=status.HTTP_200_OK,response_model=BlogShow,tags=["blogs"])#1 blog will be there for me/client
def get_blog(blog_id:int, db:Session=Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id==blog_id).first()#filter is basically where clause
    if not blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    # response:Response in the parameters of the get_blog was used for this
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog with id {blog_id} not found"}
    return blog



@app.post("/user",response_model=ShowUser,tags=["Users"])
def create_user(request: User,db:Session=Depends(get_db)):

    new_user=UserModel(username=request.username,
                       email=request.email,
                       password=Hash.encrypt(request.password))
    #have to manually assign or use some bullshit **request.dict()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)#means we can see the db has new data that is deposited
    return new_user


@app.get("/user/{user_id}",response_model=ShowUser,tags=["Users"])
def get_user(user_id: int, db: Session=Depends(get_db)):
    user=db.query(UserModel).filter(UserModel.id==user_id).first()
    if not user:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
    return user
# # Convert ORM objects to Pydantic models
#     user_data = ShowUser(
#         username=user.username,
#         email=user.email, # from_orm converts orm objects into pydantic models like Blog
#         blogs=[Blog.from_orm(blog) for blog in user.blogs]  # Convert blogs to Pydantic models
#     )