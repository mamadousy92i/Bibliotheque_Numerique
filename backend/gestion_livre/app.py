from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, declarative_base
import models, schemas, crud,database 
from database  import SessionLocal, engine, Base
Base = declarative_base()

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Livres")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1- Ajouter un livre
@app.post("/livres/", response_model=schemas.Livre)
def create_livre(livre: schemas.LivreCreate, db: Session = Depends(get_db)):
    nouveau_livre = models.Livre(title=livre.titre, auteur=livre.auteur, year=livre.annee_publication)
    db.add(nouveau_livre)
    db.commit()
    db.refresh(nouveau_livre)
    return nouveau_livre

# 2- Modifier un livre
@app.put("/livres/{livre_id}", response_model=schemas.Livre)
def update_livre(livre_id: int, livre: schemas.LivreCreate, db: Session = Depends(get_db)):
    livre_existant = db.query(models.Livre).filter(models.Livre.id == livre_id).first()
    if not livre_existant:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    livre_existant.title = livre.titre
    livre_existant.auteur = livre.auteur
    livre_existant.year = livre.annee_publication
    db.commit()
    db.refresh(livre_existant)
    return livre_existant

# 3- Supprimer un livre
@app.delete("/livres/{livre_id}")
def delete_livre(livre_id: int, db: Session = Depends(get_db)):
    livre_existant = db.query(models.Livre).filter(models.Livre.id == livre_id).first()
    if not livre_existant:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    db.delete(livre_existant)
    db.commit()
    return {"detail": "Livre supprimé avec succès"}

# 4- Lister des livres
@app.get("/livres/", response_model=list[schemas.Livre])
def lister_livres(db: Session = Depends(get_db)):
    livres = db.query(models.Livre).all()
    return livres

# 5- Rechercher des livres
@app.get("/livres/recherche/", response_model=list[schemas.Livre])
def search_livre(q: str, db: Session = Depends(get_db)):
    return db.query(models.Livre).filter(
        (models.Livre.title.contains(q)) |
        (models.Livre.auteur.contains(q)) |
        (models.Livre.isbn.contains(q))
    ).all()