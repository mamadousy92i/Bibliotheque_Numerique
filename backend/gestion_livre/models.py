from sqlalchemy import Column, column, Integer, String
from database import Base


class Livre(Base):
    __tablename__ = "livres"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    auteur = Column(String, index=True)
    year = Column(Integer, index=True)
    isbn = Column(String, index=True)

