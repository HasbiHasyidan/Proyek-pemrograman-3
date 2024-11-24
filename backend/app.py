from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    description = Column(String)
    category = Column(String)
    amount = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    db = SessionLocal()
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    db.close()
    return transaction
