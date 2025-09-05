SECRET_KEY="8f8013d109d2d9be4f371ce99095b11b4c6710610390713700d0facdaa5ddba7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
from datetime import datetime, timedelta,UTC
from typing import Optional 
from jose import JWTError, jwt
from fastapi import HTTPException as HTTPE,status
from schemas import TokenData
from sqlalchemy.orm import Session
from models import User as UserModel
#jwt is json web token

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):#expires_delta is time that is given to expire for a token
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire,"sub":data.get("sub")})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 



def verify_token(db:Session, token:str):# i hve alread done the scheme here so no need to do it here when alreadyt done in Oauth2.py
    
    credentials_exception=HTTPE(status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="could not validate credentials",
                    headers={"WWW-Authenticate":"Bearer"})
    
    
    try:
        # Optional[str] is equal to union[str,None] meaning it can be string or None
        #payload is a dictionary here so we using get to get data from key sub
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email_auth:Optional[str]=payload.get("sub")#as username is not being used here but email
        #also can use payload.get("sub","") this is giving default value so it comes off as string and not None
        if email_auth is None: #email is None
            raise credentials_exception
        user = db.query(UserModel).filter(UserModel.email == email_auth).first()
        if user is None:
            raise credentials_exception
        return user #have to return user for get_current_user
    except JWTError:
        raise credentials_exception