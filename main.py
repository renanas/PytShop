# IMPORTS
from fastapi import FastAPI
import clientes
from clientes import ClienteController

app = FastAPI()

print('route /client GET')
app.include_router(clientes.ClienteController.router)

print('route /animal GET')
#app.register_blueprint(animal_ct, url_prefix='/animal')
