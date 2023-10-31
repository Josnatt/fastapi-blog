from fastapi import FastAPI

#Instanciar fastapi
app = FastAPI()
app.title = "BlogApp"
app.version = "1.0.1"
app.description = "Este en un sevidor para un Blog"

#Crear la ruta raiz
@app.get("/", tags=["Inicio"])
async def welcome():
    return {"message": "Entrada a la ruta raiz con fastapi"}

