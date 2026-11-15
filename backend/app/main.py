#Acá está todo el rollo de la API

from fastapi import FastAPI


app = FastAPI(
    title="RAG-Programación IV",
    description="API para el proyecto de RAG-Programación IV",
    version="1.0"
)

@app.get("/activo")
def check_activo():
    return {"status": "API activa y funcionando correctamente"}