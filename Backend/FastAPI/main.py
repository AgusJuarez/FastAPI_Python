from fastapi import FastAPI
from routers import products, users, users_db, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

#El servidor se inicia con: uvicorn main:app --reload
#Para detenerlo: CTRL + C

#Documentacion con Swagger: http://127.0.0.1/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc

#url local 127.0.0.1:8000
app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#Recursos estaticos
app.mount("/static", StaticFiles(directory="static"), name="static")
 


@app.get("/")
async def root():
    return "¡Hola FastAPI!"
   
@app.get("/url")
async def root():
    return { "url_curso" : "https://mouredev.com/python" }