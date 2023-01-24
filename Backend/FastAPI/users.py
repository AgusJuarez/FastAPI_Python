from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Agus", surname = "Juarez", url = "https://moure.dev", age = 23),
              User(id = 2, name = "Alejandro", surname = "Suarez", url = "https://mouredev.dev", age = 20),
              User(id = 3, name = "Alan", surname = "Gomez", url = "https://alan.dev", age = 43)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Agus" , "surname":"Juarez", "url": "https://moure.dev", "age" : 23},
            {"name": "Alejandro" , "surname":"Suarez", "url": "https://mouredev.dev", "age" : 20},
            {"name": "Alan" , "surname":"Gomez", "url": "https://alan.com", "age" : 43},]

@app.get("/users") 
async def users():
    return users_list

#Por PATH
@app.get("/user/{id}") 
async def user(id: int):
    return search_user(id)

#Por Query
@app.get("/user/") 
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

