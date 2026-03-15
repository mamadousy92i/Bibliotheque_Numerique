from pydantic import BaseModel


class LivreBase(BaseModel):
    titre: str
    auteur: str
    annee_publication: int
    isbn: str

class LivreCreate(LivreBase):
    pass

class Livre(LivreBase):
    id: int

    class Config:
        orm_mode = True 