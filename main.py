from fastapi import FastAPI

# uvircorn with relaod meansd automatic reload
app = FastAPI()

@app.get("/")# slash means base url
def index():
    return {'data':{'name':'John Doe'}}

@app.get("/about")
def about():
    return {'data':{'about page'}}