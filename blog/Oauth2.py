#security bitches 
#put all routes after authentication here
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from sqlalchemy.orm import Session
from models import User as UserModel
from database import get_db
from auth_token import SECRET_KEY,ALGORITHM,verify_token

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")# this is the url where the user will send the username and password to get the token
def get_current_user(token:str=Depends(oauth2_scheme),db: Session=Depends(get_db)):

    return verify_token(db, token)

