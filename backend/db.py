from sqlalchemy.orm import Session
import models, schemas

def get_problem(db: Session, problem_id: str):
    return db.query(models.Problem).filter(models.Problem.id == problem_id).first()

def get_problems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Problem).offset(skip).limit(limit).all()

def create_problem(db: Session, problem: schemas.ProblemCreate, problem_id: str):
    db_problem = models.Problem(**problem.dict(), id=problem_id)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
