########## Users DB API #########

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/userdb",
                   tags= ["usersdb"],
                   responses={404: {"message":"No encontrado"}})

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



@router.get("/") 
async def users():
    return users_list

#Por PATH
@router.get("/{id}") 
async def user(id: int):
    return search_user(id)

'''#Por Query
@router.get("/user/") 
async def user(id: int):
    return search_user(id)'''

 


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code=204, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user


@router.put("/", response_model=User, status_code=200)
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        return user


@router.delete("/{id}") #por Path
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}




