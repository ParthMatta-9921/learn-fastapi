from pydantic import BaseModel
from typing import List,Optional

# these are pydantic models and the models in models.py are database models

class Blog(BaseModel):
    title: str
    body: str

class BlogResponse(BaseModel):
    id: int
    title: str
    body: str
    class Config(): # for converting to orm object to json
        #OR USED FOR ONLY MAKING THE SCHEMAS SHIT TAKE FROM THE DB AND NOT THE WHOLE DB ROW
        from_attributes = True
class User(BaseModel):
    username: str
    email: str
    password:str
    #bio: Optional[str] = None

class ShowUser(BaseModel):
    username: str
    email: str
    blogs:List[Blog]=[]
    class Config(): # for converting to orm object to json
        from_attributes = True

class UserResponse(BaseModel):
    username: str
    email: str
    class Config(): # for converting to orm object to json
        from_attributes = True


# class BlogUpdate(BaseModel):
#     title: Optional[str] = None
#     body: Optional[str] = None
    
class BlogShow(BaseModel):
    # i only need title and body to be shown in show get method so it willuse from parent blog
    title: str
    body: str
    creator: UserResponse
    class Config(): # for converting to orm object to json
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str       



#Tokens bitches

class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel):
    username: Optional[str] = None