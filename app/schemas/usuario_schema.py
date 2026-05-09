from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class Login(BaseModel):
    email: str
    senha: str
