from fastapi import FastAPI
from .schemas import Blog #. means same directory
app = FastAPI()# this is an instance of FastAPI
#needs to be a pydantic field type or model


@app.post("/blog")
#nevber do like this this sucks ass as thesea re query parametwers so we gonna create pydfamnmtic models to make it easy
#def create(title,body):
#   return {"title":title,"body":body}
def create(blog:Blog):
    return {"title":blog.title,"body":blog.body}