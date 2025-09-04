SECRET_KEY="8f8013d109d2d9be4f371ce99095b11b4c6710610390713700d0facdaa5ddba7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
from datetime import datetime, timedelta,UTC
from typing import Optional 
from jose import JWTError, jwt

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):#expires_delta is time that is given to expire for a token
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt