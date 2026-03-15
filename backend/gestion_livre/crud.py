from sqlalchemy.orm import Session
import models, schemas

def create_livre(db: Session, livre: schemas.LivreCreate):
    db_livre = models.Livre(**livre.dict())
    db.add(db_livre)
    db.commit()
    db.refresh(db_livre)
    return db_livre


def get_livres(db: Session):
    return db.query(models.Livre).all()


def delete_livre(db: Session, livre_id: int):
    livre = db.query(models.Livre).filter(models.Livre.id == livre_id).first()
    if livre:
        db.delete(livre)
        db.commit()
    return livre