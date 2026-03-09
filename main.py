from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
{"title": "favourite foods", "content": "I like pizza", "id": 2}]   

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}

# @app.get("/posts")
# def get_posts():
#     return {"data": "this is my get posts data"}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

@app.post("/posts")
def create_posts(post: Post):
    #print(post)
    #print(post.dict())
    #print(post.model_dump())
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(id)
    print(post)
    return{"post_detail": post}

@app.get("/posts/updates/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}