from sqlalchemy.orm import Session
from models import User as UserModel #to avoid name conflict
from schemas import User
from hashing import Hash
from fastapi import HTTPException as HTTPE,status
def create_user_repo(db:Session,request: User):
    new_user=UserModel(username=request.username,
                       email=request.email,
                       password=Hash.encrypt(request.password))
    #have to manually assign or use some bullshit **request.dict()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)#means we can see the db has new data that is deposited
    return new_user


def get_user_repo(db: Session, user_id: int):
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