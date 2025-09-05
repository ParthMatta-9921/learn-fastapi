from fastapi import APIRouter,Depends,status
from schemas import Blog,BlogShow,User
from models import User as UserModel
from typing import List,Optional
from sqlalchemy.orm import Session
from database import get_db
from repository.blog import get_all,create_repo,delete_repo,update_repo,get_id_repo
from Oauth2 import get_current_user
# i am a moron that should hae just imported all the module fucntions and classes and not just selective ones as it becomes 
#difficult to read the code without going up again

router=APIRouter( prefix="/blog", tags=["blogs"] )
#only need to define tags one time here
#tags for documentation and easy seeing shit and all
# also prefix means so we dont have to write /blog everytime in the routes and we need to only do it one time and
#if we want to go in deeper then we can go easily


@router.get("/",response_model=List[BlogShow],status_code=status.HTTP_200_OK)# all the blogs coming towards me/client
def get_all_blogs(db:Session=Depends(get_db),current_user: User=Depends(get_current_user)):
    # this one should not be able to be used by ay other user or should it,is it a priavte journal thing or an actual blog website so #
    # have to do all blogs with the users as well then
    return get_all(db)

#blogshow is schema 
@router.get("/{blog_id}",status_code=status.HTTP_200_OK,response_model=BlogShow)#1 blog will be there for me/client
def get_blog(blog_id:int, db:Session=Depends(get_db), current_user: UserModel=Depends(get_current_user)):
    # i am not really using current_user as it is only there for authorisation purposes
    return get_id_repo(db,blog_id)



#If you declare both a return type and a response_model, the response_model will take priority and be used by FastAPI.
#201 for creating something
@router.post("/",status_code=status.HTTP_201_CREATED)
#never do like this this sucks ass these are query parametwers so we gonna create pydfamnmtic models to make it easy
#def create(title,body):
#   return {"title":title,"body":body}
def create(request:Blog,db:Session=Depends(get_db),current_user: UserModel=Depends(get_current_user)):

    return create_repo(db,request,current_user.id)



@router.delete("/{blog_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id:int,db:Session=Depends(get_db),current_user: UserModel=Depends(get_current_user)):
    # i am not really using current_user as it is only there for authorisation purposes
    return delete_repo(db,blog_id)




# update means you have to update all of it, there will be a patch too or partial update i hope so otherwise i will do it
@router.put("/{blog_id}",status_code=status.HTTP_200_OK)
def update_blog(blog_id:int,request:Blog,db:Session=Depends(get_db),current_user: UserModel=Depends(get_current_user)):# Blog is from schemas
    # i am not really using current_user as it is only there for authorisation purposes
    return update_repo(db,blog_id,request)


