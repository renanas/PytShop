from pydantic import BaseModel

class ClienteRequest(BaseModel):
    ID: int
    nome: str
    genero: str
    idade: int
    altura: float
    #aniamis: Animal

