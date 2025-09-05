# FOR AUTHENITICATION so login
from fastapi import APIRouter,Depends,status,HTTPException as HTTPE
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from schemas import Login, ShowUser
from models import User as UserModel
from hashing import Hash



router=APIRouter( prefix="/auth", tags=["auth"] )
from auth_token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta


@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    # username is being used as 0auth2passswordrequestform needed username not email but we can use email from the backend 
    # it's just username is going to be used in the front end amd we can just say enter email in the username field
    # so no issues
    user=db.query(UserModel).filter(UserModel.email==request.username).first()
    if not user: #or user.password != Hash.encrypt(request.password):# meaning if user not found or password does not match
        raise HTTPE(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    #check for password
    if not Hash.verify(user.password,request.password):
        raise HTTPE(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrrect Password")
    #generate a jwt token and return
    access_token_expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)#expire time is optional but i am going to give it anyway
    return {"access_token": access_token,"token_type":"bearer"}