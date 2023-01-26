from pydantic import BaseModel


class AnimalRequest(BaseModel):
    ID: int
    tipo: str
    nome: str
    raca: str
    genero: int
    idade: int
