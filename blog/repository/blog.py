from sqlalchemy.orm import Session 
from models import Blog as BlogModel
from schemas import Blog
from fastapi import status,HTTPException as HTTPE

def get_all(db:Session):
    blogs = db.query(BlogModel).all()
    return blogs

def get_id_repo(db :Session,blog_id:int):
    blog = db.query(BlogModel).filter(BlogModel.id==blog_id).first()#filter is basically where clause
    if not blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    # response:Response in the parameters of the get_blog was used for this
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog with id {blog_id} not found"}
    return blog
def create_repo(db:Session,request: Blog):
    new_blog= BlogModel(title=request.title,body=request.body,user_id=1)#id is hard coded right now need to change
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_repo(db:Session,blog_id:int):
    blog=db.query(BlogModel).filter(BlogModel.id==blog_id).first()
    #blog=db.query(BlogModel).filter(BlogModel.id==blog_id).delete(synchronize_session=False) #so no need for db.delete()
    if not blog:
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {blog_id} not found")
    db.delete(blog)
    db.commit()
    #db.refresh(blog)
    #return {"done"}

def update_repo(db:Session,blog_id: int,request: Blog):
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

