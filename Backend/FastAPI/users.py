from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User("Agus", "Juarez", "https://moure.dev", 23),
              User("Alejandro", "Suarez", "https://mouredev.dev", 20),
              User("Alan", "Gomez", "https://alan.dev", 43)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Agus" , "surname":"Juarez", "url": "https://moure.dev", "age" : 23},
            {"name": "Alejandro" , "surname":"Suarez", "url": "https://mouredev.dev", "age" : 20},
            {"name": "Alan" , "surname":"Gomez", "url": "https://alan.com", "age" : 43},]

@app.get("/users") 
async def users():
    return users_list
