from fastapi import APIRouter,Depends,status
from schemas import ShowUser,User,UserResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User as UserModel
from repository.user import create_user_repo,get_user_repo
from Oauth2 import get_current_user
router=APIRouter( prefix="/user", tags=["users"] )
#only need to define tags one time here
# also prefix means so we dont have to write /user everytime in the routes and we need to only do it one time and
#if we want to go in deeper then we can go easily

@router.post("/",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(request: User,db:Session=Depends(get_db)):

    return create_user_repo(db,request)
    


@router.get("/{user_id}",response_model=ShowUser,status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session=Depends(get_db),current_user: UserModel=Depends(get_current_user)):

    return get_user_repo(db,user_id)

# would love to add search function next from username