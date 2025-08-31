from pydantic import BaseModel
from typing import Optional

# these are pydamtic models and the models in models.py are database models
class Blog(BaseModel):
    title: str
    body: str

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None\
    
class BlogShow(Blog):
    # i only need title and body to be shown in show get method so it willuse from parent blog
    class Config(): # for converting to orm object to json
        from_attributes = True


class User(BaseModel):
    username: str
    email: str
    password:str
    #bio: Optional[str] = None
