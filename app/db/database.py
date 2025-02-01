from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Need to use .env, just for teacher purposes
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postrgres@localhost/contacts_manager_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()