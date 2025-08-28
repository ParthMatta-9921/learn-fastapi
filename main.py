from fastapi import FastAPI
from typing import Optional
# uvircorn with relaod meansd automatic reload
app = FastAPI()# this is an instance of FastAPI

@app.get('/blog')# slash means base url
# ? means query parameters ?limit=10&published=true
def index(published:bool=True, limit:int=10, sort: Optional[str]=None):
    #only get 10 published blogs
    #return published
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit}  blogs from the db'}





@app.get("/blog/unpublished")
def unpublished():
    #fetch unpublished blogs
    return {'data':"unpublished blogs"}


# data validation doen by pydantic
@app.get("/blog/{id}")# app called apth op decrator get is the operation and the function beneath is path op function
# ansd slash and about are path for the website
#for dynmaic routing use {name of parameter}
def show(id:int):
    #fetch blog with id=id
    return {'data':id}

#cant keep this here as interpreated so line b line so will after /blog {id} method gets called
#and no blog/unpublished so move it above blog/{id}
'''@app.get("/blog/unpublished")
def unpublished():
    #fetch unpublished blogs
    return {'data':"unpublished blogs"}'''
@app.get("/blog/{id}/comments") # if {} ijn path then menss path parameetr and not query parameter
def get_comments(id:int,limit:int=10):
    #fetch comments for blog with id=id
    #return limit
    return {'data':"comments for blog {}".format(id), 'comments':['1','2']}