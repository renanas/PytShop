# IMPORTS
from fastapi import FastAPI
import clientes
from clientes import ClienteController
import animais
from animais import AnimalController

app = FastAPI()

app.include_router(clientes.ClienteController.router)
app.include_router(animais.AnimalController.router)

