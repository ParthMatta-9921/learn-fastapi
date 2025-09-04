# FOR AUTHENITICATION
from fastapi import APIRouter,Depends,status,HTTPException as HTTPE
from sqlalchemy.orm import Session
from database import get_db
from schemas import Login, ShowUser
from models import User as UserModel
from hashing import Hash
router=APIRouter( prefix="/auth", tags=["auth"] )


@router.post("/login",response_model=ShowUser)
def login(request:Login, db:Session=Depends(get_db)):
    # username is being used as 0auth2passswordrequestform needed username not email but we can use email from the backend 
    # it's just username is going to be used in the front end amd we can just say enter email in the username field
    # so no issues
    user=db.query(UserModel).filter(UserModel.email==request.username).first()
    if not user: #or user.password != Hash.encrypt(request.password):# meaning if user not found or password does not match
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    #check for password
    if not Hash.verify(user.password,request.password):
        raise HTTPE(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrrect Password")
    #generate a jwt token and return 
    return user
