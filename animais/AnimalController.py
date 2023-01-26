from fastapi import APIRouter, Body

from animais.AnimalRequest import AnimalRequest
from animais.AnimalResponse import animalLista

router = APIRouter(
    prefix="/animais",
)

@router.get('')
async def getAllAnimais():
    return animalLista

@router.get('/{animalID}')
async def getOneAnimalByID(animalID: int):
    for indice, animal in enumerate(animalLista):
        if animal.ID == animalID:
            return animal

    return animalLista

@router.post('')
async def insertAnimal(animalRequest: AnimalRequest = Body(...)):
    animalLista.append(animalRequest)
    return animalLista

@router.put('')
async def updateAnimal(animalRequest: AnimalRequest = Body(...)):
    for indice, animal in enumerate(animalLista):
        if animal.ID == animalRequest.ID:
            animalLista[indice] = animalRequest

    return animalLista

@router.delete('/{animalID}')
async def deleteAnimal(animalID: int):
    for indice, animal in enumerate(animalLista):
        if animal.ID == animalID:
            del animalLista[indice]

    return animalLista

