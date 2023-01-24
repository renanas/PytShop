
from fastapi import Depends, APIRouter, Request, Body

from .ClienteRequest import ClienteRequest
from .ClienteResponse import clientesLista

router = APIRouter(
    prefix="/clientes",
)

@router.get('')
async def getAllClientes():
    return clientesLista

@router.get('/{clientId}')
async def getOneCliente(clientId: int):
    for indice, cliente in enumerate(clientesLista):
        if cliente.ID == clientId:
            return clientesLista[indice]
    return clientesLista

@router.post('')
async def insertCliente(clienteRequest: ClienteRequest = Body(...)):
    clientesLista.append(clienteRequest)
    return clientesLista

@router.put('')
async def updateCliente(clienteRequest: ClienteRequest = Body(...)):
    for indice, cliente in enumerate(clientesLista):
        if cliente.ID == clienteRequest.ID:
            clientesLista[indice] = clienteRequest
    return clientesLista

@router.delete('/{clientId}')
async def deleteClienteById(clientId: int):
    for indice, cliente in enumerate(clientesLista):
        if cliente.ID == clientId:
            del clientesLista[indice]
    return clientesLista
