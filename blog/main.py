from fastapi import FastAPI,Depends,status,Response,HTTPException as HTTPE
from schemas import Blog #. means same directory .. parent directory
from models import Blog as BlogModel #to avoid name conflict
from database import engine,SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()# this is an instance of FastAPI
#needs to be a pydantic field type or model


#ORM means object-relational mapping so thta it map object to a field of a db table. a class becomes a table
BlogModel.metadata.create_all(bind=engine)#creates the table in the database



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


#201 for creating something
@app.post("/blog",status_code=status.HTTP_201_CREATED)
#never do like this this sucks ass these are query parametwers so we gonna create pydfamnmtic models to make it easy
#def create(title,body):
#   return {"title":title,"body":body}
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog= BlogModel(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get("/blog")
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs


@app.get("/blog/{blog_id}",status_code=status.HTTP_200_OK)
def get_blog(blog_id:int,response : Response, db:Session=Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id==blog_id).first()#filter is basically where clause
    if not blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog with id {blog_id} not found"}
    return blog

